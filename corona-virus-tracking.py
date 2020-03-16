import requests
import json
from subprocess import *
import time

url = 'http://api.kawalcorona.com'
response = requests.get(url)
konten = response.content
encodeKonten = konten.decode("utf-8")
jsonLoad = json.loads(encodeKonten)
slices = jsonLoad[0]
ambilWaktuKejadian = jsonLoad[1]['attributes']['Last_Update']
strStamp = str(ambilWaktuKejadian)
slicesnya  = strStamp[:10]
intSlices = int(slicesnya)
timeStamp = time.ctime(intSlices)
print(timeStamp)
# print(timeStamp)


# print(ambilWaktuKejadian)