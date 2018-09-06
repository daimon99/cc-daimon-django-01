all: test

build:
	pipenv install --skip-lock -r requirements.txt && \
	pipenv run python src/manage.py makemigrations && \
	pipenv run python src/manage.py migrate

test: build
	echo "ok"

run: build
	pipenv run python src/manage.py runserver
