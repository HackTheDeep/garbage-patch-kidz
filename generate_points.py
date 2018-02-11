import random
import json

longitudes = []
latitudes = []

for i in range(500):
    longitudes.append(float(random.randrange(13500, 15500)) / 100)
    latitudes.append(float(random.randrange(3500, 4200)) / 100)

data = {
    "longitudes": longitudes,
    "latitudes": latitudes
}

f = open('particles.json', 'w')
f.write(json.dumps(data))
f.close()
