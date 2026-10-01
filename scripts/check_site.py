"""Validate the published homepage, local resources, and removal of old pages."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import sys

root = Path(sys.argv[1] if len(sys.argv) > 1 else "_site").resolve()
errors = []

class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.refs = []
        self.ids = set()

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.add(attrs["id"])
        for key in ("href", "src"):
            if attrs.get(key):
                self.refs.append(attrs[key])
        if attrs.get("srcset"):
            self.refs.extend(item.strip().split()[0] for item in attrs["srcset"].split(","))

pages = {}
for file in root.rglob("*.html"):
    parser = Links()
    html = file.read_text()
    parser.feed(html)
    pages[file] = parser
    if "polyfill.io" in html:
        errors.append(f"{file.relative_to(root)}: unsafe polyfill reference")

expected = {root / name for name in ("index.html", "404.html", "team/index.html")}
if set(pages) != expected:
    errors.append("Expected About, Team, and the 404 page in the published site")

for file, parser in pages.items():
    for ref in parser.refs:
        url = urlsplit(ref)
        if url.scheme or url.netloc:
            continue
        target = (root / unquote(url.path).lstrip("/") if url.path.startswith("/")
                  else file.parent / unquote(url.path)) if url.path else file
        if target.is_dir():
            target /= "index.html"
        target = target.resolve()
        if not target.exists():
            errors.append(f"{file.relative_to(root)}: missing {ref}")
        elif url.fragment and target in pages and unquote(url.fragment) not in pages[target].ids:
            errors.append(f"{file.relative_to(root)}: missing anchor {ref}")

for name in ("teaching", "cv", "publications", "projects", "news", "blog", "repositories", "feed.xml"):
    if (root / name).exists():
        errors.append(f"Obsolete published content remains: {name}")
if errors:
    sys.exit("\n".join(errors))
print(f"Checked {len(pages)} HTML pages: local links and removed-page checks passed.")
