# __author__ == 'Черепанов А.В.'

def calculate_bonus(experience: int, salary:int):

  """
  Рассчет надбавки зависящий от стажа.

  :param experience: стаж работы в годах
  :param salary: зарплата
  :return: сумма надбавки и процент надбавки
  """

  percent:int = 0

  # Если стаж от 2 до 5 лет, надбавка 2
  if experience >= 2 and experience < 5:
    percent = 2

# Если стаж от 5 до 10 лет, надбавка 5%
  elif experience >= 5 and experience <= 10:
    percent = 5

  bonus:int = salary * percent / 100
  return bonus, percent


def calculate_full_salary(salary:int, bonus:int):
  """
  Рассчет зарпалаты с бонусом

  :param salary: зарплата
  :param bonus: надбавка в деньгах
  :return: полная сумма зарплаты
  """
  total:int = salary + bonus
  return total