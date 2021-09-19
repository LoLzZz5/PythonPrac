from tkinter import *
import requests

def weather():
	city = city1.get()

	key = 'd149d2734b8d63f84861457096ea7f2a'
	url = 'http://api.openweathermap.org/data/2.5/weather'
	params = {'APPID': key, 'q': city, 'units': 'metric'}
	result = requests.get(url, params=params)
	weather = result.json()
	info['text'] = 'Погода в городе 'f'{str(weather["name"])}: \n Температура: {weather["main"]["temp"]} °C \n Давление: {weather["main"]["pressure"]} мм. ртутного столба \n Ветер: {weather["wind"]["speed"]} м/c \n Влажность: {weather["main"]["humidity"]}%'

	

root = Tk()
root.title("OpenWeatherMap API")

frame_top = Frame(root, bd = 5)
frame_top.place(relx = 0.15, rely = 0.15, relwidth = 0.7, relheight = 0.25)

frame_bottom = Frame(root)
frame_bottom.place(relx = 0.15, rely = 0.55, relwidth = 0.7, relheight = 0.1)

city1 = Entry(frame_top)
city1.pack()

btn = Button(frame_top, text = 'Просмотр погоды', command = weather)
btn.pack()

info = Label(frame_bottom, text = 'Информация')
info.pack()

root.mainloop()