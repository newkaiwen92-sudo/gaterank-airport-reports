#!/usr/bin/env python3
"""Import raw GateRank airport report Markdown files into reports/YYYY-MM/<slug>.md.

No external dependencies. The parser is deliberately tolerant: it extracts common
fields from headings/bullets when present and preserves the original report body.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import re
import shutil
import unicodedata
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
INDEX_PATH = ROOT / "data" / "reports-index.json"


def slugify(text: str) -> str:
    text = unicodedata.normalize("NFKC", text).strip().lower()
    replacements = {
        "大象网络": "elphantroute",
        "隐云": "x-wkacc",
        "光速云": "qwerty-gsyaff",
        "百变小樱": "bbxy",
        "酷可云": "kukeyun",
        "电影云": "user-moviecloud",
        "飞猫云": "flycat-flycatvipaff",
        "瞬云": "ccc-jichang",
    }
    if text in replacements:
        return replacements[text]
    asciiish = re.sub(r"[^a-z0-9]+", "-", text).strip("-")
    if asciiish:
        return asciiish[:80]
    digest = hashlib.sha1(text.encode("utf-8")).hexdigest()[:10]
    return "airport-" + digest


def first_match(patterns: list[str], text: str, default: str = "") -> str:
    for pat in patterns:
        m = re.search(pat, text, flags=re.I | re.M)
        if m:
            return m.group(1).strip()
    return default


def detect_title(text: str, fallback: str) -> str:
    m = re.search(r"^#\s+(.+)$", text, flags=re.M)
    return m.group(1).strip() if m else fallback


def detect_airport_name(text: str, source_name: str) -> str:
    name = first_match([
        r"机场名称[：:]\s*([^\n|]+)",
        r"名称[：:]\s*([^\n|]+)",
        r"^#\s*([^#\n]+?)(?:机场)?(?:测试|测评|报告|事实卡|\s|：|:)",
    ], text)
    if name:
        return re.sub(r"\s*(机场)?(测试报告|测评报告|事实卡|报告).*$", "", name).strip(" ：:") or name
    return Path(source_name).stem.replace("测试报告", "").replace("测评报告", "").strip() or "unknown-airport"


def detect_month(text: str, path: Path) -> str:
    raw = first_match([
        r"报告月份[：:]\s*(\d{4}[-年/]\d{1,2})",
        r"数据日期[：:]\s*(\d{4}-\d{1,2}-\d{1,2})",
        r"报告日期[：:]\s*(\d{4}-\d{1,2}-\d{1,2})",
        r"(20\d{2})\s*年\s*(\d{1,2})\s*月",
        r"(20\d{2}-\d{1,2})",
    ], text)
    if raw:
        nums = re.findall(r"\d+", raw)
        if len(nums) >= 2:
            return f"{int(nums[0]):04d}-{int(nums[1]):02d}"
    m = re.search(r"(20\d{2})[-_/年](\d{1,2})", path.name)
    if m:
        return f"{int(m.group(1)):04d}-{int(m.group(2)):02d}"
    return dt.date.today().strftime("%Y-%m")


def extract_fields(text: str) -> dict:
    return {
        "score": first_match([r"(?:GateRank\s*)?(?:公开)?评分[：:]\s*([0-9.]+)", r"最终分[：:]\s*([0-9.]+)", r"综合评分[：:]\s*([0-9.]+)"], text),
        "status": first_match([r"当前状态[：:]\s*([^\n]+)", r"状态[：:]\s*([^\n]+)"], text),
        "price": first_match([r"月付价格[：:]\s*([^\n]+)", r"月付[：:]\s*([^\n]+)", r"价格[：:]\s*([^\n]+)"], text),
        "availability": first_match([r"30\s*天可用率[：:]\s*([^\n]+)", r"可用率[：:]\s*([^\n]+)"], text),
        "latency": first_match([r"中位延迟[：:]\s*([^\n]+)", r"延迟[：:]\s*([^\n]+)"], text),
        "speed": first_match([r"下载速率[：:]\s*([^\n]+)", r"速度[：:]\s*([^\n]+)"], text),
        "risk": first_match([r"风险(?:提示|摘要|标签)?[：:]\s*([^\n]+)", r"风险惩罚[：:]\s*([^\n]+)"], text),
    }


def gate_rank_links(slug: str, campaign: str) -> str:
    encoded_campaign = quote(campaign)
    return f"""
## 查看最新动态数据

