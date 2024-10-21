DOCKER_COMP = docker compose -f docker-compose.yml
MANAGER = $(DOCKER_COMP) exec django python manage.py
# celery -A pc_builder worker --loglevel=INFO --max-tasks-per-child 1 --autoscale=3,1 -Q ${CELERY_QUEUE_UPLOAD},

up:
	@$(DOCKER_COMP) up --detach --wait

build:
	@$(DOCKER_COMP) up --build

down:
	@$(DOCKER_COMP) down --remove-orphans

bash:
	@$(DOCKER_COMP) exec $(name) bash

migrations:
	@$(MANAGER) makemigrations $(ARGS)

migrate:
	@$(MANAGER) migrate $(ARGS)

logs:
	@$(DOCKER_COMP) logs $(name) --tail=0 --follow

update:
	@pip freeze > ./pc_builder2/requirements.txt
	@$(DOCKER_COMP) exec django uv pip install -r ./requirements.txt