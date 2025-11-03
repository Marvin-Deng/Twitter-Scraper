import asyncio
from cookies import save_cookies_to_json
from client import TwitterClient


async def main():
    # Save cookies to cookies.json
    save_cookies_to_json()

    # Create Twitter client
    twitter_client = TwitterClient()
    await twitter_client.test_authenticated_call()

    # Send request to get posts for a user
    await twitter_client.get_tweets(screen_name="elonmusk")


if __name__ == "__main__":
    asyncio.run(main())
