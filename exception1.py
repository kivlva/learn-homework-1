"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def ask_user():
    """
    Замените pass на ваш код
    """
    def ask_user_dict():
        while True:
            try:
                user_question = input("Задай мне вопрос: ")
                try:
                    answer_is = question_answer[user_question]
                    print  (answer_is)
                    break
                except LookupError:
                    pass
            except KeyboardInterrupt:
                print("Пока!")
                break

    
    question_answer = {"Как дела?":"Хорошо",
                       "Что делаешь?": "Программирую",
                       "Есть ли жизнь на Марсе?":"Вполне возможно",
                       "Какой сейчас год?":"2019",
                       "Кто подставил кролика Роджера?":"Посмотри кино, не хочу спойлерить"
    }
    
    ask_user_dict()
    
if __name__ == "__main__":
    ask_user()