- [查看该机场 GateRank 最新动态报告](https://gate-rank.com/airports/{slug}?utm_source=github&utm_medium=report_md&utm_campaign={encoded_campaign})
- [查看 GateRank 全量机场排行榜](https://gate-rank.com/rankings/all?utm_source=github&utm_medium=report_md&utm_campaign={encoded_campaign})
- [查看 GateRank 跑路风险监测](https://gate-rank.com/risk-monitor?utm_source=github&utm_medium=report_md&utm_campaign={encoded_campaign})
""".strip()


def normalize_report(source: Path) -> tuple[Path, dict]:
    text = source.read_text(encoding="utf-8")
    name = detect_airport_name(text, source.name)
    month = detect_month(text, source)
    slug = first_match([r"slug[：:]\s*([a-z0-9][a-z0-9_-]+)", r"/airports/([a-z0-9][a-z0-9_-]+)"], text.lower()) or slugify(name)
    title = detect_title(text, f"{name}机场测试报告：{month} 月度归档")
    fields = extract_fields(text)
    campaign = f"{slug}_{month.replace('-', '_')}"
    rel_path = Path("reports") / month / f"{slug}.md"
    dest = ROOT / rel_path
    dest.parent.mkdir(parents=True, exist_ok=True)

    summary_lines = [
        f"# {title}",
        "",
        "> 本文为 GateRank 机场测试报告 GitHub 月度归档。实时评分、官网状态、风险标签和榜单排名可能变化，请以 GateRank 主站为准。",
        "",
        "## 报告信息",
        "",
        f"- 机场名称：{name}",
        f"- 报告月份：{month}",
        f"- GateRank 动态报告：https://gate-rank.com/airports/{slug}?utm_source=github&utm_medium=report_md&utm_campaign={campaign}",
    ]
    for label, key in [("评分", "score"), ("状态", "status"), ("月付价格", "price"), ("30 天可用率", "availability"), ("中位延迟", "latency"), ("下载速率", "speed"), ("风险信息", "risk")]:
        if fields.get(key):
            summary_lines.append(f"- {label}：{fields[key]}")
    summary = "\n".join(summary_lines)

    # Avoid duplicate first H1 from original body because we add a normalized H1.
    body = re.sub(r"^#\s+.+\n+", "", text, count=1, flags=re.M).strip()
    content = f"{summary}\n\n## 原始测试报告\n\n{body}\n\n{gate_rank_links(slug, campaign)}\n\n## 免责声明\n\n本报告为月度归档，仅供机场 VPN 选择参考，不构成购买或长期年付建议。机场状态、价格、节点、官网和风险标签可能随时间变化。\n"
    dest.write_text(content, encoding="utf-8")

    meta = {
        "airport": name,
        "slug": slug,
        "month": month,
        "title": title,
        "path": str(rel_path).replace("\\", "/"),
        "gate_rank_url": f"https://gate-rank.com/airports/{slug}",
        "score": fields.get("score") or None,
        "status": fields.get("status") or None,
        "price": fields.get("price") or None,
        "updated_at": dt.datetime.now(dt.timezone.utc).isoformat(),
    }
    return dest, meta


def load_index() -> dict:
    if INDEX_PATH.exists():
        return json.loads(INDEX_PATH.read_text(encoding="utf-8"))
    return {"site": "GateRank 机场测评报告库", "source": "https://gate-rank.com/", "reports": []}


def save_index(index: dict) -> None:
    INDEX_PATH.parent.mkdir(parents=True, exist_ok=True)
    index["reports"] = sorted(index.get("reports", []), key=lambda x: (x.get("month", ""), x.get("airport", "")), reverse=True)
    INDEX_PATH.write_text(json.dumps(index, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def upsert_report(index: dict, meta: dict) -> None:
    reports = [r for r in index.get("reports", []) if r.get("path") != meta["path"]]
    reports.append(meta)
    index["reports"] = reports


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="*", help="Markdown files to import")
    ap.add_argument("--incoming", default=None, help="Directory containing raw Markdown reports")
    ap.add_argument("--archive", action="store_true", help="Move imported incoming files to incoming/archive")
    args = ap.parse_args()

    files = [Path(f) for f in args.files]
    if args.incoming:
        inc = ROOT / args.incoming
        files.extend(sorted(p for p in inc.glob("*.md") if p.is_file()))
    if not files:
        print("No Markdown reports found.")
        return

    index = load_index()
    for src in files:
        if not src.is_absolute():
            src = ROOT / src
        dest, meta = normalize_report(src)
        upsert_report(index, meta)
        print(f"Imported {src} -> {dest.relative_to(ROOT)}")
        if args.archive and args.incoming and "incoming" in src.parts:
            archive_dir = ROOT / args.incoming / "archive"
            archive_dir.mkdir(parents=True, exist_ok=True)
            shutil.move(str(src), str(archive_dir / src.name))
    save_index(index)


if __name__ == "__main__":
    main()
