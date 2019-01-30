import requests

print('*******************************************')
print('IP/Konum Hava Durumu Programina Hosgeldiniz')

req = requests.get('https://ipinfo.io/')
data = req.json()

konum = data['loc'].split(',')
y = konum[0]
x = konum[1]

api = 'http://api.openweathermap.org/data/2.5/weather?lat='+ y +'&lon='+ x +'&lang=tr&appid=cc37d1a66f03014918464a4a34eb2e00&units=metric'
req = requests.get(api)
data = req.json()

sicaklik = data['main']['temp']
uhava = data['weather'][0]['description']
yer = data['sys']['country']
sehir = data['name']

print('Bulundugunuz Konum : {} - {}'.format(yer,sehir))
print('Sicaklik : {}°C'.format(sicaklik))
print('Hava Durumu : {}'.format(uhava))
print('*******************************************')
