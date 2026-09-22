#__author__ == 'Черепанов А.В.'

import numpy as np

from module_list import (
    generate_list,
    generate_set,
    generate_numpy,
    relu_sum
)


def test_generate_list() -> None:
    """
    Проверка функции generate_list.

    Проверяется количество элементов, уникальность чисел
    и то, что все числа являются четными.

    :return: ничего не возвращает
    """

    n: int = 1000

    result: list[int] = generate_list(n)

    assert len(result) == n
    assert len(result) == len(set(result))
    assert all(number % 2 == 0 for number in result)


def test_generate_set() -> None:
    """
    Проверка функции generate_set.

    Проверяется количество элементов, уникальность чисел
    и то, что все числа являются четными.

    :return: ничего не возвращает
    """

    n: int = 1000

    result: set[int] = generate_set(n)

    assert len(result) == n
    assert len(result) == len(set(result))
    assert all(number % 2 == 0 for number in result)


def test_generate_numpy() -> None:
    """
    Проверка функции generate_numpy.

    Проверяется количество элементов, уникальность чисел
    и то, что все числа являются четными.

    :return: ничего не возвращает
    """

    n: int = 1000

    result: np.ndarray = generate_numpy(n)

    assert len(result) == n
    assert len(result) == len(np.unique(result))
    assert np.all(result % 2 == 0)


def test_relu_sum() -> None:
    """
    Проверка функции relu_sum.

    :return: ничего не возвращает
    """

    data: np.ndarray = np.array([-5, -2, 0, 3, 7, -1])

    result: np.int64 = relu_sum(data)

    assert result == 10


def test() -> None:
    """
    Запуск всех тестов программы.

    :return: ничего не возвращает
    """

    test_generate_list()
    test_generate_set()
    test_generate_numpy()
    test_relu_sum()

    print("Все тесты пройдены")