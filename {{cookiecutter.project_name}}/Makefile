all: test

build:
	pipenv install --skip-lock -r requirements.txt && \
	pipenv shell && \
	python src/manage.py makemigrations && \
	python src/manage.py migrate

test: build
	echo "ok"

run: build
	python src/manage.py runserver
