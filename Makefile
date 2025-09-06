
.PHONY: install run test lint format clean help

VENV_PATH=/home/vscode/venv
PYTHON=${VENV_PATH}/bin/python
PIP=${VENV_PATH}/bin/pip

help: ## Show this help message
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Targets:'
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

install: ## Install project dependencies
	@echo "Installing dependencies..."
	python -m venv ${VENV_PATH}
	${PIP} install --upgrade pip
	${PIP} install -r requirements.txt

run: ## Run the application
	@echo "Starting the application..."
	${PYTHON} app.py

test: ## Run tests
	@echo "Running tests..."
	${PYTHON} -m pytest

lint: ## Run code linting with flake8
	@echo "Linting code..."
	${PYTHON} -m flake8 app/

format: ## Format code using black
	@echo "Formatting code..."
	${PYTHON} -m black app/

clean: ## Remove temporary files and caches
	@echo "Cleaning temporary files..."
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.pyd" -delete
	find . -type f -name ".coverage" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type d -name "*.egg" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -exec rm -rf {} +

dev-install: ## Install development dependencies
	@echo "Installing development dependencies..."
	${PIP} install -r requirements.txt
	${PIP} install black flake8 pytest pytest-cov mypy

build: ## Build Docker image
	@echo "Building Docker image..."
	docker build -t lab-study-app -f .devcontainer/Dockerfile .

docker-run: ## Run the application in Docker
	@echo "Running application in Docker..."
	docker run -p 8000:8000 lab-study-app
