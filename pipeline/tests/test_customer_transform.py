from pathlib import Path

from pipeline.customer_transform import load_customer_segments


DATA_FILE = Path(__file__).resolve().parents[1] / "data" / "customer_events_after.csv"


def test_transform_supports_schema_drift_and_missing_region() -> None:
    assert load_customer_segments(DATA_FILE) == [
        {"customer_id": "C-1001", "tier": "gold", "region": "NA"},
        {"customer_id": "C-1002", "tier": "silver", "region": "UNKNOWN"},
        {"customer_id": "C-1003", "tier": "platinum", "region": "EU"},
    ]

