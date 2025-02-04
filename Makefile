### Makefile

# Global Makefile for managing the Speech4Kids microservices

.PHONY: build up down logs test

# Build all services
default: build

build:
	docker-compose build

# Start all services
up:
	docker-compose up -d

# Stop all services
down:
	docker-compose down

# View logs for all services
logs:
	docker-compose logs -f

# Run tests for all services
test:
	@echo "Running tests for all services..."
	@docker-compose exec gateway pytest
	@docker-compose exec asr_service pytest
	@docker-compose exec tts_service pytest
	@docker-compose exec nlp_service pytest

# Lint all services
lint:
	@echo "Linting all services..."
	@docker-compose exec gateway flake8
	@docker-compose exec asr_service flake8
	@docker-compose exec tts_service flake8
	@docker-compose exec nlp_service flake8