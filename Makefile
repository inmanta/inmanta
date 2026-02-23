# Shortcuts for various dev tasks. Based on makefile from pydantic
.DEFAULT_GOAL := all
isort = isort -rc src tests
black = black src tests

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
	rm -rf build dist *.egg-info
	find -name .env | xargs rm -rf
	python setup.py clean

# The following 'dummy' steps are here because they are required by the generic extension pipeline
.PHONY: ci-pep8 ci-mypy ci-test ci-install
ci-pep8:
	@echo Skipping ci-pep8 step
ci-mypy:
	@echo Skipping ci-mypy step
ci-test:
	@echo Skipping ci-test step
ci-install:
	@echo Skipping ci-install step
