import os 
import requests as rq
import json as js

print("**  Welcome to Weather App  **\n")

city = input("Enter a city: ")
api = input('Enter your api key: ')
options = int(input('What do you want to know\n1. Temperature(C/F)\n2. Wind Speed(kph/mph)\n3. Humidity\n4. Precipitation\n:=='))
url = f"https://api.weatherapi.com/v1/current.json?key={api}&q={city}"

response = rq.get(url)
tDic = js.loads(response.text)
if options == 1:
    res = f'The Temperature is {tDic["current"]["temp_c"]} in {tDic["location"]["name"]}, {tDic["location"]["region"]}'
elif options == 2:
    res = f'The Wind Speed is {tDic["current"]["wind_mph"]} in {tDic["location"]["name"]}, {tDic["location"]["region"]}'
elif options == 3:
    res = f'The Humidity is {tDic["current"]["humidity"]} in {tDic["location"]["name"]}, {tDic["location"]["region"]}'
elif options == 4:
    res = f'The Precipitation is {tDic["current"]["precip_mm"]} in {tDic["location"]["name"]}, {tDic["location"]["region"]}'

os.system(f"espeak '{res}'")