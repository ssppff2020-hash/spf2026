#!/usr/bin/env python3
"""C1 pipeline · step 5 — automated QA over the finished translations.

Runs five checks and writes pipeline/qa_report.md:

  1. coverage        every manifest item has a translation at its declared path
  2. banned terms    a blacklist of renderings we explicitly ruled out
  3. structure       *substantive* heading count vs. source (see note below)
  4. length floor    Chinese chars vs. source word count, catches abridging
  5. new terms       collects <!-- NEW-TERM: ... --> for glossary backfill

Design note on check 3: a naive heading count is misleading on scraped pages,
because site navigation ("Related posts", "Company", "Why Stytch") is marked up
with the same <h2>/<h3> tags as real sections. Counting those made three
*correct* translations look like they had dropped 60-100% of their headings.
So we only count a source heading as real if it is followed by a run of prose —
nav items are followed by another heading, not by a paragraph.

Every check is a *signal*, not a verdict: the report is meant to point a human at
the 10% worth reading, not to auto-pass. Course-agnostic — point it at any
manifest + translation tree of the same shape.

Usage:  python 05_qa.py [--root <challenge_dir>] [--manifest <path>]
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from pathlib import Path

# Chinese chars per English word below which we suspect dropped content.
# Real translations on this corpus land near 1.5-2.0; 0.75 is a tripwire.
CN_PER_WORD = 0.75

# Renderings ruled out in the glossary, each with the canonical form we use.
BANNED = {
    "大型语言模型": "大语言模型",
    "代码审查": "代码评审",
    "代码回顾": "代码评审",
    "可复现": "可复跑",
    "提示词工程": "提示工程",
    "上下文腐烂": "上下文腐化",
    "上下文衰减": "上下文腐化",
    "沙盒": "沙箱",
    "氛围编程": "vibe coding",
    "AI 代理": "AI 智能体",
    "智能代理": "智能体",
    "代理体": "智能体",
}

HEADER_FIELD = re.compile(r"^\s*>\s*\*\*(?P<k>[^*]+)\*\*[：:]\s*(?P<v>.*?)\s*$")
NEW_TERM = re.compile(r"<!--\s*NEW-TERM:\s*(?P<body>.*?)-->")
CN = re.compile(r"[一-鿿]")
HEADING_LINE = re.compile(r"^#{2,6}\s+\S")
PROSE_MIN = 150          # chars of body text for a heading to count as "real"


def cn_len(s: str) -> int:
    return len(CN.findall(s))


def parse_header(text: str) -> dict:
    out = {}
    for line in text.splitlines()[:30]:
        m = HEADER_FIELD.match(line)
        if m:
            out[m.group("k").strip()] = m.group("v").strip()
    return out


def zh_headings(text: str) -> int:
    return sum(1 for line in text.splitlines() if HEADING_LINE.match(line))


def substantive_headings(text: str) -> int:
    """Source headings that are followed by real prose (not nav items)."""
    lines = text.splitlines()
    idx = [i for i, ln in enumerate(lines) if HEADING_LINE.match(ln)]
    n = 0
    for k, i in enumerate(idx):
        end = idx[k + 1] if k + 1 < len(idx) else len(lines)
        body = "".join(lines[i + 1:end]).strip()
        if len(body) >= PROSE_MIN:
            n += 1
    return n


def load_glossary(path: Path):
    if not path.exists():
        return []
    with path.open(encoding="utf-8") as fh:
        return [r for r in csv.DictReader(fh) if r.get("zh")]


def main() -> int:
    # Windows consoles default to GBK; the report is written as UTF-8 either way,
    # but the console summary would crash on characters like ⚠.
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, OSError):
        pass

    ap = argparse.ArgumentParser()
    here = Path(__file__).resolve().parent
    ap.add_argument("--root", default=str(here.parent.parent))
    ap.add_argument("--manifest",
                    default=str(here.parent.parent / "materials/_work/source/manifest.json"))
    args = ap.parse_args()

    root = Path(args.root)
    trans_dir = root / "C1/翻译"
    glossary = load_glossary(root / "C1/glossary.csv")
    mpath = Path(args.manifest)
    items = json.loads(mpath.read_text(encoding="utf-8"))["items"] if mpath.exists() else []
    want = [i for i in items if i["status"] == "ok"]

    files = sorted(p for p in trans_dir.rglob("*.md") if not p.name.startswith(("_", ".")))

    missing, rows, banned_hits, struct_flagged, new_terms = [], [], [], [], []

    for it in want:
        p = trans_dir / it["output"] if it.get("output") else None
        if p is None or not p.exists():
            missing.append(it)
            continue
        body = p.read_text(encoding="utf-8", errors="replace")
        src = mpath.parent / f"{it['slug']}.txt"
        src_text = src.read_text(encoding="utf-8", errors="replace") if src.exists() else ""

        got, need = cn_len(body), int(it["words"] * CN_PER_WORD)
        sh, th = substantive_headings(src_text), zh_headings(body)

        for bad, good in BANNED.items():
            c = body.count(bad)
            if c:
                banned_hits.append((p.name, bad, good, c))

        new_terms += [(p.name, m.group("body").strip()) for m in NEW_TERM.finditer(body)]

        ratio = th / sh if sh else 1.0
        if sh >= 3 and ratio < 0.7:
            struct_flagged.append((p.name, sh, th, ratio))

        rows.append({"file": str(p.relative_to(root)).replace("\\", "/"),
                     "cn": got, "need": need, "words": it["words"],
                     "sh": sh, "th": th, "title": it["zh_title"]})

    covered, cov = len(rows), (len(rows) / len(want) * 100 if want else 0.0)
    short = [r for r in rows if r["cn"] < r["need"]]

    seen, uniq_terms = set(), []
    for f, b in new_terms:
        key = b.split("|")[0].strip().lower()
        if key in seen:
            continue
        seen.add(key)
        uniq_terms.append((f, b))

    L = []
    A = L.append
    A("# C1 翻译质量抽检报告（自动生成）")
    A("")
    A(f"> 生成脚本：`pipeline/05_qa.py`　｜　扫描目录：`C1/翻译/`　｜　译稿数：**{len(files)}**")
    A("")
    A("本报告只做**信号提示**，不自动判合格；`⚠` 项需人工确认。")
    A("")
    A("## 1. 覆盖度")
    A("")
    A(f"- 清单中可译条目：**{len(want)}** 篇")
    A(f"- 已产出译稿：**{covered}** 篇")
    A(f"- **覆盖率：{cov:.1f}%**（验收要求 ≥ 80%）")
    A("")
    if missing:
        A("未产出译稿的条目：")
        A("")
        for m in missing:
            A(f"- `{m['slug']}` — {m['zh_title']}（应在 `翻译/{m.get('output','')}`）")
    else:
        A("✅ 清单内所有可译条目均已产出译稿。")
    A("")

    A("## 2. 禁用译法扫描")
    A("")
    if banned_hits:
        A("| 文件 | 命中 | 应为 | 次数 |")
        A("|---|---|---|---|")
        for f, bad, good, c in banned_hits:
            A(f"| {f} | {bad} | {good} | {c} |")
    else:
        A("✅ 未命中任何禁用译法（术语一致性检查通过）。")
    A("")

    A("## 3. 结构完整性（实质小节数比对）")
    A("")
    A("> 只统计**后面跟着正文**的小节标题；站点导航标题（Related posts / Company 等）已排除，")
    A("> 否则会误判成漏译。详见脚本顶部说明。")
    A("")
    if struct_flagged:
        A("| 文件 | 原文实质小节 | 译文小节 | 比例 |")
        A("|---|---|---|---|")
        for f, sh, th, r in struct_flagged:
            A(f"| {f} | {sh} | {th} | {r:.2f} ⚠ |")
    else:
        A("✅ 所有译稿的小节数均 ≥ 原文实质小节的 70%。")
    A("")

    A("## 4. 篇幅抽查")
    A("")
    A(f"下限 = 原文词数 × {CN_PER_WORD}（低于此值疑似漏译）。")
    A("")
    if short:
        A("| 文件 | 中文字符 | 下限 |")
        A("|---|---|---|")
        for r in short:
            A(f"| {r['file']} | {r['cn']:,} | {r['need']:,} ⚠ |")
    else:
        A(f"✅ 全部 {len(rows)} 篇译稿篇幅均在阈值之上（漏译风险低）。")
    A("")

    A("## 5. 术语表待回填")
    A("")
    if uniq_terms:
        A(f"译者在正文里标记了 **{len(uniq_terms)}** 个 glossary 未覆盖的新词（已去重）：")
        A("")
        A("| 出现在 | NEW-TERM |")
        A("|---|---|")
        for f, b in uniq_terms:
            A(f"| {f} | `{b}` |")
    else:
        A("✅ 无新增术语待回填。")
    A("")

    A("## 6. 逐篇明细")
    A("")
    A("| 译稿 | 中文字符 | 原文词数 | 原文实质小节 | 译文小节 |")
    A("|---|---|---|---|---|")
    for r in rows:
        A(f"| {r['file']} | {r['cn']:,} | {r['words']:,} | {r['sh']} | {r['th']} |")
    A("")

    out = root / "C1/pipeline/qa_report.md"
    out.write_text("\n".join(L), encoding="utf-8")

    print(f"coverage      : {cov:.1f}%  ({covered}/{len(want)})")
    print(f"banned hits   : {len(banned_hits)}")
    print(f"structure ⚠   : {len(struct_flagged)}")
    print(f"short ⚠       : {len(short)}")
    print(f"new terms     : {len(uniq_terms)} unique")
    print(f"report        : {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
