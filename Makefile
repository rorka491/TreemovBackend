rabbit_compose_up_build:
	docker compose -f ./services/rabbitmq/docker-compose.yml up --build
rabbit_compose_up:
	docker compose -f ./services/rabbitmq/docker-compose.yml up -d
auth_compose_up:
	docker compose -f ./services/auth-service/docker-compose.yml up -d
auth_compose_up_build:
	docker compose -f ./services/auth-service/docker-compose.yml up --build
crm_core_compose_up_build:
	docker compose -f ./services/crm_core/docker-compose.yml up --build
crm_core_compose_up:
	docker compose -f ./services/crm_core/docker-compose.yml up -d


