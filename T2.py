#This python program commicates with the openweatherapp API in which we request the weather from a city we request
import argparse
import math
import requests#Used for HTTP request
#Used for env files and the variables it stores
import os
from dotenv import load_dotenv
load_dotenv()

def call_API(city, id): #Returns JSON of HTTP Request From OpenWeather API/URL
    #URL known as Endpoint will connect to the API if theres internet avaliable. - This can be run on IDE with requests library
    url = "https://api.openweathermap.org/data/2.5/weather"
    para = {"q": city, "appid": id}

    #Get HTTPs object by requesting and store it in response
    response = requests.get(url, params=para)
    
    #Check if response was given properly
    if response.status_code == 200:
        return response.json()
    else:
        print("Something went wrong...\n")
        exit()

#==================================================================================================== Variables/Parameters

#Command Line Interface - Parser Object that Reads from CLI
parser = argparse.ArgumentParser(usage="T1.py [-h] city")
parser.add_argument("city",help="Name of City | Use - for space if any")

#Args - Gets all the arguments from Parser
args = parser.parse_args()

#Check API later to see how to format city name
current_city = args.city
id = os.getenv("API_KEY_OPENWEATHER")

#Format City Name for API request
current_city = current_city.replace("-"," ")
if any(char.isdigit() for char in current_city):
    print("The string contains numbers.")
    exit()

current_city = current_city.lower().capitalize()

#==================================================================================================== Function Call - Result
#Once city has been given / API ID is valid = Request to the server
data = call_API(current_city, id)

#Set Variables
# Extract the temperature in Kelvin
temp_k = data['main']['temp']

# Convert to Celsius and Fahrenheit
temp_c = temp_k - 273.15
temp_f = temp_c * 1.8 + 32

# Print the weather condition and temperatures
print(f"The weather in {data['name']} is {data['weather'][0]['description']} with a temperature of {temp_c:.2f} °C / {temp_f:.2f} °F.")

exit()


