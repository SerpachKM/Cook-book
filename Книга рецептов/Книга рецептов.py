'''Импорт модулей.'''
import os
import time
from pprint import pprint

def read_cookbook():
    '''Это функция которая считывает содержимое файла recipes.txt и сохраняет его в словарь cook_book.
    Она использует модуль os для получения текущего каталога (os.getcwd()) и функцию os.path для объединения пути к файлу recipes.txt.
    Затем она открывает файл в режиме чтения (with open('recipes.txt', 'r')) и считывает каждую строку файла.
    Для каждой строки она удаляет пробелы в начале и конце строки, используя метод strip(), а затем разбивает строку на три поля с помощью метода split('|').
    Затем она преобразует количество ингредиентов в int и добавляет их в список ing_list, который затем добавляется в словарь cook_book с ключом, полученным из строки.
    В конце функции она закрывает файл.'''
    file_path = os.path.join(os.getcwd(), 'recipes.txt')
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




def get_shop_list_by_dishes(dishes, person_count):
    '''Данный код получает список блюд (dishes) и количество людей (person_count) и возвращает словарь с количеством ингредиентов для каждого блюда.
    Функция сначала создает пустой словарь ingr_list, который будет использоваться для хранения количества ингредиентов для каждого блюда.
    Затем она проходит по каждому блюду в списке dishes и проверяет, есть ли оно в словаре cook_book.
    Если блюдо есть в cook_book, то функция проходит по ингредиентам этого блюда и добавляет их количество в словарь ingr_list.
    Если ингредиент уже есть в словаре, то функция увеличивает его количество на количество человек.
    Если блюдо не найдено в cook_book, функция выводит сообщение об ошибке. В целом, данная функция позволяет получить список ингредиентов для каждого блюда, учитывая количество людей.'''
    ingr_list = dict()

    for dish_name in dishes:
        if dish_name in cook_book:
            for ings in cook_book[dish_name]:
                meas_quan_list = dict()
                if ings['ingredient_name'] not in ingr_list:
                    meas_quan_list['measure'] = ings['measure']
                    meas_quan_list['quantity'] = ings['quantity'] * person_count
                    ingr_list[ings['ingredient_name']] = meas_quan_list
                else:
                    ingr_list[ings['ingredient_name']]['quantity'] = ingr_list[ings['ingredient_name']]['quantity'] + \
                                                                     ings['quantity'] * person_count

        else:
            print(f'\n"Такого блюда нет в списке!"\n')
    return ingr_list





def rewrite_file(path1=None, path2=None, path3=None):
    '''Данный код имеет три аргумента: path1, path2 и path3, которые могут быть заданы пользователем.
    В случае, если один из аргументов не задан, функция использует значения по умолчанию.
    Если все аргументы не заданы, она переходит в каталог "sorted" и создает файл "rewrite_file.txt".
    Затем функция открывает файлы "1.txt", "2.txt" и "3.txt" в режиме чтения и считывает их содержимое в переменные file1 и file2 соответственно.
    После этого функция закрывает файлы и возвращает переменные file1 и file2'''
    if path1 or path2 or path3 is None:
        path1 = '1.txt'
        path2 = '2.txt'
        path3 = '3.txt'
        os.chdir('sorted')
        outout_file = "rewrite_file.txt"
        file1_path = os.path.join(os.getcwd(), path1)
        file2_path = os.path.join(os.getcwd(), path2)
        file3_path = os.path.join(os.getcwd(), path3)
        with open(file1_path, 'r', encoding='utf-8') as f1:
            file1 = f1.readlines()
        with open(file2_path, 'r', encoding='utf-8') as f2:
            file2 = f2.readlines()
        with open(file3_path, 'r', encoding='utf-8') as f3:
            file3 = f3.readlines()
        with open(outout_file, 'w', encoding='utf-8') as f_total:

            if len(file1) < len(file2) and len(file1) < len(file3):
                f_total.write(path1 + '\n')
                f_total.write(str(len(file1)) + '\n')
                f_total.writelines(file1)
                f_total.write('\n')
            elif len(file2) < len(file1) and len(file2) < len(file3):
                f_total.write(path2 + '\n')
                f_total.write(str(len(file2)) + '\n')
                f_total.writelines(file2)
                f_total.write('\n')
            elif len(file3) < len(file1) and len(file3) < len(file2):
                f_total.write(path3 + '\n')
                f_total.write(str(len(file3)) + '\n')
                f_total.writelines(file3)
                f_total.write('\n')
            if len(file2) > len(file1) > len(file3) or len(file2) < len(file1) < len(
                    file3):
                f_total.write(path1 + '\n')
                f_total.write(str(len(file1)) + '\n')
                f_total.writelines(file1)
                f_total.write('\n')
            elif len(file1) > len(file2) > len(file3) or len(file2) > len(file1) and len(file2) < len(
                    file3):
                f_total.write(path2 + '\n')
                f_total.write(str(len(file2)) + '\n')
                f_total.writelines(file2)
                f_total.write('\n')
            elif len(file1) > len(file3) > len(file2) or len(file3) > len(file1) and len(file3) < len(
                    file2):
                f_total.write(path3 + '\n')
                f_total.write(str(len(file3)) + '\n')
                f_total.writelines(file3)
                f_total.write('\n')
            if len(file1) > len(file2) and len(file1) > len(file3):
                f_total.write(path1 + '\n')
                f_total.write(str(len(file1)) + '\n')
                f_total.writelines(file1)
            elif len(file2) > len(file1) and len(file2) > len(file3):
                f_total.write(path2 + '\n')
                f_total.write(str(len(file2)) + '\n')
                f_total.writelines(file2)
            elif len(file3) > len(file1) and len(file3) > len(file2):
                f_total.write(path3 + '\n')
                f_total.write(str(len(file3)) + '\n')
                f_total.writelines(file3)
    else:
        print('Давай лучше без параметров')
    return


if __name__ == '__main__':
    filename = "recipes.txt"
    cook_book = read_cookbook()
    print('Задание 1')
    time.sleep(2)
    print(cook_book)
    print('Задание 2')
    pprint(get_shop_list_by_dishes(dishes=['Запеченный картофель', 'Омлет'], person_count=2))

    time.sleep(2)
    print('Задание 3')
    rewrite_file()
    