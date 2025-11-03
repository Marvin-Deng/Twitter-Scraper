# Twitter Scraper

Twitter API script built using [twikit](https://github.com/d60/twikit). It allows you to get the most viewed tweets from a specific user and get the most liked replies for a set of tweets, and export the results as CSV files.

For tweets, the API limit is 50 requests (~1000 tweets) every 15 minutes.

For getting individual tweets by ID (replies), the API limit is 150 requests (~3000 replies) every 15 minutes.

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

3. Add your Twitter username to `.env`. If your screen name is @username123, then your username is username123.

```shell
# .env

USERNAME=username123
```

4. Theres an issue with twikit's [get_tweet_by_id()](https://github.com/d60/twikit/issues/375) which is fixed [in this PR](https://github.com/d60/twikit/pull/377) but isn't merged. Ignore this step if the fix was merged.

- Go into `venv/bin/twikit/client/client.py` and change `reply_next_cursor = entries[-1]['content']['itemContent']['value']` to `reply_next_cursor = entries[-1]['content']['value']`

## Usage

1. Log into [Twitter](https://x.com/home). Make sure the username is the same as the one you added to `.env`. Keep the Twitter webpage open while running the script. The script needs active session cookies in order to bypass Cloudflare restrictions.

2. Start virtual environment.

```shell
# macOS / Linux (bash/zsh)
source venv/bin/activate

# Windows (Command Prompt)
venv\Scripts\activate

# Windows (PowerShell)
.\venv\Scripts\Activate.ps1
```

3. Run script.

```shell
options:
  - -a, --action: tweets or replies (default: tweets)
  - -s, --screenname: Twitter username to fetch tweets for (tweets action), or exclude from replies (replies action)
  - -i, --tweet-ids: Tweet ID to fetch replies for (required for replies action)
  - -c, --count: Number of tweets or replies to fetch (default: 100)
  - -t, --top: Number of top replies to show (for replies only, default: 5)
  - -f, --filename: Optional custom filename for CSV export

# Get script arguments
python3 src/main.py -h

# Get most viewed tweets for a specific user (top 100 most viewed posts out of 1000 most recent posts).
python3 src/main.py -a tweets -s bigfatsurprise -t 100 -c 1000 -f nina_tweets
python3 src/main.py --action tweets --screenname elonmusk --top 100 --count 1000 --filename musk_tweets

# Get most liked replies for a single tweet (top 5 most liked replies across 100 replies for a single tweet, excluding the original poster).
python3 src/main.py -a replies -s bigfatsurprise -i 1927722797909836090 -t 5 -c 100
python3 src/main.py --action replies -screenname bigfatsurprise --tweet-ids 1927722797909836090 --top 5 --count 100

# Get most like replies for a list of tweets (top 100 most liked replies across 30 replies per tweet, excluding the original poster)
python3 src/main.py -a replies -s bigfatsurprise -i 1927722797909836090 1962224063361020390 1921934899281281115 1978177514854842462 1973534268447154600 1945937731324178775 1945284503330586672 1922780121703801315 1961125436928528695 1938765277086482446 1970215889191493899 1954484867053342815 1947755708986101965 1955637347720323515 1955254718323953746 1965014252366045604 1970944639113781405 1952813803013587449 1932891956675555663 -t 100 -c 30
```

4. Allow the script access to browser cookies. Enter your computer password and click "Always allow".

   <img width="428" height="181" alt="Screenshot 2025-11-02 at 1 58 30 PM" src="https://github.com/user-attachments/assets/4ab7ebed-70d6-43ca-9167-5719a4e5d9c4" />

5. View generated CSV reports in your downloads folder.

### Update Requirements

```shell
make freeze
```

### Formatter

```shell
black .
```
