from twikit import Client
from constants import USERNAME, COOKIES_FILE


class TwitterClient:
    def __init__(
        self,
    ):
        self.client = Client("en-US")
        self.client.load_cookies(COOKIES_FILE)

    async def test_authenticated_call(self) -> bool:
        if not USERNAME:
            raise ValueError("USERNAME not set in .env file or environment.")

        try:
            user = await self.client.get_user_by_screen_name(USERNAME)
            print(f"Twikit reports: logged in as {user.name} (@{user.screen_name})")
            return True
        except Exception as e:
            print("Auth test failed (Twikit call):", repr(e))
            return False

    async def get_tweets(self, screen_name: str, count=40) -> list:
        """
        Fetches the latest tweets for a specific user by their screen name.
        """
        print(f"\nFetching tweets for @{screen_name}...")
        all_tweets = []

        try:
            user = await self.client.get_user_by_screen_name(screen_name)
            if not user:
                print(f"Could not find user @{screen_name}")
                return []

            tweets = await self.client.get_user_tweets(user.id, tweet_type="Tweets")
            all_tweets.extend(tweets)
            self.print_tweets(tweets)

            # Continue fetching next pages until count is reached
            while len(all_tweets) < count:
                if hasattr(tweets, "next"):
                    try:
                        tweets = await tweets.next()
                        if not tweets:
                            break
                        all_tweets.extend(tweets)
                        self.print_tweets(tweets)
                    except Exception as e:
                        print(f"Error fetching next page: {repr(e)}")
                        break
                else:
                    break

            return all_tweets[:count]

        except Exception as e:
            print(f"Error getting tweets for @{screen_name}: {repr(e)}")
            return []

    def print_tweets(self, tweets):
        for tweet in tweets:
            print(f"ID: {tweet.id}")
            print(f"Text: {tweet.text}")
            print(f"Author: @{tweet.user.screen_name}")
            print(f"Likes: {tweet.favorite_count}")
            print(f"Retweets: {tweet.retweet_count}")
            print(f"Timestamp: {tweet.created_at}")
            print(f"Reply count: {tweet.reply_count}")
            print(f"Replies: {tweet.replies}")
            print("------------------------")
