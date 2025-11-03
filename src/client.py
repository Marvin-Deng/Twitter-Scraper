from twikit import Client, Tweet
from constants import USERNAME, COOKIES_FILE


class TwitterClient:
    def __init__(self):
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
            raise RuntimeError("Auth test failed (Twikit call).") from e

    async def get_tweets(self, screen_name: str, count=10) -> list:
        """
        Fetches at least `count` number of tweets for a specific user by their screen name. Rate limit is 50 requests every 15 min.
        """
        print(f"\nFetching tweets for @{screen_name}...")
        all_tweets = []

        try:
            user = await self.client.get_user_by_screen_name(screen_name)
            if not user:
                raise ValueError(f"Could not find user @{screen_name}")

            tweets = await self.client.get_user_tweets(user.id, tweet_type="Tweets")
            all_tweets.extend(tweets)
            await self.__print_tweets(tweets)

            # Continue fetching next pages until count is reached
            while len(all_tweets) < count:
                try:
                    tweets = await tweets.next()
                    if not tweets:
                        break
                    all_tweets.extend(tweets)
                    await self.__print_tweets(tweets)
                except Exception as e:
                    print(f"Error fetching next page of tweets for {screen_name}.")
                    break

            print(f"Total replies fetched: {len(all_tweets)}")
            return all_tweets

        except Exception as e:
            raise RuntimeError(f"Error getting tweets for @{screen_name}.") from e

    async def get_top_replies(self, tweet_id: str, top: int = 5, count: int = 100):
        """
        Fetch replies for a tweet and return the top ones ranked by likes. Rate limit is 150 requests every 15 min.
        """
        all_replies = await self.__get_replies(tweet_id, count)
        if not all_replies:
            print("No replies found.")
            return []

        # Sort by likes descending
        sorted_replies = sorted(
            all_replies, key=lambda t: t.favorite_count, reverse=True
        )

        top_replies = sorted_replies[:top]
        print(f"\nTop {top} replies by likes:")
        await self.__print_tweets(top_replies)
        return top_replies

    async def __get_replies(self, tweet_id: str, count: int):
        """
        Fetch at least `count` number of replies for a given tweet.
        """
        print(f"\nFetching replies for tweet ID {tweet_id}...")
        all_replies = []

        try:
            tweet_obj = await self.client.get_tweet_by_id(tweet_id)
            if not tweet_obj:
                raise ValueError(f"Could not find tweet with ID {tweet_id}")

            replies = tweet_obj.replies
            if not replies:
                raise ValueError("No replies found.")

            all_replies.extend(replies)
            self.print_tweets(replies)
            print(f"First page: {len(replies)} replies found!")

            # Continue fetching additional reply pages until we reach the count
            while len(all_replies) < count:
                try:
                    next_page = await tweet_obj.next()
                    if not next_page or not next_page.replies:
                        break

                    new_replies = next_page.replies
                    all_replies.extend(new_replies)
                    self.print_tweets(new_replies)
                    print(f"Next page: {len(new_replies)} replies found!")
                except Exception as e:
                    print(f"Error fetching next page of replies for tweet {tweet_id}.")
                    break

            print(f"Total replies fetched: {len(all_replies)}")
            return all_replies

        except Exception as e:
            raise RuntimeError(f"Error getting replies for tweet {tweet_id}.") from e

    async def __print_tweets(self, tweets: list[Tweet]):
        for tweet in tweets:
            print(f"ID: {tweet.id}")
            print(f"Text: {tweet.text}")
            print(f"Author: @{tweet.user.screen_name}")
            print(f"Likes: {tweet.favorite_count}")
            print(f"Retweets: {tweet.retweet_count}")
            print(f"Timestamp: {tweet.created_at}")
            print(f"Reply count: {tweet.reply_count}")
            print("------------------------")
