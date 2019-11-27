"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    allscores = [
        {'school_class': '1a', 'scores': [5,5,5,3,4,4,5,2,3,4,5]},
        {'school_class': '2a', 'scores': [3,3,4,5,2,4,4,3,4,5]},
        {'school_class': '3a', 'scores': [3,4,4,5,3,4,5,3,2,4]},
        {'school_class': '4a', 'scores': [2,5,3,4,5,5,5,5,3,4,5]},
        {'school_class': '8a', 'scores': [3,4,3,4,3,3,3,3,5,4]},
        {'school_class': '9a', 'scores': [4,3,4,3,4,5,2,4]},
        {'school_class': '9b', 'scores': [3,4,4,5,2,3,4,5,3]},
        {'school_class': '7b', 'scores': [5]},
        {'school_class': '2b', 'scores': [4]}
    ]

    total_score = 0
    amt_scores = 0
    for current_class in allscores:
        total_class_score = 0
        for cur_score in current_class['scores']:
            total_class_score += cur_score
        current_class['avg_score'] =  total_class_score / len(current_class['scores'])
        total_score += total_class_score
        amt_scores += len(current_class['scores'])
        print('Средний балл по классу {school_class}: {score}'.format(school_class=current_class["school_class"], score=current_class['avg_score']))
    print(f'Средний балл по школе: {total_score / amt_scores}')

    
if __name__ == "__main__":
    main()
