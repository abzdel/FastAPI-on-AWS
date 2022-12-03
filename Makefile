install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	black dblib/*.py

lint:
	pylint --disable=R,C *.py *.ipynb

all: install lint format