setup:
    pipenv sync --dev
    pipenv run pre-commit install
    cp -n ./meditrack/example.env ./meditrack/.env
    pipenv run python manage.py collectstatic --noinput
    pipenv run python manage.py migrate

test:
    pipenv run pytest

vt:
    open ./htmlcov/index.html

run:
    pipenv run python manage.py runserver

format:
    pipenv run pre-commit run --all-files

format-fix:
    pipenv run pre-commit run black --all-files
    pipenv run ruff check --fix .

manage *COMMAND:
    pipenv run python manage.py {{COMMAND}}

docker *COMMAND:
    docker compose -f docker-compose.yml {{COMMAND}}

docker-manage *COMMAND:
    docker compose -f docker-compose.yml exec web python manage.py {{COMMAND}}