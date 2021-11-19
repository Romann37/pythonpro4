import requests
from datetime import datetime
from pprint import pprint

# п.1 декоратор-логгер
def get_info_function(function):
    def new_function(*args, **kwargs):
        result = function(*args, **kwargs)
        log = f'Время: {datetime.now()}, имя функции:{function.__name__}, аргументы: {args} {kwargs}, ' \
              f'результат: {result} \n'
        with open('log.txt', 'a', encoding='UTF-8') as file:
            file.writelines(log)
        return result
    return new_function


### п.2 декоратор-логгер с параметром – путь к логам
def get_log_function_path(path):
    def get_info_function(function):
        def new_function(*args, **kwargs):
            result = function(*args, **kwargs)
            log = f'Время: {datetime.now()}, имя функции:{function.__name__}, аргументы: {args} {kwargs}, ' \
                  f'результат: {result} \n'
            with open(path, 'a', encoding='UTF-8') as file:
                file.writelines(log)
            return result
        return new_function
    return get_info_function


# п.3 Применить написанный логгер к приложению из любого предыдущего д/з.
@get_log_function_path('log.txt')


def read_cookbook(file_path):
    cook_book = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            dish_name = line.strip()
            count = int(f.readline())
            ing_list = list()
            for item in range(count):
                ingrs = {}
                ingr = f.readline().strip()
                ingrs['ingredient_name'], ingrs['quantity'], ingrs['measure'] = ingr.split('|')
                ingrs['quantity'] = int(ingrs['quantity'])
                ing_list.append(ingrs)
            f.readline()
            cook_book[dish_name] = ing_list
    return cook_book
    
                
cook_book = read_cookbook('recipes.txt')
pprint(cook_book)

