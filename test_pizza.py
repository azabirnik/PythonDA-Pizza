from pizza import Pizza
import pytest


def test_init1() -> None:
    with pytest.raises(TypeError):
        Pizza()


def test_init2() -> None:
    with pytest.raises(TypeError):
        Pizza("pizza")


def test_init3() -> None:
    with pytest.raises(KeyError):
        Pizza({"piza": "margerita"})


def test_dict1() -> None:
    pizza_dict = {"pizza": "margerita", "ingredients": ["a", "b"]}
    res = pizza_dict
    res["emoji"] = ""
    assert Pizza(pizza_dict).dict() == pizza_dict


def test_str1() -> None:
    pizza_dict = {"pizza": "margerita", "ingredients": ["a", "b"]}
    assert str(Pizza(pizza_dict)) == "- Margerita  : a, b"


def test_eq1() -> None:
    pizza_dict = {"pizza": "margerita", "ingredients": ["a", "b"]}
    assert Pizza(pizza_dict) == Pizza(pizza_dict)


def test_eq2() -> None:
    pizza_dict1 = {"pizza": "margerita", "ingredients": ["a", "b"]}
    pizza_dict2 = {"pizza": "margerita", "ingredients": ["a", "b", "c"]}
    assert Pizza(pizza_dict1) != Pizza(pizza_dict2)


def test_eq3() -> None:
    pizza_dict1 = {"pizza": "margerita", "ingredients": ["a", "b"]}
    pizza_dict2 = {"pizza": "Margerita", "ingredients": ["a", "b"]}
    assert Pizza(pizza_dict1) == Pizza(pizza_dict2)


def test_eq4() -> None:
    pizza_dict1 = {"pizza": "marger", "ingredients": ["a", "b"]}
    pizza_dict2 = {"pizza": "Marger", "emoji": "@", "ingredients": ["a", "b"]}
    assert Pizza(pizza_dict1) == Pizza(pizza_dict2)
