# Shortcuts for various dev tasks. Based on makefile from pydantic
.DEFAULT_GOAL := all
isort = isort -rc src tests
black = black src tests

VERSION := $(shell python3 setup.py -V)
RPMDIR-EL7 := "$(shell pwd)/rpms-el7"

ifndef $(RELEASE)
RELEASE := dev
endif

ifndef ISO_MAJOR_VERSION
ifeq ($(RPM_REPOSITORY),iso)
$(error ISO_MAJOR_VERSION should be set if RPM_REPOSITORY is set to iso)
endif
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

ifeq ($(RPM_REPOSITORY),oss)
REPOMANAGER_REPO := "inmanta-oss-$(RELEASE)"
else
ifeq ($(RELEASE), dev)
ISO_REPO := inmanta-service-orchestrator-$(ISO_MAJOR_VERSION)-dev
REPOMANAGER_REPO := inmanta-service-orchestrator-dev/$(ISO_MAJOR_VERSION)
endif
ifeq ($(RELEASE), next)
ISO_REPO := inmanta-service-orchestrator-$(ISO_MAJOR_VERSION)-next
REPOMANAGER_REPO := inmanta-service-orchestrator-next/$(ISO_MAJOR_VERSION)
endif
ifeq ($(RELEASE), stable)
ISO_REPO := inmanta-service-orchestrator-$(ISO_MAJOR_VERSION)
REPOMANAGER_REPO := inmanta-service-orchestrator/$(ISO_MAJOR_VERSION)
endif
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
	rm -rf ${RPMDIR-EL7}
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

ifeq ($(RPM_REPOSITORY),oss)
	mock -r inmanta-and-epel-7-x86_64 --bootstrap-chroot --enablerepo="inmanta-oss-$(RELEASE)" --buildsrpm --spec inmanta.spec --sources dist --resultdir ${RPMDIR-EL7}
	mock -r inmanta-and-epel-7-x86_64 --bootstrap-chroot --enablerepo="inmanta-oss-$(RELEASE)" --rebuild ${RPMDIR-EL7}/python3-inmanta-${VERSION}-*.src.rpm --resultdir ${RPMDIR-EL7}
else
	mock -r inmanta-and-epel-7-x86_64 --bootstrap-chroot --enablerepo="$(ISO_REPO)" --buildsrpm --spec inmanta.spec --sources dist --resultdir ${RPMDIR-EL7}
	mock -r inmanta-and-epel-7-x86_64 --bootstrap-chroot --enablerepo="$(ISO_REPO)" --rebuild ${RPMDIR-EL7}/python3-inmanta-${VERSION}-*.src.rpm --resultdir ${RPMDIR-EL7}
endif

.PHONY: upload
upload: ensure-valid-release-type
# Can be extended later with el8
	pip3 install cloudsmith-cli
	@for path_to_rpm in $(shell find rpms-el7 -name '*.x86_64.rpm'); do \
		rpm=$$(basename $$path_to_rpm) ; \
		el_version=$$(echo $$rpm| rev| cut -d '.' -f 3| rev |tr -d 'el') ; \
		if [ "$${RPM_REPOSITORY}" = "iso" ] && [ $${el_version} = "7" ] && [ $${ISO_MAJOR_VERSION} = "3" ]; then \
			repomanager@artifacts.ii.inmanta.com "/usr/bin/repomanager --config /etc/repomanager.toml --repo ${REPOMANAGER_REPO} --distro el7 --file - --file-name $${rpm}" < $${path_to_rpm} ; \
		fi ; \
		if [ "$${RPM_REPOSITORY}" = "oss" ]; then \
			if [ "$${RELEASE}" = "stable" ]; then \
				cloudsmith push rpm inmanta/oss-stable-staging-el$${el_version} $${path_to_rpm} ; \
			else \
				cloudsmith push rpm inmanta/oss-$${RELEASE}-el$${el_version} $${path_to_rpm} ;\
			fi ;\
		else \
			if [ "$${RELEASE}" = "stable" ]; then \
				cloudsmith push rpm inmanta/inmanta-service-orchestrator-$${ISO_MAJOR_VERSION}-stable-staging $${path_to_rpm} ; \
			else \
				cloudsmith push rpm inmanta/inmanta-service-orchestrator-$${ISO_MAJOR_VERSION}-$${RELEASE} $${path_to_rpm} ;\
			fi ;\
		fi ; \
	done
	@if [ "${RPM_REPOSITORY}" = "oss" ] && [ "${RELEASE}" = "stable" ]; then \
		for el_version in '7'; do \
			cloudsmith list packages inmanta/oss-stable-staging-el$${el_version} -F json | \
			jq -r ".data[].identifier_perm" | \
			xargs -I pkg_id cloudsmith copy inmanta/oss-stable-staging-el$${el_version}/pkg_id oss-stable-el$${el_version} ; \
		done ;\
	fi ;\
