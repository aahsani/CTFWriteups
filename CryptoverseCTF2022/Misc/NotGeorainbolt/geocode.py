import reverse_geocode
coordinates = (-37.81, 144.96),
print(reverse_geocode.search(coordinates)[0]["city"].lower())
