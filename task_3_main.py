#__author__ == 'Черепанов А.В.'

from module_list import (
    generate_list,
    generate_set,
    generate_numpy,
    measure_time,
    relu_sum,
    write_list_in_file
)

from module_assert_lists import test


def main() -> None:
    """
    Основная функция программы.

    Запускает тесты, генерирует данные, сравнивает время работы
    различных способов генерации и записывает результаты в CSV-файл.

    :return: ничего не возвращает
    """

    # Запуск assert-тестов
    test()

    sizes: list[int] = [1_000, 10_000]

    results: list[list] = [
        ["n", "list_time", "set_time", "numpy_time", "relu_sum"]
    ]

    for n in sizes:
        print(f"\nn = {n}")

        # Генерация списка
        time_list, list_data = measure_time(generate_list, n)
        print(f"list:  {time_list:.6f} секунд")

        # Генерация множества
        time_set, set_data = measure_time(generate_set, n)
        print(f"set:   {time_set:.6f} секунд")

        # Генерация массива NumPy
        time_numpy, numpy_data = measure_time(generate_numpy, n)
        print(f"numpy: {time_numpy:.6f} секунд")

        # Применение ReLU и вычисление суммы
        relu_result = relu_sum(numpy_data)

        print(f"Сумма после ReLU: {relu_result}")


        results.append([
            n,
            time_list,
            time_set,
            time_numpy,
            relu_result
        ])


    write_list_in_file("results.csv", results)

    print("\nРезультаты записаны в файл results.csv")


if __name__ == "__main__":
    main()