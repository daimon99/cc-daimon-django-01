all: test

clean:
	rm -rf /tmp/yourproject/

test: clean
	cookiecutter . --output-dir /tmp --no-input && \
	cd /tmp/yourproject && \
	make test
