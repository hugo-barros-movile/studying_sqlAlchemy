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
	$(VENV) env && \
	. env/bin/activate && \
	make deps

deps:
	$(PIP) install --allow-all-external -r requirements.txt --allow-unverified Twisted-Core 

lint:
	. env/bin/activate && \
	$(FLAKE8) --exclude=env . 

test:
	make env && \
	. env/bin/activate && \
	$(PYTEST) tests

run:
	. env/bin/activate && \
	python run.py
