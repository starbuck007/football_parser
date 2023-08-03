import requests
import json
import pymysql
import os.path


con = pymysql.connect(host='localhost', user='root', password='', db='football', cursorclass=pymysql.cursors.DictCursor)
cur = con.cursor()

url = "https://api-football-v1.p.rapidapi.com/v3/venues"

querystring = {"country":"England"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "rapidapi_token"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

data = json.loads(response.text)

venues = data['response']

cur.execute('TRUNCATE TABLE `venues`')

for venue in venues:

    if venue['image'] is None:
        img = ''

    else:
        img = venue['image'].split('/')[-1]

        if not os.path.isfile('img/venues/' + img):
            img_data = requests.get(venue['image'], allow_redirects=True).content
            with open('img/venues/' + img, 'wb') as handler:
                handler.write(img_data)

    cur.execute(
        """INSERT INTO `venues` 
        (
            `id`,
            `name`,
            `address`,
            `city`,
            `country`,
            `capacity`,
            `surface`,
            `image`,
            `img`
        ) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)""", (venue['id'], venue['name'], venue['address'], venue['city'], venue['country'], venue['capacity'], venue['surface'], venue['image'], img))

con.commit()

con.close()
