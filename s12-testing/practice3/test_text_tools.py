import pytest

from ask import ask_name
from text_tools import shout


def test_shout(capsys: pytest.CaptureFixture[str]) -> None:
    shout("go team")
    assert capsys.readouterr().out == "GO TEAM!\n"


def test_ask_name(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("builtins.input", lambda prompt: "  ada lovelace ")
    assert ask_name() == "Ada Lovelace"
