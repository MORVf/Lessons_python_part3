'''
Требуется написать программу, осуществляющую преобразование из одних единиц измерения длины в другие. 
Должны поддерживаться:
- мили (1 mile = 1609 m), 
- ярды (1 yard = 0.9144 m), 
- футы (1 foot = 30.48 cm), 
- дюймы (1 inch = 2.54 cm), 
- километры (1 km = 1000 m), 
- метры (m), 
- сантиметры (1 cm = 0.01 m)
- миллиметры (1 mm = 0.001 m)

Используйте именно указанные в формулировке задачи единицы измерения с указанной точностью.

Формат ввода:
Одна строка с фразой следующего вида:
<number> <unit_from> in <unit_to>
например, если пришла фраза "15.5 mile in km", то требуется перевести 15.5 миль в километры.

Формат вывода:
Дробное число в научном формате (экспоненциальном), с точностью ровно два знака после запятой.

Sample Input:
15.5 mile in km

Sample Output:
2.49e+01
'''

#словарь с единицами измерения длины (в метрах)
dict_units_of_length_measurement = {'mm': 0.001, 'cm': 0.01, 'm': 1, 'km': 1000, 'inch': 0.0254, 'foot': 0.3048, 'yard': 0.9144, 'mile': 1609}

n = input().split() #считываем строку и формируем список

res = float(n[0]) * dict_units_of_length_measurement[n[1]] / dict_units_of_length_measurement[n[3]]   #вычисляем длину
print('%.2e' % res)  #выводим длину в научном формате с точностью до двух знаков после запятой
