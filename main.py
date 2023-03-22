a = int(input('Сколько денег на счету'))
discount = 0
if a >= 75000:
  print('Списать со счета деньги')
  if a <= 5000:
    print('Cделана скидка')
    discount = 1000
price = a + discount
print('Курс успешно приобритен')