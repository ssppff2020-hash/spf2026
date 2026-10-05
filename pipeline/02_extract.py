#!/usr/bin/env python3
"""Step 1 of the C1 pipeline: HTML/PDF -> clean plain text.

Reusable across courses: point SRC at any directory of downloaded
.html/.pdf materials and it emits a text/ mirror with a manifest.
"""
import json
import os
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

SRC = Path(sys.argv[1] if len(sys.argv) > 1 else "CS146S_offline")
OUT = Path(sys.argv[2] if len(sys.argv) > 2 else "extracted")

DROP_TAGS = {"script", "style", "noscript", "svg", "nav", "footer", "header",
             "form", "iframe", "template", "button", "aside", "menu", "dialog"}
BLOCK_TAGS = {"p", "div", "section", "article", "li", "tr", "h1", "h2", "h3",
              "h4", "h5", "h6", "blockquote", "pre", "br", "figcaption", "td"}


class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []
        self.skip_depth = 0
        self.heading = None

    def handle_starttag(self, tag, attrs):
        if tag in DROP_TAGS:
            self.skip_depth += 1
            return
        if self.skip_depth:
            return
        m = re.fullmatch(r"h([1-6])", tag)
        if m:
            self.heading = int(m.group(1))
        elif tag in BLOCK_TAGS:
            self.parts.append("\n")

    def handle_endtag(self, tag):
        if tag in DROP_TAGS and self.skip_depth:
            self.skip_depth -= 1
        elif self.skip_depth == 0 and tag in BLOCK_TAGS:
            self.parts.append("\n")

    def handle_data(self, data):
        if self.skip_depth:
            return
        text = data.strip()
        if not text:
            return
        if self.heading:
            self.parts.append("\n" + "#" * self.heading + " " + text + "\n")
            self.heading = None
        else:
            self.parts.append(text + " ")

    def text(self):
        raw = "".join(self.parts)
        raw = re.sub(r"[ \t]+", " ", raw)
        raw = re.sub(r"\n\s*\n\s*\n+", "\n\n", raw)
        return raw.strip()


def decode_html(raw):
    """Decode bytes to str, honouring <meta charset> when present."""
    head = raw[:4096].decode("ascii", errors="ignore").lower()
    meta = re.search(r'charset=["\']?([\w-]+)', head)
    cands = []
    if meta:
        cands.append(meta.group(1))
    cands += ["utf-8", "cp1252", "latin-1"]
    best, best_bad = None, None
    for enc in dict.fromkeys(cands):
        try:
            text = raw.decode(enc)
        except (UnicodeDecodeError, LookupError):
            continue
        bad = text.count("�")
        if bad == 0:
            return text
        if best_bad is None or bad < best_bad:
            best, best_bad = text, bad
    if best is not None:
        return best
    return raw.decode("utf-8", errors="replace")


def content_root(html):
    """Narrow to the main content container when the page declares one.

    Kills site chrome (docs sidebars, mega-menus) that would otherwise be
    translated as if it were part of the article. Falls back to the whole
    document when no <main>/<article> wrapper exists.
    """
    cands = []
    for tag in ("main", "article"):
        cands += [m.group(0) for m in re.finditer(rf"(?is)<{tag}[\s>].*?</{tag}>", html)]
    cands = [c for c in cands if len(c) > 1500]
    return max(cands, key=len) if cands else html


def html_to_text(path):
    html = decode_html(Path(path).read_bytes())
    p = TextExtractor()
    p.feed(html)
    full = p.text()
    root = content_root(html)
    if root is html:
        return full
    p2 = TextExtractor()
    p2.feed(root)
    narrowed = p2.text()
    # Only trust the narrowed container if it kept most of the text; a tiny
    # match means we grabbed a sidebar card, not the article.
    if len(narrowed) >= 1500 and len(narrowed) >= 0.6 * len(full):
        return narrowed
    return full


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    manifest = []
    for path in sorted(SRC.rglob("*")):
        if not path.is_file():
            continue
        rel = path.relative_to(SRC)
        suffix = path.suffix.lower()
        if suffix == ".html":
            text = html_to_text(path)
        elif suffix == ".txt":
            text = path.read_text(encoding="utf-8", errors="ignore")
        else:
            continue
        if len(text) < 200:
            status = "placeholder"
        else:
            status = "ok"
        dest = OUT / rel.with_suffix(".txt")
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(text, encoding="utf-8")
        manifest.append({"source": str(rel).replace("\\", "/"),
                         "text": str(dest.relative_to(OUT)).replace("\\", "/"),
                         "chars": len(text), "words": len(text.split()),
                         "status": status})
    (OUT / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    ok = [m for m in manifest if m["status"] == "ok"]
    print(f"files={len(manifest)} ok={len(ok)} "
          f"chars={sum(m['chars'] for m in ok):,} "
          f"words={sum(m['words'] for m in ok):,}")
    for m in sorted(ok, key=lambda x: -x["chars"])[:10]:
        print(f"  {m['chars']:>8,}  {m['source']}")


if __name__ == "__main__":
    main()
