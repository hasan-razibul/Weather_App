from flask import Flask, render_template, request
import requests

app = Flask(__name__)





@app.route("/", methods=["GET", "POST"])
def weather():
    if request.method == "POST":
        city = request.form["city"]

        BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
        API_KEY = open('api_key', 'r').read()
        CITY = city

        url = BASE_URL + 'q=' + CITY + '&' + 'units=metric' + "&" + '&appid=' + API_KEY

        response = requests.get(url).json()

        name = response['name']
        timezone = response['timezone']
        description = response['weather'][0]['description']
        temp = response['main']['temp']
        feels_like = response['main']['feels_like']
        temp_max = response['main']['temp_max']
        temp_min = response['main']['temp_min']
        pressure = response['main']['pressure']
        humidity = response['main']['humidity']
        sunrise = response['sys']['sunrise']
        sunset = response['sys']['sunset']

        return render_template("weather.html",
                               name= name,
                               description= description,
                               temp= temp,
                               feels_like= feels_like,
                               temp_max= temp_max,
                               temp_min= temp_min,
                               humidity=humidity,
                               pressure= pressure
                               )
    else:
        return render_template("weather.html")


if __name__ == "__main__":
    app.run(debug=True)
