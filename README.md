# Twitter Scraper

Twitter API script built using [twikit](https://github.com/d60/twikit).

## Links

### Project

- [Notebooks + Assignments](https://docs.google.com/document/d/1s9ht5jLj01NJ3QdozLH6LFmnPcYn3m2UMf0pEPqF5B4/edit?tab=t.0)

### Twikit

- [API Docs](https://twikit.readthedocs.io/en/latest/twikit.html)
- [Rate Limit](https://github.com/d60/twikit/blob/main/ratelimits.md)
- [Twikit Tweet Object](https://twikit.readthedocs.io/en/latest/twikit.html#module-twikit.tweet)

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

4. Theres an issue with [itemContent](https://github.com/d60/twikit/issues/375) in `twikit` which is fixed [in this PR](https://github.com/d60/twikit/pull/377) but isn't merged. Ignore this step if the fix was merged.

- Go into `venv/bin/twikit/client/client.py` and change `reply_next_cursor = entries[-1]['content']['itemContent']['value']` to `reply_next_cursor = entries[-1]['content']['value']`

## Usage

1. Log into [Twitter](https://x.com/home). Make sure the username is the same as the one you added to `.env`. The script needs active session cookies in order to bypass Cloudflare restrictions.

2. Run script.

- Arguments
  - --action, -a: tweets or replies (default: tweets)
  - --screenname, -s: Twitter username to fetch tweets for (required for tweets action)
  - --tweet-id, -i: Tweet ID to fetch replies for (required for replies action)
  - --count, -c: Number of tweets or replies to fetch (default: 100)
  - --top, -t: Number of top replies to show (for replies only, default: 5)

```shell
# Get script arguments
python src/main.py -h

# Get tweets for a specific user. API limit is 50 requests every 15 minutes. Keep count to below 50.
python src/main.py -a tweets -s elonmusk -c 10
python3 src/main.py --action tweets --screenname elonmusk --count 10

# Get top replies from a tweet. API limit is 150 requests every 15 minutes. Keep count to below 150.
python src/main.py -a replies -s elonmusk -i 1984717014620078498 -t 5 -c 100
python src/main.py --action replies --screenname elonmusk --tweet-id 1984717014620078498 --top 5 --count 100
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
