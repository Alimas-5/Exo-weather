import dotenv
import os
import web
import requests
dotenv.load_dotenv()
API_key = os.environ.get('API_key')
base_url = "http://api.openweathermap.org/data/2.5/weather?"
urls = ('/(.*)', 'weather')
app = web.application(urls, globals())
class weather:
    def GET(self, CP):
     Final_url = base_url + "appid=" + API_key + "&q=" + CP

     weather_data = requests.get(Final_url).json()
     weather_data.get('main').get('temp')
     Meteo = 'meteo : ' + str(weather_data.get('weather')[0].get('main')) + '\ntemp max : ' +str(weather_data.get('main').get('temp_max')) + '\ntemp min : ' + str(weather_data.get('main').get('temp_min')) + '\ntemp actuelle : ' + str(weather_data.get('main').get('temp'))
     return Meteo

if __name__ == "__main__":
    app.run()

