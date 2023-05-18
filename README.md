# Weather Web Application

This Python script sets up a simple web application using Flask to display weather information for a given city. It utilizes the OpenWeatherMap API to fetch weather data based on user input.

## Setup Instructions

To set up and run the weather web application, follow these steps:

1. Get a free API key from [OpenWeatherMap](https://openweathermap.org/api).
2. Install the required packages by running the following command:

`pip install flask requests`


3. Place the `templates` folder in the root directory of the `main.py` file.
4. Open the `main.py` file in a text editor and replace `"706277cdaa0945527284e5a35484bf29"` with your OpenWeatherMap API key (`api_key` variable).
5. Run the Python script by executing the following command:

`python main.py`


The web app will be available at [http://127.0.0.1:5000](http://127.0.0.1:5000).

6. Use the web app to search for weather information by entering the name of a city in the provided form.

7. The web app will display the temperature, description, humidity, and wind speed for the specified city if the data is available. Otherwise, it will display an error message.

## Usage

- Access the web app by opening a web browser and navigating to [http://127.0.0.1:5000](http://127.0.0.1:5000).
- Enter the name of a city in the provided form and submit the form.
- The web app will retrieve weather data from the OpenWeatherMap API and display the temperature, description, humidity, and wind speed for the specified city.
- If the entered city is not found or if there is an unexpected API response, an error message will be displayed.
