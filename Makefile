# Shortcuts for various dev tasks. Based on makefile from pydantic
.DEFAULT_GOAL := all
isort = isort -rc src tests
black = black src tests

VERSION := $(shell python3 setup.py -V)
RPMDIR_EL7 := "$(shell pwd)/rpms-el7"
RPMDIR_EL8 := "$(shell pwd)/rpms-el8"

ifndef $(RELEASE)
RELEASE := dev
endif

ifeq ($(BUILDID),)
TIMESTAMP := $(shell date --utc +%Y%m%d%H%M)
   ifeq ("$(RELEASE)","dev")
BUILDID := .dev$(TIMESTAMP)
BUILDID_EGG := .dev$(TIMESTAMP)
   endif
   ifeq ("$(RELEASE)","next")
BUILDID := .next$(TIMESTAMP)
BUILDID_EGG := rc$(TIMESTAMP)
   endif
endif

ifeq ($(RELEASE), dev)
ISO_REPO := inmanta-service-orchestrator-3-dev
REPOMANAGER_REPO := inmanta-service-orchestrator-dev/3
endif
ifeq ($(RELEASE), next)
ISO_REPO := inmanta-service-orchestrator-3-next
REPOMANAGER_REPO := inmanta-service-orchestrator-next/3
endif
ifeq ($(RELEASE), stable)
ISO_REPO := inmanta-service-orchestrator-3
REPOMANAGER_REPO := inmanta-service-orchestrator/3
endif

.PHONY: install
install:
	pip install -U setuptools pip
	pip install -U -r requirements.txt
	pip install -e .

.PHONY: format
format:
	$(isort)
	$(black)

.PHONY: pep8
pep8:
	pip install -c requirements.txt pep8-naming flake8-black flake8-isort
	flake8 src tests

all: pep8

.PHONY: clean
clean:
	rm -rf `find . -name __pycache__`
	rm -f `find . -type f -name '*.py[co]' `
	rm -f `find . -type f -name '*~' `
	rm -f `find . -type f -name '.*~' `
	rm -rf .cache
	rm -rf .pytest_cache
	rm -rf .mypy_cache
	rm -rf mypy
	rm -rf coverage
	rm -rf *.egg-info
	rm -f .coverage
	rm -f .coverage.*
	rm -rf build dist *.egg-info rpms
	find -name .env | xargs rm -rf
	python setup.py clean

.PHONY: ensure-valid-release-type
ensure-valid-release-type:
ifneq ($(RELEASE), dev)
  ifneq ($(RELEASE), next)
    ifneq ($(RELEASE), stable)
    $(error RELEASE parameter should have value 'dev', 'next' or 'stable')
    endif
  endif
endif

.PHONY: build
build: ensure-valid-release-type
	rm -rf dist/*
	pip3 install -U wheel
	python3 setup.py egg_info -Db "$(BUILDID_EGG)" sdist bdist_wheel

.PHONY: upload-python-package
upload-python-package: build
	pip install -U devpi-client
	devpi use https://artifacts.internal.inmanta.com/inmanta/$(RELEASE)
	devpi login ${DEVPI_USER} --password=${DEVPI_PASS}
	# upload packages only if this version hasn't been upload previously
	if [ -z "$$(devpi list $$(ls dist/*-py3-*.whl | sed 's/dist\/\(.*\)-\(.*\)-py3-.*\.whl/\1==\2/'))" ]; then \
		devpi upload dist/*; \
	fi
	devpi logoff

.PHONY: rpm
rpm: ensure-valid-release-type build
	rm -rf ${RPMDIR_EL7}
	rm -rf ${RPMDIR_EL8}
	sed -i '0,/^%define version.*/s/^%define version.*/%define version ${VERSION}/' inmanta.spec

ifneq ($(BUILDID),)
	sed -i '0,/^%define buildid.*/s/^%define buildid.*/%define buildid $(BUILDID)/' inmanta.spec
	sed -i '0,/^%define buildid_egg.*/s/^%define buildid_egg.*/%define buildid_egg $(BUILDID_EGG)/' inmanta.spec
else
	sed -i '0,/^%define buildid.*/s/^%define buildid.*/%define buildid %{nil}/' inmanta.spec
	sed -i '0,/^%define buildid_egg.*/s/^%define buildid_egg.*/%define buildid_egg %{nil}/' inmanta.spec
endif

ifneq ("$(RELEASE)","stable")
	sed -i '0,/^%define release.*/s/^%define release.*/%define release 0/' inmanta.spec
endif

	mock -r inmanta-and-epel-7-x86_64 --bootstrap-chroot --enablerepo="inmanta-oss-$(RELEASE),$(ISO_REPO)" --buildsrpm --spec inmanta.spec --sources dist --resultdir ${RPMDIR_EL7}
	mock -r inmanta-and-epel-7-x86_64 --bootstrap-chroot --enablerepo="inmanta-oss-$(RELEASE),$(ISO_REPO)" --rebuild ${RPMDIR_EL7}/python3-inmanta-${VERSION}-*.src.rpm --resultdir ${RPMDIR_EL7}

	mock -r epel-8-x86_64 --bootstrap-chroot --enablerepo="inmanta-oss-$(RELEASE),$(ISO_REPO)" --buildsrpm --spec inmanta.spec --sources dist --resultdir ${RPMDIR_EL8}
	mock -r epel-8-x86_64 --bootstrap-chroot --enablerepo="inmanta-oss-$(RELEASE),$(ISO_REPO)" --rebuild ${RPMDIR_EL8}/python3-inmanta-${VERSION}-*.src.rpm --resultdir ${RPMDIR_EL8}


.PHONY: upload
upload: RPM := $(shell basename ${RPMDIR_EL7}/python3-inmanta-${VERSION}-*.x86_64.rpm)

.PHONY: upload
upload: ensure-valid-release-type
	@echo Uploading $(RPM)
	ssh repomanager@artifacts.ii.inmanta.com "/usr/bin/repomanager --config /etc/repomanager.toml --repo $(REPOMANAGER_REPO) --distro el7 --file - --file-name ${RPM}" < ${RPMDIR_EL7}/${RPM}
