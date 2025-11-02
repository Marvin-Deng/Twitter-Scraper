# DIG-120

Project for DIG-120: Social Media Data Analytics

## Setup

```shell
git clone git@github.com:Marvin-Deng/DIG-120.git

make setup
```

## Running

1. Log into [Twitter](https://x.com/home). The script requires active session cookies.

2. Run script

```shell
make run
```

3. Allow the script access to browser cookies. Enter your computer password and click "Always allow".
   <img width="428" height="181" alt="Screenshot 2025-11-02 at 1 58 30 PM" src="https://github.com/user-attachments/assets/4ab7ebed-70d6-43ca-9167-5719a4e5d9c4" />

### Update Requirements

```shell
make freeze
```

### Formatter

```shell
black .
```

## Links

- [Twikit API](https://twikit.readthedocs.io/en/latest/twikit.html)
