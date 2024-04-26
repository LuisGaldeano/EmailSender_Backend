#!make
include .env
.DEFAULT_GOAL=up
MAKEFLAGS += --no-print-directory

# Constants
TAIL_LOGS = 50
PYTEST_WORKERS = 8

up:
	$s docker compose up --force-recreate -d

down:
	$s docker compose down

down-up: down up

up-build:
	$s docker compose down
	$s docker compose up --force-recreate -d --build

build:
	$s docker compose build

complete-build:
	$s docker image prune -af
	$s docker compose build
	$s docker compose down
	$s docker compose up --force-recreate -d

logs:
	$s docker logs --tail ${TAIL_LOGS} -f ${PROJECT_NAME}_backend

bash:
	$s docker exec -it ${PROJECT_NAME}_backend bash

sh:
	$s docker exec -it ${PROJECT_NAME}_backend bash

shell:
	$s docker exec -it ${PROJECT_NAME}_backend python manage.py shell_plus


make-migrations:
	$s docker exec -it ${PROJECT_NAME}_backend python manage.py makemigrations

migrate:
	$s docker exec -it ${PROJECT_NAME}_backend python manage.py migrate $(ARGS)

migrations:
	$s docker exec -it ${PROJECT_NAME}_backend python manage.py makemigrations
	$s docker exec -it ${PROJECT_NAME}_backend python manage.py migrate

make-messages:
	$s docker exec -it ${PROJECT_NAME}_backend python manage.py makemessages -a


IMAGES := $(shell docker images -qa)
clean-images:
	$s docker rmi $(IMAGES) --force

CONTAINERS := $(shell docker ps -qa)
remove-containers:
	$s docker rm $(CONTAINERS)

restart:
	$s docker compose restart

update-requirements:
	$s docker exec ${PROJECT_NAME}_backend poetry update

all-logs:
	$s docker compose logs --tail ${TAIL_LOGS} -f