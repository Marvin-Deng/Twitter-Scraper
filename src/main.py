import asyncio
from cookies import get_cookiejar_from_browser
from client import TwitterClient


async def main():
    # Get cookies from logged in account
    jar = get_cookiejar_from_browser()

    # Send request via twikit client
    twitter_client = TwitterClient(jar)
    await twitter_client.test_authenticated_call()


if __name__ == "__main__":
    asyncio.run(main())
