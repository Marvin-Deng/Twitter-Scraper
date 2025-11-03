import json
import browser_cookie3
from constants import DOMAIN, COOKIES_FILE


def save_cookies_to_json():
    cj = browser_cookie3.chrome(domain_name=DOMAIN)
    cookies_dict = {}

    allowed_domains = (DOMAIN.lower(), f".{DOMAIN.lower()}")

    for c in cj:
        name = getattr(c, "name", None)
        value = getattr(c, "value", "")
        domain = getattr(c, "domain", "")

        if not name or not value:
            continue

        if domain.lower() not in allowed_domains:
            print(f"Skipping cookie for non-target domain: {name} ({domain})")
            continue

        cookies_dict[name] = value

    with open(COOKIES_FILE, "w") as f:
        json.dump(cookies_dict, f, indent=2)

    print(f"Saved {len(cookies_dict)} cookies to {COOKIES_FILE} for domain {DOMAIN}")
