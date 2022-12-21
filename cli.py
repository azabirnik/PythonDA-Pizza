import click
from random import randint
from ruamel.yaml import safe_load


def _log(fmt_str: str):
    def decorator(function):
        def wrapper(*args, **kwargs):
            time = randint(1, 5)
            print(fmt_str.format(time))
            return function(*args, **kwargs)
        return wrapper
    return decorator


class Pizza:

    """ A class for Pizza """

    def __init__(self, pizza: dict):
        self.name = pizza["pizza"].lower()
        self.emoji = pizza["emoji"]
        self.ingredients = pizza["ingredients"]

    def dict(self):
        return {
            "pizza": self.name,
            "emoji": self.emoji,
            "ingredients": self.ingredients,
        }

    def __str__(self):
        return f'- {self.name.title()} {self.emoji} : {", ".join(self.ingredients)}'

    def __ed__(self, second):
        if self.name != second.name:
            return False
        # pass emoji
        return sorted(self.ingredients) == sorted(second.ingredients)

    @_log("🛵  Доставили за {}с!")
    def delivery(self):
        pass

    @_log("🏠  Забрали за {}с!")
    def pickup(self):
        pass

    @_log("👩‍🍳  Приготовили за {}с!")
    def bake(self, xl: bool):
        pass


def load_menu(source="pizza.yml"):
    with open(source, "rt") as f:
        loaded_menu = safe_load(f)["menu"]
    return {item["pizza"]: Pizza(item) for item in loaded_menu}


def show_menu():
    loaded_menu = load_menu()
    for pizza in loaded_menu.values():
        print(pizza)


@click.group()
def cli():
    pass


@cli.command()
@click.option("--delivery", default=False, is_flag=True)
@click.option("--L", default=False, is_flag=True)
@click.option("--XL", default=False, is_flag=True)
@click.argument("pizza", nargs=1)
def order(pizza: str, delivery: bool, l: bool, xl: bool):
    """Готовит и доставляет пиццу"""
    pizza_order = load_menu().get(pizza.lower())
    if not pizza_order:
        print(f'Такой пиццы в меню нет - "{pizza}". Доступны для заказа:')
        show_menu()
        return
    if l and xl:
        print("Придётся сделать выбор L или XL.")
        return
    pizza_order.bake(xl)
    if delivery:
        pizza_order.delivery()
    else:
        pizza_order.pickup()
    print("Приятного аппетита!")


@cli.command()
def menu():
    """Выводит меню"""
    show_menu()


if __name__ == "__main__":
    cli()
