#__author__ Черепанов А.В.

"""Вывести все четные числа кратные 5, от 0 до 100"""

from module_range_count import even_multiple_five
from module_assert import test


def main():
    test()
    
    min_num:int = 2 # начало промежутка
    max_num:int = 100 # конец промежутка
    max_num = int(input("Введите конец промежутка: "))

    result = even_multiple_five(min_num, max_num)

    print(result)

# Зачем нужна эта конструкция?
if __name__ == "__main__":
    main()