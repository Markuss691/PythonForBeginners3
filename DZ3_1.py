from DZ3 import compare as compare

StrSr = input('Введите наименование города для сравнения: ')

towns = [
    'Кадников', 'Казань', 'Калач', 'Калач-на-Дону', 'Калининград', 'Калуга'
    ]

for town in towns: 
    print(compare(town,StrSr))
