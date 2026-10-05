#!/usr/bin/env python3
"""C1 pipeline · step 2b — PDF -> clean plain text, with an engine sanity check.

Why this is a separate step from 02_extract.py:

    On this corpus, `pdftotext` (poppler) silently corrupted one of the three
    PDFs — it emitted every glyph twice, so "How Anthropic teams" came out as
    "HHooww AAnntthhrrooppicic tteeaammss". The file still looked like plausible
    text, page counts matched, and nothing errored. It would have gone straight
    into translation unnoticed.

    PyMuPDF read the same file cleanly (and recovered ~33% more text, because
    poppler was also dropping content, not just duplicating it).

    So: try two engines, sanity-check both, keep the better one. The check is
    cheap and the failure mode it catches is invisible.

Usage:  python 02b_extract_pdf.py <pdf_dir> <out_dir>
"""
from __future__ import annotations

import pathlib
import re
import subprocess
import sys

# A "doubled" word is one where the odd-index chars equal the even-index chars,
# e.g. HHooww -> "Hw" twice. Real prose essentially never scores above ~2%.
DOUBLE_ALARM = 0.10


def doubled_rate(text: str) -> float:
    words = re.findall(r"[A-Za-z]{4,}", text)
    if not words:
        return 0.0
    n = sum(1 for w in words
            if w[0::2].lower() == w[1::2].lower() and len(set(w[1::2])) > 1)
    return n / len(words)


def via_pymupdf(pdf: pathlib.Path) -> str:
    try:
        import pymupdf
    except ImportError:
        return ""
    doc = pymupdf.open(pdf)
    return "\n".join(page.get_text("text") for page in doc)


def via_poppler(pdf: pathlib.Path) -> str:
    try:
        out = subprocess.run(["pdftotext", "-enc", "UTF-8", str(pdf), "-"],
                             capture_output=True, timeout=120)
        return out.stdout.decode("utf-8", errors="replace")
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return ""


def tidy(text: str) -> str:
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def main() -> int:
    src = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".")
    out = pathlib.Path(sys.argv[2] if len(sys.argv) > 2 else "extracted_pdf")
    out.mkdir(parents=True, exist_ok=True)

    for pdf in sorted(src.rglob("*.pdf")):
        cands = {"pymupdf": tidy(via_pymupdf(pdf)),
                 "poppler": tidy(via_poppler(pdf))}
        cands = {k: v for k, v in cands.items() if v}

        scored = {k: (doubled_rate(v), len(v)) for k, v in cands.items()}
        # Prefer an engine that passes the sanity check; among those, the longest.
        clean = {k: v for k, v in scored.items() if v[0] < DOUBLE_ALARM}
        if clean:
            pick = max(clean, key=lambda k: clean[k][1])
        else:
            pick = min(scored, key=lambda k: scored[k][0])   # least corrupted

        text = cands[pick]
        dest = out / f"{pdf.stem}.txt"
        dest.write_text(text, encoding="utf-8")

        flags = "  ".join(f"{k}:{v[0]:.1%}/{v[1]:,}c" for k, v in sorted(scored.items()))
        mark = "ok  " if scored[pick][0] < DOUBLE_ALARM else "WARN"
        print(f"{mark} {pdf.stem:42s} picked={pick:8s} {scored[pick][1]:>7,}c  ({flags})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
