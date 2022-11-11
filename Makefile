install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	black dblib/*.py

lint:
	pylint --disable=R,C dblib

all: install lint format