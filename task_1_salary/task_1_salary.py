# __author__ == 'Черепанов А.В.'

""" Task: Рассчитать надбавку к зарпалате за стаж
    Если стаж от 2 до 5 лет, надбавка 2%
    Если стаж от 5 до 10 лет, надбавка 5%
"""


from module_math import calculate_bonus, calculate_full_salary
from module_assert import test_calculate_bonus, test_calculate_full_salary


def main():
  test_calculate_bonus()
  test_calculate_full_salary()


  salary = float(input("Введите зарплату: "))
  experience = float(input("Введите стаж: "))


  bonus, percent = calculate_bonus(experience, salary)
  total = calculate_full_salary(salary, bonus)


  print("Надбавка:", percent, "%")
  print("Сумма надбавки:", bonus)
  print("Сумма к выплате:", total)


# Зачем нужна эта конструкция?
if __name__ == "__main__":
    main()