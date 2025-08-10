import pytest
from app.main import add, main


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_main_entrypoint(capsys):
    main()
    captured = capsys.readouterr()
    assert "Result of add(2, 3): 5" in captured.out
