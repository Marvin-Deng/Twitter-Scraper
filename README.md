# DIG-120

Project for DIG-120: Social Media Data Analytics

## Setup

1. Clone the repo.

```shell
git clone git@github.com:Marvin-Deng/DIG-120.git
```

2. Run setup.

```shell
make setup
```

3. Add your Twitter username to `.env`. If you screen name is @username123, then your username is username123.

```shell
# .env

USERNAME=username123
```

## Running

1. Fix [`itemContent` key bug](https://github.com/d60/twikit/issues/375) in the twikit library. Its fixed [in this PR](https://github.com/d60/twikit/pull/377) but not merged. Ignore this step if the fix was merged.

- Go into `venv/bin/twikit/client/client.py` and change `reply_next_cursor = entries[-1]['content']['itemContent']['value']` to `reply_next_cursor = entries[-1]['content']['value']`

2. Log into [Twitter](https://x.com/home) if you have't already. The script requires active session cookies.

3. Run script.

```shell
# Get tweets for a specific user
python3 src/main.py --action tweets --screenname elonmusk --count 10

# Get top replies from a tweet
python src/main.py --action replies --screenname elonmusk --tweet-id 1985104111499657502 --top 5 --count 100
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
