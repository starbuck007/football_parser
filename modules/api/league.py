from modules.api.query import query
import modules.cache.cache as cache

def get_leagues():
    data = cache.load('league.txt')

    if not data:
        print('load from api')
        data = query("https://api-football-v1.p.rapidapi.com/v3/leagues")
        cache.save('league.txt', data)

    return data