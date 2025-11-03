import argparse
import asyncio
from cookies import save_cookies_to_json
from client import TwitterClient


async def main(args):
    # Save cookies to cookies.json
    save_cookies_to_json()

    # Create Twitter client
    twitter_client = TwitterClient()
    await twitter_client.test_authenticated_call()

    # Send request to get posts for a user
    if args.action == "tweets":
        await twitter_client.get_tweets(screen_name=args.screenname, count=args.count)
    elif args.action == "replies":
        await twitter_client.get_top_replies(
            tweet_id=args.tweet_id, top=args.top, count=args.count
        )
    else:
        print(f"Unknown action: {args.action}")


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
        required=True,
        help="Twitter handle (without @) of the user to fetch tweets for.",
    )
    parser.add_argument(
        "--tweet-id",
        "-i",
        type=str,
        help="Tweet ID (for fetching replies)",
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

    args = parser.parse_args()
    asyncio.run(main(args))
