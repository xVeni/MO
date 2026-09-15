from module_math import calculate_bonus, calculate_full_salary


def test_calculate_bonus():
    assert calculate_bonus(1, 100000) == (0, 0)
    assert calculate_bonus(2, 100000) == (2000, 2)
    assert calculate_bonus(4, 100000) == (2000, 2)
    assert calculate_bonus(5, 100000) == (5000, 5)
    assert calculate_bonus(10, 100000) == (5000, 5)
    print("бонус прошёл тест")


def test_calculate_full_salary():
    assert calculate_full_salary(100000, 2000) == 102000
    assert calculate_full_salary(100000, 5000) == 105000
    assert calculate_full_salary(50000, 0) == 50000
    print("полная зарплата прошла тест")