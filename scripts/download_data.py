from __future__ import annotations

import argparse
from pathlib import Path

PROJECT = {
  "code": "R-12",
  "title": "Web Server Log Analyzer",
  "description": "Regex-based web-log parser for synthetic access logs, route counts, status codes, and hourly traffic."
}
ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    parser = argparse.ArgumentParser(description="Document optional data preparation for this educational lab.")
    parser.add_argument("--write-source-card", action="store_true", help="Write a local source card in data/raw/SOURCE.md.")
    args = parser.parse_args()

    message = (
        f"{PROJECT['code']} - {PROJECT['title']}\n"
        f"{PROJECT['description']}\n\n"
        "This helper intentionally does not download external files automatically. "
        "Use only authorized public or laboratory data, keep large raw files outside Git, "
        "and keep the default CI workflow on synthetic samples."
    )
    print(message)

    if args.write_source_card:
        raw_dir = ROOT / "data" / "raw"
        raw_dir.mkdir(parents=True, exist_ok=True)
        (raw_dir / "SOURCE.md").write_text(message + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
