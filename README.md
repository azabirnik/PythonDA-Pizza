# PythonDA-Pizza
## Требования
Для запуска понадобится интерпретатор python и библиотеки `click` и `ruamel.yaml`. К сожалению, эмоджи корректно отображаются только в Unix / Linux. Меню пиццерии содержится в файле `pizza.yml`.

## Команды и опции
Показать меню

    python cli.py menu
    
    
Заказать пиццу

    python cli.pu order <pizza> [--L|--XL] [--delivery]
  
  `--L` для большой пиццы
  
  `--XL` для очень большой (маленьких не делаем)
  
  `--delivery` доставить пиццу заказчику (иначе вам нужно будет забрать её самим)
