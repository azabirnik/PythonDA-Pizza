from random import randint
from typing import Callable, Any


def _log(fmt_str: str) -> Callable:
    """
    Создает декоратор, который логгирует время выполнения функций пиццерии
    """

    def decorator(function: Callable) -> Callable:
        def wrapper(*args, **kwargs) -> Any:
            time = randint(1, 5)
            print(fmt_str.format(time))
            return function(*args, **kwargs)

        return wrapper

    return decorator


class Pizza:

    """Рецепт пиццы"""

    def __init__(self, pizza: dict, xl=False) -> None:
        """
        Объект класса создается на основе словаря, который парсится из yaml
        """
        self.name = pizza["pizza"].lower()
        self.emoji = pizza.get("emoji", "")
        self.ingredients = pizza["ingredients"]
        self.xl = xl

    def dict(self) -> dict:
        """Конвертирует объект класса обратно в словарь"""
        return {
            "pizza": self.name,
            "emoji": self.emoji,
            "ingredients": self.ingredients,
        }

    def __str__(self) -> str:
        """Строка в меню пиццерии"""
        ingrid = ", ".join(self.ingredients)
        return f"- {self.name.title()} {self.emoji} : {ingrid}"

    def __eq__(self, second) -> bool:
        """
        Считаем что пиццы совпадают если их имена, размеры и составы совпадают
        """
        if self.name != second.name:
            return False
        # Эмоджи игнорируем
        return (
            sorted(self.ingredients) == sorted(second.ingredients)
            and self.xl == second.xl
        )

    @_log("🛵  Доставили за {}с!")
    def delivery(self) -> None:
        """Здесь должна быть описана логика доставки пиццы"""
        pass

    @_log("🏠  Забрали за {}с!")
    def pickup(self) -> None:
        """Здесь должна быть описана логика забора пиццы из пиццерии"""
        pass

    @_log("👩‍🍳  Приготовили за {}с!")
    def bake(self) -> None:
        """Процедура приготовления пиццы"""
        pass
