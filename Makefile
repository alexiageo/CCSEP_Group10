# A sample Makefile to use make command to build, test and run the program
# Guide: https://philpep.org/blog/a-makefile-for-your-dockerfiles/
APP=app.py

all: build

build:
	docker build --rm --tag=$(APP) .
	docker image prune -f

test:
	docker run -it --rm $(APP) python manage.py test

run:
	docker run -p 0.0.0.0:8000:8000/tcp -it --rm $(APP)

clean:
	docker image rm $(APP)
	docker system prune

.PHONY: all test clean
