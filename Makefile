.PHONY: help install test run docker-build docker-run docker-stop clean

# Colors
GREEN  := $(shell tput -Txterm setaf 2)
YELLOW := $(shell tput -Txterm setaf 3)
RESET  := $(shell tput -Txterm sgr0)

help:  ## Hiển thị help
	@echo ''
	@echo '${GREEN}Makefile Commands:${RESET}'
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  ${YELLOW}%-15s${RESET} %s\n", $$1, $$2}'
	@echo ''

install: ## Install Python dependencies
	@echo "${GREEN}Installing dependencies...${RESET}"
	pip install -r requirements.txt

test: ## Run tests với pytest
	@echo "${GREEN}Running tests...${RESET}"
	pytest test_app.py -v --cov=app --cov-report=term-missing

run: ## Chạy ứng dụng local
	@echo "${GREEN}Starting Flask application...${RESET}"
	python app.py

docker-build: ## Build Docker image
	@echo "${GREEN}Building Docker image...${RESET}"
	docker build -t devops-cicd-demo:latest .

docker-run: ## Chạy Docker container
	@echo "${GREEN}Running Docker container...${RESET}"
	docker run -d -p 5000:5000 --name devops-demo devops-cicd-demo:latest
	@echo "${GREEN}Application running at http://localhost:5000${RESET}"

docker-compose-up: ## Chạy với docker-compose
	@echo "${GREEN}Starting with docker-compose...${RESET}"
	docker-compose up -d
	@echo "${GREEN}Application running at http://localhost:5000${RESET}"

docker-compose-down: ## Dừng docker-compose
	@echo "${YELLOW}Stopping docker-compose...${RESET}"
	docker-compose down

docker-stop: ## Dừng và xóa container
	@echo "${YELLOW}Stopping Docker container...${RESET}"
	docker stop devops-demo || true
	docker rm devops-demo || true

docker-logs: ## Xem logs của container
	docker logs -f devops-demo

clean:  ## Dọn dẹp files tạm
	@echo "${YELLOW}Cleaning up...${RESET}"
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.coverage" -delete
	rm -rf htmlcov/ .pytest_cache/ .coverage

lint: ## Check code quality với flake8
	@echo "${GREEN}Running linter...${RESET}"
	flake8 app.py test_app.py --max-line-length=120

all: clean install test docker-build ## Run all:  clean, install, test, build