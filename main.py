import requests
import datetime

x = requests.get('https://localmonero.co/blocks/api/get_stats')
x = x.json()["last_timestamp"]
x = datetime.datetime.fromtimestamp(x)
print(x)