import requests
import json

api_telegram = '1632251448:AAGAbnBu-9K02mU4R0NbYRSJuOkC337nnSs'
appid = '7a821860997f24e331f7261c75bb9ec9'
url_weather = 'http://api.openweathermap.org/weather/2.5/weather'

def handler(event, context):
    body = json.loads(event['body'])
    chat_id = body['message']['from']['id']
    text = body["message"]["text"]

    response = "Введите /start"
 
    if "/start" in text:
        response = "Привет ! Чтобы ознакомиться введите /help."
    else:
        if "/help" in text:
            response = "/weather - погода в твоем городе"
        else:
            if "/weather" in text:
                response = ("Введите название города")
            else:
                response = weather_city(text)
    send_message(chat_id,response)
    
def weather_city(city_name):
    weather = requests.get("http://api.openweathermap.org/data/2.5/weather", params={'q': city_name, 'units': 'metric', 'lang': 'ru', 'APPID': appid}).json()
    response = ("В городе " + str(weather["name"]) + " температура " + str(float(weather["main"]['temp'])) + "\n" + 
				"Максимальная температура " + str(float(weather['main']['temp_max'])) + "\n" + 
				"Минимальная температура " + str(float(weather['main']['temp_min'])) + "\n" + 
				"Скорость ветра " + str(float(weather['wind']['speed'])) + "\n" + 
				"Давление " + str(float(weather['main']['pressure'])) + "\n" + 
				"Влажность " + str(int(weather['main']['humidity'])) + "%" + "\n" + 
				"Видимость " + str(weather['visibility']) + "\n" + 
				"Описание " + str(weather['weather'][0]["description"]) + "\n\n")
    print(weather)
    return response


   
def send_message(chat_id, text):
    url = 'https://api.telegram.org/bot' + api_telegram + '/' + 'sendMessage'
    weather = {"text": text, "chat_id": chat_id}
    requests.post(url, weather)
