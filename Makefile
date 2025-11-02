
VENV_DIR = venv
PYTHON = $(VENV_DIR)/bin/python3
PIP = $(VENV_DIR)/bin/pip

.PHONY: setup, run, freeze


$(VENV_DIR)/bin/activate:
	@echo "Creating virtual environment at: $(VENV_DIR)/"
	python3 -m venv $(VENV_DIR)

setup: $(VENV_DIR)/bin/activate
	@echo "Installing dependencies from requirements.txt..."
	$(PIP) install -r requirements.txt
	@echo "Setup complete."


run: $(VENV_DIR)/bin/activate
	@echo "Running main script (src/main.py)..."
	$(PYTHON) src/main.py

freeze:
	@echo "Freezing dependencies > requirements.txt"
	$(PIP) freeze > requirements.txt
	@echo "requirements.txt updated."
