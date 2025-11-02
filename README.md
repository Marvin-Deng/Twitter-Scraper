# DIG-120

## Usage

### Setup

```shell
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Running

1. Log into [Twitter](https://x.com/home)

2. Run script

```shell
source venv/bin/activate
python3 src/main.py
```

3. Allow the script access to browser cookies. Enter your computer password and click "Always allow".
<img width="428" height="181" alt="Screenshot 2025-11-02 at 1 58 30 PM" src="https://github.com/user-attachments/assets/4ab7ebed-70d6-43ca-9167-5719a4e5d9c4" />

### Update Requirements

```shell
pip freeze > requirements.txt
```

### Formatter

```shell
black .
```
