from modules.api.query import query
import modules.cache.cache as cache

def get_countries():
    data = cache.load('country.txt')

    if not data:
        print('load from api')
        data = query("https://api-football-v1.p.rapidapi.com/v3/countries")
        cache.save('country.txt', data)

    return data