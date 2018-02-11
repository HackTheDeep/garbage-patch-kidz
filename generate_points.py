import random
import json

longitudes = []
latitudes = []

for i in range(500):
    longitudes.append(float(random.randrange(20500, 21800)) / 100)
    latitudes.append(float(random.randrange(3300, 4200)) / 100)

data = {
    "longitudes": longitudes,
    "latitudes": latitudes
}

f = open('particles_2.json', 'w')
f.write(json.dumps(data))
f.close()
