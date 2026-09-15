from module_range_count import even_multiple_five


def test():
    assert even_multiple_five(0, 100) == [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    assert even_multiple_five(2, 20) == [10, 20]
    assert even_multiple_five(11, 19) == []
    assert even_multiple_five(1, 10) == [10]

    print("тесты пройдены")