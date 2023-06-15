from modules.api.query import query
import modules.cache.cache as cache

def get_venue(id):
    querystring = {"id": id}
    data = cache.load('venue-' + id + '.txt')

    if not data:
        print('load from api')
        data = query("https://api-football-v1.p.rapidapi.com/v3/venues", querystring)
        cache.save('venue-' + id + '.txt', data)

    return data