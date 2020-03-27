import requests

print ('*******************************************')
print ('Welcome to IP / Location Weather Program')

req = requests.get ('https://ipinfo.io/')
data = req.json ()

location = data ['loc']. split (',')
y = position [0]
x = position [1]

api = 'http://api.openweathermap.org/data/2.5/weather?lat='+ y +' & lon = '+ x +' & lang = en & appid = cc37d1a66f03014918464a4a34eb2e00 & units = metric '
req = requests.get (api)
data = req.json ()

temperature = data ['main'] ['temp']
uhava = data ['weather'] [0] ['description']
location = data ['sys'] ['country']
city = data ['name']

print ('Your Location: {} - {}'. format (location, city))
print ('Temperature: {} ° C'.format (temperature))
print ('Weather: {}'. format (uhava))
print ('*******************************************')
