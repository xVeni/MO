# __author__ == 'Черепанов А.В.'

def even_multiple_five(min_num: int, max_num:int):
  """
  Перебор всех четных и кратных 5 чисел от min_num до max_num
  :param: min_num начало промежутка
  :param: min max конец промежутка
  :return: возвращает все четные и кратные числа
  """

  result = []

  for number in range(min_num, max_num+1):

    # Проверяем, является ли число чётным
    if number % 2 == 0:

      # Проверяем, кратно ли число пяти
      if number % 5 == 0:
        result.append(number)
  return result

# А вообще можно сделать так "for i in range(0, x+1, 10)"