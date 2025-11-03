import argparse
import asyncio
from client import TwitterClient
from cookies import save_cookies_to_json
from export import export_tweets_to_csv


async def main(args):
    # Save cookies to cookies.json
    save_cookies_to_json()

    # Create Twitter client
    twitter_client = TwitterClient()
    await twitter_client.test_authenticated_call()

    tweets = []
    filename_prefix = ""
    action = args.action
    if action == "tweets":
        tweets = await twitter_client.get_top_tweets(
            screen_name=args.screenname, top=args.top, count=args.count
        )
        filename_prefix = action
        tweet_ids = [str(tweet.id) for tweet in tweets]
        print(" ".join(tweet_ids))  # string of top tweet IDs for top reply script
    elif action == "replies":
        tweets = await twitter_client.get_top_replies(
            tweet_ids=args.tweet_ids, top=args.top, count=args.count
        )
        filename_prefix = action
    else:
        print(f"Unknown action: {args.action}")
        return

    if args.filename:
        filename = args.filename
        if not filename.lower().endswith(".csv"):
            filename += ".csv"
    elif args.screenname:
        filename = f"{filename_prefix}_{args.screenname}.csv"
    else:
        filename = f"{filename_prefix}.csv"

    # Export to CSV
    await export_tweets_to_csv(tweets=tweets, filename=filename)
    print(f"Tweets exported to {filename}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Twitter client CLI using Twikit and cookies."
    )
    parser.add_argument(
        "--action",
        "-a",
        choices=["tweets", "replies"],
        default="tweets",
        help="Action to perform",
    )
    parser.add_argument(
        "--screenname",
        "-s",
        help="Twitter handle (without @) of the user to fetch tweets for.",
    )
    parser.add_argument(
        "--tweet-ids",
        "-i",
        nargs="+",
        type=str,
        help="Tweet IDs (for fetching replies)",
    )
    parser.add_argument(
        "--count",
        "-c",
        type=int,
        default=100,
        help="Number of tweets or replies to fetch",
    )
    parser.add_argument(
        "--top",
        "-t",
        type=int,
        default=5,
        help="Number of top replies to show (for replies only)",
    )
    parser.add_argument(
        "--filename",
        "-f",
        type=str,
        help="Custom filename for the exported CSV",
    )

    args = parser.parse_args()
    asyncio.run(main(args))
