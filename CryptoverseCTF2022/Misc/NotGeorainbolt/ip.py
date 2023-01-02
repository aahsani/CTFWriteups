import requests

ip = "39.110.142.79"
ip = "132.128.187.56"
ip = "125.92.43.82"
#response = requests.get(f"https://geolocation-db.com/json/{ip}&position=true").json()

#print(response)

import geocoder
print(geocoder.ip(ip).city.lower())