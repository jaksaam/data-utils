import pandas as pd
import pytest
from src import parse_logs

def test_parse_csv_logs(tmp_path):
    # napravi test CSV fajl sa logovima
    csv_file = tmp_path / "logs.csv"
    csv_file.write_text(
        "timestap,level,message\n"
        "2025-09-28T12:00:00Z,INFO,Started service\n"
        "2025-09-28T12:00:01Z,ERROR,Failed to load x\n"
        "2025-09-28T12:00:02Z,INFO,Processing request\n"
        "2025-09-28T12:00:03Z,INFO,Processing request\n"
    )

    df = pd.read_csv(csv_file)

    # provera
    assert len(df) == 4
    assert list(df.columns) == ["timestap", "level", "message"]
    assert df.iloc[1]["level"] == "ERROR"
    assert df.iloc[1]["message"] == "Failed to load x"

def test_parse_json_logs(tmp_path):
    # napravi test JSON fajl sa logovima (NDJSON format)
    json_file = tmp_path / "logs.json"
    json_file.write_text(
        '{"timestap":"2025-09-28T12:00:00Z","level":"INFO","message":"Started service"}\n'
        '{"timestap":"2025-09-28T12:00:01Z","level":"ERROR","message":"Failed to load x"}\n'
        '{"timestap":"2025-09-28T12:00:02Z","level":"INFO","message":"Processing request"}\n'
        '{"timestap":"2025-09-28T12:00:03Z","level":"INFO","message":"Finished job"}\n'
    )

    df = pd.read_json(json_file, lines=True)

    # provera
    assert len(df) == 4
    assert list(df.columns) == ["timestap", "level", "message"]
    assert df.iloc[0]["message"] == "Started service"
    assert df.iloc[1]["level"] == "ERROR"
