import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import random
import pyowm
from pyowm import *
from pyowm.utils.config import get_default_config

config_dict = get_default_config()
config_dict['language'] = 'ru'
owm = pyowm.OWM('...',config_dict)
mgr=owm.weather_manager()
token='...'
def write_msg(user_id, message):
	random_id = vk_api.utils.get_random_id()
	vk.method('messages.send',{'user_id': user_id, 'message': message, 'random_id': random_id})
vk = vk_api.VkApi(token=token)
longpoll = VkLongPoll(vk)
for event in longpoll.listen():
	if event.type == VkEventType.MESSAGE_NEW:
		if event.to_me:
			request = event.text
			city = request
			observation = mgr.weather_at_place(city)
			w = observation.weather
			otvet = 'Погода в городе ' + city.title() + ': ' + w.detailed_status
			write_msg(event.user_id, otvet)
			a = w.temperature('celsius')['temp']
			otvet = 'Температура: ' + str(a) + ' °C'
			write_msg(event.user_id, otvet)
			b = w.pressure
			bb = w.humidity
			otvet = 'Давление: ' + str(b['press']) + '; Влажность: ' + str(bb) + ' %'
			write_msg(event.user_id, otvet)
			d = w.wind()
			otvet = 'Ветер: ' + str(d['deg']) + ' °;' + ' Скорость: ' + str(d['speed']) + ' м/c'
			write_msg(event.user_id, otvet)
