ENV      := $(shell which env)
VENV     := $(shell which virtualenv)
FLAKE8   := $(shell which flake8)
PIP      := $(shell which pip)
PYTHON   := $(shell which python)
PYTEST   := $(shell which py.test)

help:
	@echo "  bootstrap   create a development environment using virtualenv"
	@echo "  deps        install dependencies using pip"
	@echo "  lint        check style with flake8"
	@echo "  test        run all your tests using py.test"
	@echo "  run         run your server"


bootstrap:
	$(VENV) venv && \
	source venv/bin/activate
	$(MAKE) deps

deps:
	$(PIP) install -r requirements.txt

lint:
	$(FLAKE8) --exclude=venv . 

test:
	$(PYTEST) tests

run:
	$(PYTHON) run.py
