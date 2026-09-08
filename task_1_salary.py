# Черепанов А.В.
# Рассчитать надбавку к зарпалате за стаж


salary = float(input("Введите зарплату: "))
experience = float(input("Введите стаж: "))

# Надбавка
percent = 0

# Если стаж от 2 до 5 лет, надбавка 2%
if experience >= 2 and experience < 5:
    percent = 2

# Если стаж от 5 до 10 лет, надбавка 5%
elif experience >= 5 and experience <= 10:
    percent = 5
    
# Рассчет суммы надбавки
bonus = salary * percent / 100

# Рассчет суммы к выплате
total = salary + bonus


print("Надбавка:", percent, "%")
print("Сумма надбавки:", bonus)
print("Сумма к выплате:", total)
