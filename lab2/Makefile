APP=secure_programming.lab.sqli_and_xss

all: build

build:
	docker build --rm --tag=$(APP) .

run:
	docker run -p 0.0.0.0:8000:8000/tcp -it --rm $(APP)

clean:
	docker image rm $(APP)
	docker system prune
