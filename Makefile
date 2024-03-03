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

package-reinstall:
	python3 -m pip install --force-reinstall --user dist/*.whl

lint:
	poetry run flake8

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml tests/

selfcheck:
	poetry check

check:
	make selfcheck
	make test
	make lint

.PHONY: install test lint selfcheck check build
