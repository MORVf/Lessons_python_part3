'''
Напишите программу, которая проверяет, являются ли два введённых слова анаграммами.
Программа должна вывести True в случае, если введённые слова являются анаграммами, и False в остальных случаях.

Формат ввода:
Два слова, каждое на отдельной строке. 
Слово может состоять только из латинских символов произвольного регистра. Регистр символов не должен влиять на ответ.

Формат вывода:
True или False.

Sample Input 1:
silent
listen
Sample Output 1:
True

Sample Input 2:
AbaCa
AcaBa
Sample Output 2:
True

Sample Input 3:
abaca
acada
Sample Output 3:
False
'''

word1 = input().lower() #считываем первое слово и переводим в нижний регистр
word2 = input().lower() #считываем второе слово и переводим в нижний регистр
    
def lst_sort(word):   #функция формирования сортированного списка из строки
    lst = []
    for symbol in word: #считываем каждый символ из строки
        lst += symbol  #и записываем в список
    lst.sort()   #сортируем по возрастанию
    return lst   #вернуть список

if lst_sort(word1) == lst_sort(word2):   #если списки равны, то
    print('True')  #возвращаем True
else:   #иначе возвращаем
    print('False')   #False