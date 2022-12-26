import pytest
from cli import load_menu
from pizza import Pizza


def test_load_menu1() -> None:
    res = load_menu(source="test_load_menu1.yml")
    assert isinstance(res, dict)
    assert "pizza1" in res.keys()
    assert isinstance(res["pizza1"], Pizza)


def test_load_menu2() -> None:
    with pytest.raises(TypeError):
        load_menu(source="test_load_menu2.yml")
