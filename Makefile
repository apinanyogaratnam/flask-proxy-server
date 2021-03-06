IMAGE := flask-proxy-server
VERSION := 0.0.2
REGISTRY_URL := ghcr.io/apinanyogaratnam/${IMAGE}:${VERSION}
REGISTRY_URL_LATEST := ghcr.io/apinanyogaratnam/${IMAGE}:latest

start:
	python3 proxy.py

build:
	docker build -t ${IMAGE} .

run:
	docker run -d -p 8000:8000 ${IMAGE}

up:
	docker-compose up

exec:
	docker exec -it $(sha) /bin/sh

auth:
	grep -v '^#' .env.local | grep -e "CR_PAT" | sed -e 's/.*=//' | docker login ghcr.io -u USERNAME --password-stdin

tag:
	docker tag ${IMAGE} ${REGISTRY_URL}
	docker tag ${IMAGE} ${REGISTRY_URL_LATEST}
	git tag -m "v${VERSION}" v${VERSION}

push:
	docker push ${REGISTRY_URL}
	docker push ${REGISTRY_URL_LATEST}
	git push --tags

all:
	make build && make auth && make tag && make push
