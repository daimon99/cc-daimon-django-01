.DEFAULT_GOAL := help

define BROWSER_PYSCRIPT
import os, webbrowser, sys, re, platform

try:
        from urllib import pathname2url
except:
        from urllib.request import pathname2url

if platform.system() != 'Linux': 
	is_http = re.match('http://.*', sys.argv[1])
	if is_http:
		webbrowser.open(sys.argv[1])
	else:
		webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
        match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
        if match:
                target, help = match.groups()
                print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

BROWSER := python -c "$$BROWSER_PYSCRIPT"

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

all: test

build: ## 构建
	pipenv install --skip-lock -r requirements.txt && \
	pipenv run python src/manage.py makemigrations && \
	pipenv run python src/manage.py migrate

test: build
	echo "ok"

stop: ## 停止
	-pkill -P `cat .pid`

run: stop ## 运行
	nohup pipenv run python src/manage.py runserver {{cookiecutter.port}} > {{cookiecutter.project_name}}.log & echo $$! > .pid
	sleep 5
	$(BROWSER) http://localhost:{{cookiecutter.port}}
