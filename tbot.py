import telebot
import pyowm
from pyowm import *
from pyowm.utils.config import get_default_config

bot=telebot.TeleBot('...')#ключ бота
config_dict = get_default_config()
config_dict['language'] = 'ru'#установка русского языка для вывода PYOWM
owm = pyowm.OWM('...',config_dict)#ключ от api OWM
mgr=owm.weather_manager()#создание точки для просмотра погоды

@bot.message_handler(func=lambda m: True)
def mes(message):
	city = message.text
	observation = mgr.weather_at_place(city)
	w = observation.weather
	otvet = 'Погода в городе ' + city.title() + ': ' + w.detailed_status+';'
	a = w.temperature('celsius')
	otvet +='\n'+ 'Максимальная температура: ' + str(a['temp_max']) + ' °C;'+'\n'+'Температура в данный момент '+ str(a['temp']) + ' °C;'+'\n'+'Минимальная температура '+ str(a['temp_min']) + ' °C;'
	b = w.pressure
	bb = w.humidity
	otvet +='\n'+ 'Давление: ' + str(b['press']) + ' мм;'+'\n'+'Влажность: ' + str(bb) + ' %;'
	d = w.wind()
	otvet +='\n'+ 'Ветер: ' + str(d['deg']) + ' °;' +'\n'+ 'Скорость: ' + str(d['speed']) + ' м/c;'
	bot.send_message(message.from_user.id, otvet)

bot.polling()#запуск бота