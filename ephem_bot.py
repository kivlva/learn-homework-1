"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход 
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите 
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите 
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging, ephem
from datetime import date
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
)

"""
PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn', 
        'password': 'python'
    }
}
"""

def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)

def get_const(planet):

    today = date.today()

    planets = {
        'Mercury': ephem.Mercury(today),
        'Venus': ephem.Venus(today),
        'Moon': ephem.Moon(today),
        'Mars': ephem.Mars(today),
        'Jupiter': ephem.Jupiter(today),
        'Uranus': ephem.Uranus(today),
        'Neptune': ephem.Neptune(today),
        'Pluto': ephem.Pluto(today)
    }

    try:
        planet_object = planets[planet]
        const = ephem.constellation(planet_object)
        output_text = "Планета {plnt} сегодня находится в созвездии {cnst}".format(plnt=planet,cnst=const)
    except KeyError:
        output_text = "Попробуйте ввести название планеты на английском с большой буквы"
    return(output_text)

def planet(bot, update):

    text = update.message.text
    print(text)
    lplanet = text.split()
    try:
        my_planet = lplanet[1]
        output_text = get_const(my_planet)
    except IndexError:
        output_text = "Ожилалась команда вида '/planet НазваниеПланеты'"

    update.message.reply_text(output_text)

def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)
 

def main():
    #mybot = Updater("990130820:AAH8xm8ufJA6hLHdwSlOi5QJCiRULfOZZv8", request_kwargs=PROXY)
    mybot = Updater("990130820:AAH8xm8ufJA6hLHdwSlOi5QJCiRULfOZZv8")
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    mybot.start_polling()
    mybot.idle()
       

if __name__ == "__main__":
    main()