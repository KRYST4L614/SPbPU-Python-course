money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
count = 0

while salary + money_capital >= spend:
    count += 1
    money_capital -= spend - salary
    spend += spend*increase

print("Количество месяцев, которое можно протянуть без долгов:", count)
