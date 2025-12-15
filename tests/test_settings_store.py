import json
from pathlib import Path
import pytest

from water_flow.storage import settings_store


def test_load_settings_returns_empty_dict_if_file_missing(tmp_path, monkeypatch):
    fake_path = tmp_path / "settings.json"
    monkeypatch.setattr(settings_store, "get_settings_file_path", lambda: fake_path)

    result = settings_store.load_settings()

    assert result == {}


def test_load_settings_reads_valid_json(tmp_path, monkeypatch):
    fake_path = tmp_path / "settings.json"
    fake_path.write_text(json.dumps({"key": "value"}), encoding="utf-8")
    monkeypatch.setattr(settings_store, "get_settings_file_path", lambda: fake_path)

    result = settings_store.load_settings()

    assert isinstance(result, dict)
    assert result["key"] == "value"


def test_load_settings_invalid_json_raises_value_error(tmp_path, monkeypatch):
    fake_path = tmp_path / "settings.json"
    fake_path.write_text("{ invalid json }", encoding="utf-8")
    monkeypatch.setattr(settings_store, "get_settings_file_path", lambda: fake_path)

    with pytest.raises(ValueError):
        settings_store.load_settings()
