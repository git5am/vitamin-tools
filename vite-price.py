import requests
import json
import time
import datetime

i = 0

while i <= 10:
# defining vitex api
    url = "https://vitex.vite.net/api/v1/exchange-rate?tokenSymbols=VITE"
# connecting to the api
    response = requests.get(url)
# defining time
    localtime = time.asctime( time.localtime(time.time()) )
    print("<===============Made by:5am===============>")
# setting up parsing
    response = requests.get(url)
    data = response.text
    parsed = json.loads(data)
    data = parsed["data"]
    type(data)
    usdRate = data[0]['usdRate']
    time.sleep(1)
    # printing VITC value!
    print("VITE's price @ " + str(localtime) + " is $" + str(usdRate))
