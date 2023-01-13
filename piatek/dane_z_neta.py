import json

import requests as requests

# response = requests.get('http://api.weatherapi.com/v1/current.json?key=d863af85e8fa43618f682810220812&q=Kielce&aqi=no')
# dane = response.json()
#
# dane_to_json = json.dumps(dane)
# print(dane_to_json)
#
#
# with open('pogoda.json', 'w') as f:
#     f.write(str(dane_to_json))

with open('pogoda.json', 'r') as f:
    pogoda = json.load(f)

miasto = pogoda['location']['name']
wiatr = pogoda['current']['wind_dir']
code = pogoda['current']['condition']['code']

print(f'W mieście {miasto} wieje wiatr z kierunku {wiatr}, kod pogody to {code}')
print(type(miasto))
print(type(wiatr))
print(type(code))