.PHONY: build test

default: build test

build:
	docker build -t cache .

test:
	docker run --rm cache nosetests tests