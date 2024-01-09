install:
	poetry install

gendiff:
	poetry run gendiff

build: check
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python -m pip install dist/*.whl

lint:
	poetry run flake8

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml tests/

selfcheck:
	poetry check

check: selfcheck test lint

.PHONY: install test lint selfcheck check build