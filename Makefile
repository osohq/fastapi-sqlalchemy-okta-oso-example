.PHONY: requirements fmt run

run: requirements
	uvicorn app.main:app --reload --reload-dir=app

requirements: .make.requirements-install

.make.requirements-install: requirements.txt
	pip install -r requirements.txt
	touch $@

fmt: requirements
	black .
