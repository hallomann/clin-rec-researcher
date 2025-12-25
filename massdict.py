from adtodict import adtodict

name = input("Введите название заболевания в формате: ID МКБ + имя заболевания")
while name != "0":
    adtodict(name)
    name = input("Следующее название (для окончания введите 0)")
