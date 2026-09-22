#__author__ == 'Черепанов А.В.'

import csv
import random
import time
import numpy as np


MAX_VALUE: int = 10_000_000


def write_list_in_file(filename: str, data: list[list]) -> None:
    """
    Запись списка в текстовый файл в формате CSV.

    :param filename: название файла для записи
    :param data: список данных для записи в файл
    :return: ничего не возвращает

    Сложность: O(n)
    """

    with open(filename, "w", newline="", encoding="utf8") as file:
        writer = csv.writer(file)
        writer.writerows(data)


def generate_list(n: int) -> list[int]:
    """
    Генерация n уникальных четных чисел от 1 до MAX_VALUE
    с использованием списка, модуля random и функции randint.

    :param n: количество чисел для генерации
    :return: список уникальных четных чисел

    Сложность: O(n²)
    """

    result: list[int] = []

    while len(result) < n:
        number: int = random.randint(1, MAX_VALUE)

        # Проверяем, является ли число четным
        if number % 2 == 0:

            # Проверяем, нет ли числа в списке
            if number not in result:
                result.append(number)

    return result


def generate_set(n: int) -> set[int]:
    """
    Генерация n уникальных четных чисел от 1 до MAX_VALUE
    с использованием множества, модуля random и функции randint.

    :param n: количество чисел для генерации
    :return: множество уникальных четных чисел

    Сложность:
    Время: O(n) в среднем
    Память: O(n)
    """

    result: set[int] = set()

    while len(result) < n:
        number: int = random.randint(1, MAX_VALUE)

        # Проверяем, является ли число четным
        if number % 2 == 0:
            result.add(number)

    return result


def generate_numpy(n: int) -> np.ndarray:
    """
    Генерация n уникальных четных чисел от 1 до MAX_VALUE
    с использованием массива ndarray из библиотеки NumPy.

    :param n: количество чисел для генерации
    :return: массив ndarray с уникальными четными числами

    Сложность: O(n)
    """

    result: np.ndarray = np.random.choice(
        np.arange(2, MAX_VALUE + 1, 2),
        size=n,
        replace=False
    )

    return result


def measure_time(function, n: int) -> tuple[float, object]:
    """
    Измерение времени выполнения функции генерации данных.

    :param function: функция, время выполнения которой необходимо измерить
    :param n: количество генерируемых чисел
    :return: время выполнения функции и результат её работы

    Сложность:
    Время: O(f(n))
    Память: зависит от переданной функции
    """

    start: float = time.perf_counter()

    result = function(n)

    end: float = time.perf_counter()

    return end - start, result


def relu_sum(data: np.ndarray) -> np.int64:
    """
    Преобразование каждого элемента массива по формуле ReLU
    и вычисление суммы полученных элементов.

    ReLU(x) = 0, если x < 0
    ReLU(x) = x, если x >= 0

    :param data: массив ndarray, элементы которого необходимо преобразовать
    :return: сумма элементов массива после применения ReLU

    Сложность: O(n)
    """

    result: np.ndarray = np.maximum(data, 0)

    return np.sum(result)