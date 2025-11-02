import asyncio
from cookies import get_cookiejar_from_browser
from client import TwitterClient


async def main():
    # Get cookies from logged in account
    jar = get_cookiejar_from_browser()

    # Send request via twikit client
    twitter_client = TwitterClient(jar)
    await twitter_client.test_authenticated_call()

    # Send request to get posts for a user
    await twitter_client.get_tweets(screen_name="elonmusk", count=30)


if __name__ == "__main__":
    asyncio.run(main())
