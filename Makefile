
VENV_DIR = venv
PYTHON = $(VENV_DIR)/bin/python3
PIP = $(VENV_DIR)/bin/pip

.PHONY: setup, freeze


$(VENV_DIR)/bin/activate:
	@echo "Creating virtual environment at: $(VENV_DIR)/"
	python3 -m venv $(VENV_DIR)

setup: $(VENV_DIR)/bin/activate
	@echo "Installing dependencies from requirements.txt..."
	$(PIP) install -r requirements.txt
	@echo "Creating .env if it doesn't exist..."
	@test -f .env || cp .env.template .env
	@echo "Setup complete."

freeze:
	@echo "Freezing dependencies > requirements.txt"
	$(PIP) freeze > requirements.txt
	@echo "requirements.txt updated."
