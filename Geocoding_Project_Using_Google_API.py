import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = 'XXXXXXXXXXXXXXXX'		# Enter "Google Places API Key" Here (https://developers.google.com/maps/documentation/geocoding/intro)
serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter Location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving...')
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    #print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failed To Retrieve ====')
        print(data)
        continue

    #print(json.dumps(js, indent=4))
    placeid = js['results'][0]['place_id']
    print('Place ID:', placeid)
    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    print('Latitude:', lat, 'Longitude:', lng)
    location = js['results'][0]['formatted_address']
    print(location)