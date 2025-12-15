import json
import sys
from pathlib import Path
import tempfile

from water_flow.storage import settings_store


def run():
    # Test 1: file missing -> {}
    with tempfile.TemporaryDirectory() as td:
        fake = Path(td) / "settings.json"
        orig = settings_store.get_settings_file_path
        settings_store.get_settings_file_path = lambda: fake
        try:
            assert settings_store.load_settings() == {}
        finally:
            settings_store.get_settings_file_path = orig

    # Test 2: valid json
    with tempfile.TemporaryDirectory() as td:
        fake = Path(td) / "settings.json"
        fake.write_text(json.dumps({"key": "value"}), encoding="utf-8")
        orig = settings_store.get_settings_file_path
        settings_store.get_settings_file_path = lambda: fake
        try:
            data = settings_store.load_settings()
            assert isinstance(data, dict)
            assert data["key"] == "value"
        finally:
            settings_store.get_settings_file_path = orig

    # Test 3: invalid json -> ValueError
    with tempfile.TemporaryDirectory() as td:
        fake = Path(td) / "settings.json"
        fake.write_text("{ invalid json }", encoding="utf-8")
        orig = settings_store.get_settings_file_path
        settings_store.get_settings_file_path = lambda: fake
        try:
            try:
                settings_store.load_settings()
                raise SystemExit("Expected ValueError but none was raised")
            except ValueError:
                pass
        finally:
            settings_store.get_settings_file_path = orig

    print("All checks passed")


if __name__ == "__main__":
    try:
        run()
    except AssertionError as exc:
        print("Assertion failed:", exc)
        sys.exit(1)
    except Exception as exc:
        print("Error during checks:", exc)
        sys.exit(2)