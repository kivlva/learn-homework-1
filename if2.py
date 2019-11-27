"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """

    def str_compare(str1, str2):
        if not (type(str1) == type("это строка") and type(str1) == type(str2) ):
            return(0)
        elif not (str1 == str2):
            if str2 == 'learn':
                return (3)
            elif len(str1) > len(str2):
                return (2)
        else:
            return(1)


    print(str_compare(None, 1)) # None и число -> ожидаем 0
    print(str_compare("this is string", 10500)) # строка и число -> ожидаем 0
    print(str_compare("this is string", "this is string")) # одинаковые строки -> ожидаем 1
    print(str_compare("this is very big string", "this is string")) # строки разные, первая больше второй -> ожидаем 2
    print(str_compare("this is string", "learn")) # строки разные, вторая = 'learn'  -> ожидаем 3
    print(str_compare("this is string", "this is very big string")) # строки разные, первая меньше второй, вторая не равна 'learn'  -> неучтенный в условии кейс, ожидаем None
    
if __name__ == "__main__":
    main()
