APP=secure_programming.lab.cache_poisoin

all: build

build:
	docker build --rm --tag=$(APP) .

run:
	docker run -p 127.0.0.1:5000:5000/tcp -it --rm $(APP)

clean:
	docker image rm $(APP)
	docker system prune
