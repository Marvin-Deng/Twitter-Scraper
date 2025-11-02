import browser_cookie3
from requests.cookies import RequestsCookieJar
from constants import DOMAIN


def get_cookiejar_from_browser() -> RequestsCookieJar:
    """
    Fetch cookies from the browser and return a RequestsCookieJar.
    """
    cj = browser_cookie3.chrome(domain_name=DOMAIN)
    jar = RequestsCookieJar()
    seen = {}  # key: (name, domain, path) -> cookie

    allowed_domains = (DOMAIN.lower(), f".{DOMAIN.lower()}")

    for c in cj:
        name = getattr(c, "name", None)
        value = getattr(c, "value", "")
        domain = getattr(c, "domain", "")
        path = getattr(c, "path", "/")
        secure = bool(getattr(c, "secure", False))
        expires = getattr(c, "expires", None)

        if not name:
            continue

        if domain.lower() not in allowed_domains:
            print(f"Skipping cookie for non-target domain: {name} ({domain})")
            continue

        key = (name, domain, path)
        seen[key] = (name, value, domain, path, secure, expires)

    for name, value, domain, path, secure, expires in seen.values():
        jar.set(name, value, domain=domain, path=path, secure=secure, expires=expires)

    print(f"Loaded {len(jar)} cookies from browser for domain {DOMAIN}")
    return jar
