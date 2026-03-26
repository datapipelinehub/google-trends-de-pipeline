import json
from pathlib import Path


def write_audit_record(audit_file: str, record: dict) -> None:
    path = Path(audit_file)
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")
