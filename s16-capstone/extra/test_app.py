import pytest
from fastapi.testclient import TestClient

import main
from forecast import Hour, parse

SAMPLE = {
    "properties": {
        "periods": [
            {"startTime": "2026-11-01T06:00:00-05:00", "temperature": 48, "probabilityOfPrecipitation": {"value": 0}, "shortForecast": "Sunny"},
            {"startTime": "2026-11-01T07:00:00-05:00", "temperature": 52, "probabilityOfPrecipitation": {"value": None}, "shortForecast": "Cloudy"},
        ]
    }
}


def test_parse() -> None:
    assert parse(SAMPLE) == [Hour("06:00", 48, 0, "Sunny"), Hour("07:00", 52, 0, "Cloudy")]


def test_home(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(main, "fetch_hours", lambda city: parse(SAMPLE))
    monkeypatch.setattr(main, "summarize", lambda city, hours: "Wear a light jacket.")
    response = TestClient(main.app).get("/?city=Chicago")
    assert response.status_code == 200
    assert "Warmest at 07:00" in response.text
    assert "Wear a light jacket." in response.text


def test_unknown_city() -> None:
    response = TestClient(main.app).get("/api/hours?city=Boston")
    assert response.status_code == 422
