import os
import csv
from twikit import Tweet

if os.name == "nt":  # Windows
    DOWNLOAD_DIR = os.path.join(os.environ["USERPROFILE"], "Downloads")
else:  # macOS/Linux
    DOWNLOAD_DIR = os.path.join(os.path.expanduser("~"), "Downloads")


async def export_tweets_to_csv(tweets: list[Tweet], filename: str):
    """
    Export a list of Tweet objects to a CSV file in the Downloads directory.
    Adds an 'original_tweet_id' column for replies.
    """
    if not tweets:
        print("No tweets to export.")
        return

    # Ensure download directory exists
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)

    # Full path to output file
    filepath = os.path.join(DOWNLOAD_DIR, filename)

    # Build header row in lowercase snake_case
    headers = [
        "id",
        "author",
        "timestamp",
        "text",
        "views",
        "likes",
        "retweets",
        "reply_count",
        "original_tweet_id",
    ]

    with open(filepath, mode="w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)

        for tweet in tweets:
            row = [
                tweet.id,
                tweet.user.screen_name,
                tweet.created_at,
                tweet.text.replace("\n", " "),
                tweet.view_count,
                tweet.favorite_count,
                tweet.retweet_count,
                tweet.reply_count,
                getattr(tweet, "original_tweet_id", None),
            ]

            writer.writerow(row)

    print(f"Exported {len(tweets)} tweets to {filepath}")
