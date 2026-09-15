def calculate_bonus(experience: int, salary:int):
  
  percent = 0

  # Если стаж от 2 до 5 лет, надбавка 2
  if experience >= 2 and experience < 5:
    percent = 2

# Если стаж от 5 до 10 лет, надбавка 5%
  elif experience >= 5 and experience <= 10:
    percent = 5

  bonus = salary * percent / 100
  return bonus, percent


def calculate_full_salary(salary:int, bonus:int):
  total = salary + bonus
  return total