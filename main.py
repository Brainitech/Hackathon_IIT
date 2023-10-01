import uagents
import requests
import json
import pandas
import time


sleep = time.sleep
# API Key from openweathermap.org
API_KEY = '7b2931324d4376e5420c3225115822a9'

#default values
dmin_temp = float(16)
dmax_temp = float(35)

tdf = input("Use default values? [Y/n]:")

if tdf.upper() == 'N':
    # User preferenes
    # Min Temp
    for i in range(5):
        try:
            min_temp = float(input("Enter the minimum temperature (in Celsius): "))
        except ValueError:
            print("Enter a Numeric value")
        else:
            print("Sucessfully recorded user input. Min Temp =",min_temp,"°C")
            break
    else: #if failed to get user input
        print("Failed to record user inpdfut. Taking Default value of",dmin_temp,"°C")

    #Max Temp
    for i in range(5):
        try:
            for i in range(5):    
                max_temp = float(input("Enter the maximum temperature (in Celsius): "))  
                if max_temp < min_temp:
                    print("Maximum temperature can not be less than the minimum temparature, try a different value.")
                else:
                    break
            else: 
                max_temp = dmax_temp
                print("Failed to record user input. Taking Default value of",dmax_temp,"°C")
            break                          
        except ValueError:
            print("Enter a numeric value")
        else:
            print("Successfully recorded user input. Max Temp =",max_temp,"°C")
            break
    else: #if failed to get user input
        print("Failed to record user input. Taking Default value of",dmax_temp,"°C")
else:
    max_temp = dmax_temp
    min_temp = dmin_temp
    print("Taking Default Values.") 

#location
location = input("Enter your desired location (city name or coordinates): ")

 # Fetch weather data
url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=metric"
response = requests.get(url)
weather_data = json.loads(response.content)
current_temp = weather_data['main']['temp']

 # Check temperature range
if current_temp < min_temp:
    alert_message = f"Alert: Temperature in {location} is below {min_temp}°C ({current_temp}°C)."
elif current_temp > max_temp:
    alert_message = f"Alert: Temperature in {location} is above {max_temp}°C ({current_temp}°C)."
else:
    alert_message = f"Temperature in {location} is within the preferred range."

 # Send alert/notification
print(alert_message)
