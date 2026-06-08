import csv
from pathlib import Path
from typing import Union


def load_customer_segments(path: Union[str, Path]) -> list[dict[str, str]]:
    """Load customer segment records from the latest CRM export."""
    rows: list[dict[str, str]] = []

    with Path(path).open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for raw in reader:
            rows.append(
                {
                    "customer_id": raw["customer_id"].strip(),
                    "tier": raw["customer_tier"].strip().lower(),
                    "region": raw["region_code"].strip(),
                }
            )

    return rows
