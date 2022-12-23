import click

from ruamel.yaml import safe_load
from pizza import Pizza


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
    pizza_order.xl = xl
    pizza_order.bake()
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
