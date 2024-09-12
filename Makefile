DOCKER_COMP = docker compose -f docker-compose.yml
MANAGER = $(DOCKER_COMP) exec django python task_manager/manage.py
up:
	@$(DOCKER_COMP) up --detach --wait

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
	@pwd
	@pip freeze > ./pc_builder2/requirements.txt
	@$(DOCKER_COMP) exec django uv pip install -r ./requirements.txt