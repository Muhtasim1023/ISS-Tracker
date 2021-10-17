import requests as rq
import time


while(True):
    response = rq.get("http://api.open-notify.org/iss-now.json").json()
    longitude = float(response["iss_position"]["longitude"])
    latitude = float(response["iss_position"]["latitude"])
    print(longitude,",",latitude)
    time.sleep(1)



