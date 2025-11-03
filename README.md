# DIG-120

Project for DIG-120: Social Media Data Analytics

## Setup

```shell
git clone git@github.com:Marvin-Deng/DIG-120.git

make setup
```

## Running

1. Log into [Twitter](https://x.com/home). The script requires active session cookies.

2. Fix [`itemContent` key bug](https://github.com/d60/twikit/issues/375) in the twikit library. Its fixed [in this PR](https://github.com/d60/twikit/pull/377) but not merged.

- Go into `venv/bin/twikit/client/client.py` and change `reply_next_cursor = entries[-1]['content']['itemContent']['value']` to `reply_next_cursor = entries[-1]['content']['value']`

3. Run script

```shell
make run
```

4. Allow the script access to browser cookies. Enter your computer password and click "Always allow".
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

### Project Links

- [Notebooks + Assignments](https://docs.google.com/document/d/1s9ht5jLj01NJ3QdozLH6LFmnPcYn3m2UMf0pEPqF5B4/edit?tab=t.0)

### Twikit

- [API Docs](https://twikit.readthedocs.io/en/latest/twikit.html)
- [Rate Limit](https://github.com/d60/twikit/blob/main/ratelimits.md)
- [Twikit Tweet Object](https://twikit.readthedocs.io/en/latest/twikit.html#module-twikit.tweet)
