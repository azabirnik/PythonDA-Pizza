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
  
  Если размер пиццы не указан, делаем `L`.
  
  `--delivery` доставить пиццу заказчику (иначе вам нужно будет забрать её самим)
  
## Тесты

Для запуска теста введите команду (соответствующая библиотека должна быть установлена)

    pytest -v
  
Результат должен быть следующим приблизительно

    =================================================== test session starts ===================================================
  
    platform linux -- Python 3.8.6, pytest-7.2.0, pluggy-1.0.0
  
    rootdir: /app/PythonDA-Pizza
  
    collected 11 items
  
    test_cli.py ..                                                                                                      [ 18%]
  
    test_pizza.py .........                                                                                             [100%]
  

    =================================================== 11 passed in 0.05s ====================================================

    (base) root@6a80d8060de3:/app/PythonDA-Pizza# pytest -v

    =================================================== test session starts ===================================================
  
    platform linux -- Python 3.8.6, pytest-7.2.0, pluggy-1.0.0 -- /opt/conda/bin/python3.8
  
    cachedir: .pytest_cache
  
    rootdir: /app/PythonDA-Pizza
  
    collected 11 items

    test_cli.py::test_load_menu1 PASSED                                                                                 [  9%]

    test_cli.py::test_load_menu2 PASSED                                                                                 [ 18%]
  
    test_pizza.py::test_init1 PASSED                                                                                    [ 27%]
  
    test_pizza.py::test_init2 PASSED                                                                                    [ 36%]
  
    test_pizza.py::test_init3 PASSED                                                                                    [ 45%]
  
    test_pizza.py::test_dict1 PASSED                                                                                    [ 54%]
  
    test_pizza.py::test_str1 PASSED                                                                                     [ 63%]
  
    test_pizza.py::test_eq1 PASSED                                                                                      [ 72%]
  
    test_pizza.py::test_eq2 PASSED                                                                                      [ 81%]
  
    test_pizza.py::test_eq3 PASSED                                                                                      [ 90%]
  
    test_pizza.py::test_eq4 PASSED                                                                                      [100%]
  
    =================================================== 11 passed in 0.04s ====================================================
