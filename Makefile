#   Makefile
#
# license   http://opensource.org/licenses/MIT The MIT License (MIT)
# copyright Copyright (c) 2016, TUNE Inc. (http://www.tune.com)
#

PYTHON3 := $(shell which python3)
PYTHON27 := $(shell which python2.7)
PIP3    := $(shell which pip3)
PY_MODULES := pip setuptools pylint flake8 pprintpp pep8 requests six sphinx wheel retry validators python-dateutil
PYTHON3_SITE_PACKAGES := $(shell python3 -c "import site; print(site.getsitepackages()[0])")

LOGGING_MV_INTGS_PKG := logging-mv-integrations
LOGGING_MV_INTGS_PKG_PREFIX := logging_mv_integrations

PKG_SUFFIX := py3-none-any.whl

VERSION := $(shell $(PYTHON3) setup.py version)
LOGGING_MV_INTGS_WHEEL_ARCHIVE := dist/$(LOGGING_MV_INTGS_PKG_PREFIX)-$(VERSION)-$(PKG_SUFFIX)

LOGGING_MV_INTGS_FILES := $(shell find logging_mv_integrations ! -name '__init__.py' -type f -name "*.py")
LINT_REQ_FILE := requirements-pylint.txt
REQ_FILE      := requirements.txt
SETUP_FILE    := setup.py
ALL_FILES     := $(LOGGING_MV_INTGS_FILES) $(REQ_FILE) $(SETUP_FILE)

# Report the current logging-mv-integrations version.
version:
	@echo MV Integration Base Version: $(VERSION)

# Install Python 3 via Homebrew.
brew-python:
	brew install python3
	$(eval $(shell which python3))
	$(PIP3) install --upgrade $(PY_MODULES)

# Upgrade pip. Note that this does not install pip if you don't have it.
# Pip must already be installed to work with this Makefile.
pip:
	$(PIP3) install --upgrade pip

