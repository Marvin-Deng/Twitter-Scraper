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

    async def get_top_tweets(self, screen_name: str, top: int = 5, count: int = 100):
        """
        Gets the most viewed posts created by a specific user.
        """
        all_tweets = await self.__get_tweets(screen_name, count)

        # Sort tweets by views (descending)
        sorted_tweets = sorted(
            all_tweets,
            key=lambda t: int(t.view_count) if t.view_count is not None else 0,
            reverse=True,
        )

        top_tweets = sorted_tweets[:top]
        print(f"\nTop {top} posts by views:")
        await self.__print_tweets(top_tweets)
        return top_tweets

    async def get_top_replies(
        self, tweet_ids: list[str], top: int = 20, count: int = 20
    ):
        """
        Fetch replies for multiple tweets and return the top replies sorted by likes.
        """
        all_replies = []

        for tweet_id in tweet_ids:
            try:
                replies = await self.__get_replies(tweet_id, count)
                if not replies:
                    continue

                # Annotate each reply with the original tweet ID
                for reply in replies:
                    setattr(reply, "original_tweet_id", tweet_id)

                all_replies.extend(replies)

            except Exception as e:
                print(f"Failed to fetch replies for tweet {tweet_id}: {e}")
                break

        if not all_replies:
            print("No replies found across all tweets.")
            return []

        # Sort all replies by likes (descending)
        sorted_replies = sorted(
            all_replies, key=lambda t: t.favorite_count, reverse=True
        )

        top_replies = sorted_replies[:top]
        print(f"\nTop {top} replies by likes across {len(tweet_ids)} tweets:")
        await self.__print_tweets(top_replies)
        return top_replies

    async def __get_tweets(self, screen_name: str, count: int) -> list:
        """
        Fetch at least `count` tweets for a user.
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
            await self.__print_tweets(tweets)

            while len(all_tweets) < count:
                try:
                    tweets = await tweets.next()
                    if not tweets:
                        break
                    all_tweets.extend(tweets)
                    await self.__print_tweets(tweets)
                except Exception as e:
                    print(
                        f"Warning: Error fetching next page of tweets for {screen_name}: {e}"
                    )
                    break

        except Exception as e:
            print(f"Warning: Error getting tweets for @{screen_name}: {e}")

        print(f"Total tweets fetched: {len(all_tweets)}")
        return all_tweets

    async def __get_replies(self, tweet_id: str, count: int):
        """
        Fetch replies for a tweet.
        """
        print(f"\nFetching replies for tweet ID {tweet_id}...")
        all_replies = []

        try:
            tweet = await self.client.get_tweet_by_id(tweet_id)
            if not tweet:
                print(f"Could not find tweet {tweet_id}")
                return []

            replies = tweet.replies or []
            all_replies.extend(replies)
            self.__print_tweets(replies)
            print(f"First page: {len(replies)} replies found!")

            while len(all_replies) < count:
                try:
                    next_page = await tweet.next()
                    if not next_page or not next_page.replies:
                        break
                    new_replies = next_page.replies
                    all_replies.extend(new_replies)
                    self.__print_tweets(new_replies)
                    print(f"Next page: {len(new_replies)} replies found!")
                except Exception as e:
                    print(
                        f"Warning: Error fetching next page of replies for tweet {tweet_id}: {e}"
                    )
                    break

        except Exception as e:
            print(f"Warning: Error getting replies for tweet {tweet_id}: {e}")

        print(f"Total replies fetched: {len(all_replies)}")
        return all_replies

    async def __print_tweets(self, tweets: list[Tweet]):
        for tweet in tweets:
            print(f"ID: {tweet.id}")
            print(f"Text: {tweet.text}")
            print(f"Author: @{tweet.user.screen_name}")
            print(f"Views: {tweet.view_count}")
            print(f"Likes: {tweet.favorite_count}")
            print(f"Retweets: {tweet.retweet_count}")
            print(f"Timestamp: {tweet.created_at}")
            print(f"Reply count: {tweet.reply_count}")
            print("------------------------")
