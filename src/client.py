from twikit import Client
from requests.cookies import RequestsCookieJar
from constants import USERNAME


class TwitterClient:
    def __init__(self, cookie_jar: RequestsCookieJar):
        self.client = Client("en-US")
        self.__attach_cookiejar(cookie_jar)

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

    def __attach_cookiejar(self, cookiejar: RequestsCookieJar) -> None:
        """
        Attaches a RequestsCookieJar to a session attribute on the twikit Client object.
        """
        candidate_attrs = [
            "session",
            "_session",
            "http",
            "_http",
            "client",
            "_client",
            "requests_session",
            "requests",
            "httpx_client",
        ]
        for attr in candidate_attrs:
            if hasattr(self.client, attr):
                obj = getattr(self.client, attr)

                if hasattr(obj, "cookies"):
                    try:
                        if hasattr(obj.cookies, "update"):
                            obj.cookies.update(cookiejar)
                            print(f"Merged cookiejar into client.{attr}.cookies")
                    except Exception as e:
                        print(
                            f"Failed to assign/merge cookiejar to client.{attr}.cookies: {e}"
                        )