clean:
	@echo "======================================================"
	@echo clean
	@echo "======================================================"
	rm -fR __pycache__ venv "*.pyc" build/*    \
		$(LOGGING_MV_INTGS_PKG_PREFIX)/__pycache__/         \
		$(LOGGING_MV_INTGS_PKG_PREFIX)/helpers/__pycache__/ \
		$(LOGGING_MV_INTGS_PKG_PREFIX).egg-info/*
	find ./* -maxdepth 0 -name "*.pyc" -type f -delete
	find $(LOGGING_MV_INTGS_PKG_PREFIX) -name "*.pyc" -type f -delete

# Install the project requirements.
requirements: $(REQ_FILE) pip
	$(PIP3) install --upgrade -r $(REQ_FILE)

# Make a project distributable.
dist: clean
	@echo "======================================================"
	@echo dist
	@echo "======================================================"
	@echo Building: $(LOGGING_MV_INTGS_WHEEL_ARCHIVE)
	$(PYTHON3) --version
	find ./dist/ -name $(LOGGING_MV_INTGS_PKG_PREFIX_PATTERN) -exec rm -vf {} \;
	$(PYTHON3) $(SETUP_FILE) bdist_wheel
	$(PYTHON3) $(SETUP_FILE) bdist_egg
	$(PYTHON3) $(SETUP_FILE) sdist --format=zip,gztar
	ls -al ./dist/$(LOGGING_MV_INTGS_PKG_PREFIX_PATTERN)

# DIST UPDATE INTENTIONALLY REMOVED

# Build and install the module. Apparently this target isn't really used
# anymore. It's a candidate for removal, or at least redefinition, since
# "build" is a useful target, generally speaking.
build: $(ALL_FILES) pip requirements
	$(PYTHON3) $(SETUP_FILE) clean
	$(PYTHON3) $(SETUP_FILE) build
	$(PYTHON3) $(SETUP_FILE) install

uninstall:
	@echo "======================================================"
	@echo uninstall $(LOGGING_MV_INTGS_PKG)
	@echo "======================================================"
	$(PIP3) install --upgrade list
	@if $(PIP3) list --format=legacy | grep -F $(LOGGING_MV_INTGS_PKG) > /dev/null; then \
		echo "python package $(LOGGING_MV_INTGS_PKG) Found"; \
		$(PIP3) uninstall --yes $(LOGGING_MV_INTGS_PKG); \
	else \
		echo "python package $(LOGGING_MV_INTGS_PKG) Not Found"; \
	fi;

remove-package: uninstall
	@echo "======================================================"
	@echo remove-package $(LOGGING_MV_INTGS_PKG)
	@echo "======================================================"
	rm -fR $(PYTHON3_SITE_PACKAGES)/$(LOGGING_MV_INTGS_PKG_PREFIX)*

# Install the module from a binary distribution archive.
install: remove-package
	@echo "======================================================"
	@echo install $(LOGGING_MV_INTGS_PKG)
	@echo "======================================================"
	$(PIP3) install --upgrade pip
	$(PIP3) install --upgrade $(LOGGING_MV_INTGS_WHEEL_ARCHIVE)
	$(PIP3) freeze | grep $(LOGGING_MV_INTGS_PKG)

# Install project for local development. Changes to the files will be reflected in installed code
local-dev-editable: remove-package
	@echo "======================================================"
	@echo local-dev-editable $(LOGGING_MV_INTGS_PKG)
	@echo "======================================================"
	$(PIP3) install --upgrade freeze
	$(PIP3) install --upgrade --editable .
	$(PIP3) freeze | grep $(LOGGING_MV_INTGS_PKG)

local-dev: remove-package
	@echo "======================================================"
	@echo local-dev $(LOGGING_MV_INTGS_PKG)
	@echo "======================================================"
	$(PIP3) install --upgrade freeze
	$(PIP3) install --upgrade .
	$(PIP3) freeze | grep $(LOGGING_MV_INTGS_PKG)

dist:
	rm -fR ./dist/*
	$(PYTHON3) $(SETUP_FILE) sdist --format=zip,gztar upload
	$(PYTHON27) $(SETUP_FILE) bdist_egg upload
	$(PYTHON27) $(SETUP_FILE) bdist_wheel upload
	$(PYTHON3) $(SETUP_FILE) bdist_egg upload
	$(PYTHON3) $(SETUP_FILE) bdist_wheel upload

build:
	$(PIP3) install --upgrade -r requirements.txt
	$(PYTHON3) $(SETUP_FILE) clean
	$(PYTHON3) $(SETUP_FILE) build
	$(PYTHON3) $(SETUP_FILE) install


# Register the module with PyPi.
register:
	$(PYTHON3) $(SETUP_FILE) register

flake8:
	flake8 --ignore=F401,E265,E129 tune
	flake8 --ignore=E123,E126,E128,E265,E501 tests

lint: clean
	pylint --rcfile .pylintrc logging_mv_integrations | more

lint-requirements: $(LINT_REQ_FILE)
	$(PIP3) install --upgrade -f $(LINT_REQ_FILE)

pep8: lint-requirements
	@echo pep8: $(LOGGING_MV_INTGS_FILES)
	$(PYTHON3) -m pep8 --config .pep8 $(LOGGING_MV_INTGS_FILES)

pyflakes: lint-requirements
	@echo pyflakes: $(LOGGING_MV_INTGS_FILES)
	$(PYTHON3) -m pyflakes $(LOGGING_MV_INTGS_FILES)

pylint: lint-requirements
	@echo pylint: $(LOGGING_MV_INTGS_FILES)
	$(PYTHON3) -m pylint --rcfile .pylintrc $(LOGGING_MV_INTGS_FILES) --disable=C0330,F0401,E0611,E0602,R0903,C0103,E1121,R0913,R0902,R0914,R0912,W1202,R0915,C0302 | more -30

site-packages:
	@echo $(PYTHON3_SITE_PACKAGES)

list-package:
	ls -al $(PYTHON3_SITE_PACKAGES)/$(LOGGING_MV_INTGS_PKG_PREFIX)*


.PHONY: brew-python clean register lint pylint pep8 pyflakes examples analysis
