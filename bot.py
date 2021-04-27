import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import random
import pyowm

owm = pyowm.OWM('...', language='RU')
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
			observation = owm.weather_at_place(city)
			w = observation.get_weather()
			otvet = 'Погода в городе ' + city.title() + ': ' + w.get_detailed_status()
			write_msg(event.user_id, otvet)
			a = w.get_temperature('celsius')['temp']
			otvet = 'Температура: ' + str(a) + ' °C'
			write_msg(event.user_id, otvet)
			b = w.get_pressure()
			bb = w.get_humidity()
			otvet = 'Давление: ' + str(b['press']) + '; Влажность: ' + str(bb) + ' %'
			write_msg(event.user_id, otvet)
			d = w.get_wind()
			otvet = 'Ветер: ' + str(d['deg']) + ' °;' + ' Скорость: ' + str(d['speed']) + ' м/c'
			write_msg(event.user_id, otvet)
