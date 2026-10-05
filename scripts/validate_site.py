"""Check local HTML resources and optionally compare their HTTP responses."""

import argparse
from html.parser import HTMLParser
from pathlib import Path
import sys
import time
from urllib.error import URLError
from urllib.parse import unquote, urljoin, urlsplit
from urllib.request import urlopen


class Resources(HTMLParser):
    def __init__(self):
        super().__init__()
        self.paths = {"/": "index.html"}

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        value = attrs.get("src") if tag in ("img", "script") else None
        if tag == "link" and set(attrs.get("rel", "").split()) & {"stylesheet", "icon"}:
            value = attrs.get("href")
        if not value:
            return
        parts = urlsplit(value)
        if parts.scheme or parts.netloc or not parts.path:
            return
        path = urlsplit(urljoin("http://site.invalid/", value)).path
        self.paths[path] = unquote(path).lstrip("/")


def check_http(base_url, resources):
    deadline = time.monotonic() + 30
    while True:
        try:
            with urlopen(base_url + "/", timeout=5) as response:
                if response.status != 200:
                    raise ValueError(f"Unexpected HTTP status: {response.status}")
            break
        except (URLError, OSError):
            if time.monotonic() >= deadline:
                raise ValueError("Server did not become available within 30 seconds")
            time.sleep(1)

    for path, local_file in resources.items():
        with urlopen(base_url + path, timeout=5) as response:
            if response.status != 200:
                raise ValueError(f"Unexpected HTTP status for {path}: {response.status}")
            if response.read() != local_file.read_bytes():
                raise ValueError(f"HTTP content differs from local file: {path}")
    print(f"PASS: HTTP 200 and matching content for {len(resources)} resources")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site-dir", type=Path, default=Path(__file__).resolve().parents[1] / "website")
    parser.add_argument("--base-url", help="HTTP server origin, for example http://127.0.0.1")
    args = parser.parse_args()
    try:
        root = args.site_dir.resolve()
        html = Resources()
        html.feed((root / "index.html").read_text(encoding="utf-8"))
        resources = {}
        for url_path, relative_path in html.paths.items():
            local_file = (root / relative_path).resolve()
            if not local_file.is_relative_to(root) or not local_file.is_file():
                raise ValueError(f"Missing or invalid local resource: {url_path}")
            resources[url_path] = local_file
        print(f"PASS: {len(resources)} local resources exist")
        if args.base_url:
            base_url = args.base_url.rstrip("/")
            parts = urlsplit(base_url)
            if parts.scheme not in ("http", "https") or not parts.netloc or parts.path or parts.query or parts.fragment:
                raise ValueError("--base-url must be an HTTP(S) origin without a path, query, or fragment")
            check_http(base_url, resources)
    except (OSError, ValueError, URLError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
