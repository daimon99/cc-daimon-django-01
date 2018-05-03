all: test

build:
	pyvenv env && \
	. env/bin/activate && \
	pip install -r requirements.txt && \
	python src/manage.py makemigrations && \
	python src/manage.py migrate

test: build
	echo "ok"