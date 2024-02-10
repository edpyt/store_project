TEST_COMPOSE="docker-compose.test.yml"

test:
	docker-compose -f $(TEST_COMPOSE) run --service-ports --build -d test-db
	poetry run pytest .
	docker-compose -f $(TEST_COMPOSE) kill test-db
