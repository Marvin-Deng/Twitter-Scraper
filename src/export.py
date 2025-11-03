import os
import csv
from twikit import Tweet

if os.name == "nt":  # Windows
    DOWNLOAD_DIR = os.path.join(os.environ["USERPROFILE"], "Downloads")
else:  # macOS/Linux
    DOWNLOAD_DIR = os.path.join(os.path.expanduser("~"), "Downloads")


async def export_tweets_to_csv(tweets: list[Tweet], filename: str):
    """
    Export a list of Tweet objects to a CSV file in the reports directory.
    """
    if not tweets:
        print("No tweets to export.")
        return

    # Ensure reports directory exists
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)

    # Full path to output file
    filepath = os.path.join(DOWNLOAD_DIR, filename)

    with open(filepath, mode="w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(
            ["ID", "Text", "Author", "Likes", "Retweets", "Timestamp", "Reply count"]
        )

        for tweet in tweets:
            writer.writerow(
                [
                    tweet.id,
                    tweet.text.replace("\n", " "),
                    tweet.user.screen_name,
                    tweet.favorite_count,
                    tweet.retweet_count,
                    tweet.created_at,
                    tweet.reply_count,
                ]
            )

    print(f"Exported {len(tweets)} tweets to {filepath}")
