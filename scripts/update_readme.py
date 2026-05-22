#!/usr/bin/env python3
"""Regenerate README.md report index from data/reports-index.json."""
from __future__ import annotations

import datetime as dt
import json
from collections import defaultdict
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
INDEX = ROOT / "data" / "reports-index.json"
START = "<!-- REPORT_INDEX_START -->"
END = "<!-- REPORT_INDEX_END -->"


def load_reports() -> list[dict]:
    if not INDEX.exists():
        return []
    data = json.loads(INDEX.read_text(encoding="utf-8"))
    return data.get("reports", [])


def campaign_for(month: str) -> str:
    return "monthly_" + month.replace("-", "_")


def build_index(reports: list[dict]) -> str:
    if not reports:
        return "暂无报告。"
    by_month: dict[str, list[dict]] = defaultdict(list)
    for r in reports:
        by_month[r.get("month", "unknown")].append(r)

    lines: list[str] = []
    latest_month = sorted(by_month.keys(), reverse=True)[0]
    latest = sorted(by_month[latest_month], key=lambda r: (float(r.get("score") or 0), r.get("airport", "")), reverse=True)

    lines.append(f"### 最新报告月份：{latest_month}")
    lines.append("")
    lines.append(f"[查看 GateRank 实时全量排行榜](https://gate-rank.com/rankings/all?utm_source=github&utm_medium=readme&utm_campaign={campaign_for(latest_month)})")
    lines.append("")
    lines.append("#### 最新月度报告列表")
    lines.append("")
    for r in latest:
        score = f"，评分 {r['score']}" if r.get("score") else ""
        status = f"，状态：{r['status']}" if r.get("status") else ""
        lines.append(f"- [{r.get('airport', r.get('slug'))}机场测试报告]({r['path']}){score}{status} ｜ [GateRank 动态报告]({r['gate_rank_url']}?utm_source=github&utm_medium=readme&utm_campaign={quote(r.get('slug','report'))})")

    lines.append("")
    lines.append("### 历史月度归档")
    lines.append("")
    for month in sorted(by_month.keys(), reverse=True):
        items = sorted(by_month[month], key=lambda r: r.get("airport", ""))
        lines.append(f"#### {month}")
        lines.append("")
        for r in items:
            extra = []
            if r.get("score"):
                extra.append(f"评分 {r['score']}")
            if r.get("price"):
                extra.append(f"价格 {r['price']}")
            suffix = "（" + "，".join(extra) + "）" if extra else ""
            lines.append(f"- [{r.get('airport', r.get('slug'))}]({r['path']}){suffix}")
        lines.append("")

    lines.append("### 按机场索引")
    lines.append("")
    by_airport: dict[str, list[dict]] = defaultdict(list)
    for r in reports:
        by_airport[r.get("airport", r.get("slug", "unknown"))].append(r)
    for airport in sorted(by_airport.keys()):
        items = sorted(by_airport[airport], key=lambda r: r.get("month", ""), reverse=True)
        links = "、".join(f"[{r.get('month')}]({r['path']})" for r in items)
        lines.append(f"- **{airport}**：{links}")

    lines.append("")
    lines.append(f"_README 索引更新时间：{dt.datetime.now(dt.timezone(dt.timedelta(hours=8))).strftime('%Y-%m-%d %H:%M:%S %z')}_")
    return "\n".join(lines).strip()


def main() -> None:
    text = README.read_text(encoding="utf-8") if README.exists() else "# GateRank 机场测评报告库\n\n" + START + "\n" + END + "\n"
    if START not in text or END not in text:
        text += f"\n\n## 报告目录\n\n{START}\n{END}\n"
    before, rest = text.split(START, 1)
    _, after = rest.split(END, 1)
    new_text = before + START + "\n" + build_index(load_reports()) + "\n" + END + after
    README.write_text(new_text, encoding="utf-8")
    print("README.md updated")


if __name__ == "__main__":
    main()
