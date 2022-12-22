import click
from random import randint
from ruamel.yaml import safe_load


def _log(fmt_str: str):
    """
    Создает декоратор, который логгирует время выполнения функций пиццерии
    """

    def decorator(function):
        def wrapper(*args, **kwargs):
            time = randint(1, 5)
            print(fmt_str.format(time))
            return function(*args, **kwargs)

        return wrapper

    return decorator


class Pizza:

    """Рецепт пиццы"""

    def __init__(self, pizza: dict, xl: bool):
        """
        Объект класса создается на основе словаря, который парсится из yaml
        """
        self.name = pizza["pizza"].lower()
        self.emoji = pizza["emoji"]
        self.ingredients = pizza["ingredients"]
        self.xl = xl

    def dict(self):
        """Конвертирует объект класса обратно в словарь"""
        return {
            "pizza": self.name,
            "emoji": self.emoji,
            "ingredients": self.ingredients,
        }

    def __str__(self):
        """Строка в меню пиццерии"""
        return f"- {self.name.title()} {self.emoji} :"
        ' {", ".join(self.ingredients)}'

    def __ed__(self, second):
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
    def delivery(self):
        """Здесь должна быть описана логика доставки пиццы"""
        pass

    @_log("🏠  Забрали за {}с!")
    def pickup(self):
        """Здесь должна быть описана логика забора пиццы из пиццерии"""
        pass

    @_log("👩‍🍳  Приготовили за {}с!")
    def bake(self, xl: bool):
        """Процедура приготовления пиццы"""
        pass


def load_menu(source="pizza.yml"):
    """
    Загружает меню пиццерии из исходного yml-файла.
    Возвращает словать <элемент меню>: <рецепт>
    <рецепт> -- как элемент соответствующего класса.
    В настоящей версии реализован только класс пицц.
    """
    with open(source, "rt") as f:
        loaded_menu = safe_load(f)["menu"]
    return {item["pizza"]: Pizza(item) for item in loaded_menu}


def show_menu():
    """Демонстрирует доступное для заказа меню"""
    loaded_menu = load_menu()
    for pizza in loaded_menu.values():
        print(pizza)


@click.group()
def cli():
    """Техническая функция для инициализации группы декораторов cli"""
    pass


@cli.command()
@click.option("--delivery", default=False, is_flag=True)
@click.option("--L", default=False, is_flag=True)
@click.option("--XL", default=False, is_flag=True)
@click.argument("pizza", nargs=1)
def order(pizza: str, delivery: bool, l: bool, xl: bool):
    """
    Готовит и доставляет пиццу, если указан флаг delivery.
    Если пиццы нет -- выведет сообщение об этом и доступное меню.
    Если заказаная пицца должна быть одновременно L и XL --
    укажет на противоречие в заказе.
    """
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
