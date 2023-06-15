from modules.api.query import query
import modules.cache.cache as cache


def get_timezones():
    data = cache.load('timezone.txt')

    if not data:
        print('timezone load from api')
        data = query("https://api-football-v1.p.rapidapi.com/v3/timezone")
        cache.save('timezone.txt', data)

    return data
