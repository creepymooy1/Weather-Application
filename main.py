# Hey Atticus, I know you didn't fully accept my bounty request, but this looked like a fun little project I could throw together and I was bored, lol. Feel free to either accept my bounty, or if this isn't what you had in mind you can also accept someone else. Hope this helps! :D

# Setup instructions: Get a free API key from https://openweathermap.org/api, then install packages using 'pip install flask'. After running the python script (make sure templates folder is in the root directory of main.py's location), your web app will be available at 127.0.0.1:5000. You can also implement into any website as necessary.

import requests
from flask import Flask, render_template, request

# API key for OpenWeatherMap API
api_key = "706277cdaa0945527284e5a35484bf29"

# base URL for OpenWeatherMap API
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# create a Flask app
app = Flask(__name__)

@app.route("/weather", methods=["POST"])
def weather():
    city = request.form["city"]
    weather_data = get_weather_data(city)
    if weather_data["cod"] != "404" and 'main' in weather_data:
        # retrieve weather information from API response
        temperature = round(weather_data["main"]["temp"] - 273.15, 2)
        description = weather_data["weather"][0]["description"]
        humidity = weather_data["main"]["humidity"]
        wind_speed = weather_data["wind"]["speed"]
        # render weather information
        return render_template("weather.html",
                               temperature=temperature,
                               description=description,
                               humidity=humidity,
                               wind_speed=wind_speed,
                               city=city)
    elif weather_data["cod"] == "404":
        error_message = "City not found."
        # render error message
        return render_template("error.html", error=error_message)
    else:
        error_message = "Unexpected API response."
        # render error message
        return render_template("error.html", error=error_message)

# define a route to accept user input and display weather information
@app.route("/", methods=["GET", "POST"])
def weather_info():
    if request.method == "POST":
        city_name = request.form["city"]
        weather_data = get_weather_data(city_name)
        if weather_data["cod"] != "404" and 'main' in weather_data:
            # retrieve weather information from API response
            temperature = round(weather_data["main"]["temp"] - 273.15, 2)
            description = weather_data["weather"][0]["description"]
            humidity = weather_data["main"]["humidity"]
            wind_speed = weather_data["wind"]["speed"]
            # render weather information
            return render_template("weather.html",
                                   temperature=temperature,
                                   description=description,
                                   humidity=humidity,
                                   wind_speed=wind_speed,
                                   city=city_name)
        elif weather_data["cod"] == "404":
            error_message = "City not found."
            # render error message
            return render_template("error.html", error=error_message)
        else:
            error_message = "Unexpected API response."
            # render error message
            return render_template("error.html", error=error_message)
    # render the initial form
    return render_template("form.html")

# function to get weather data for a given city
def get_weather_data(city_name):
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    data = response.json()
    return data

if __name__ == "__main__":
    app.run(debug=True)

