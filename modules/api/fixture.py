from modules.api.query import query
import modules.cache.cache as cache

def get_fixtures(year, league):
    querystring = {"league": league,"season": year}
    data = cache.load('fixture-' + str(league) + '-' + str(year) + '.txt')

    if not data:
        print('load from api')
        data = query("https://api-football-v1.p.rapidapi.com/v3/fixtures", querystring)
        cache.save('fixture-' + str(league) + '-' + str(year) + '.txt', data)

    return data

def get_day(date, year, league):

    querystring = {"date": date, "league": league, "season": year}
    data = cache.load('fixture_' + str(league) + '_' + str(date) + '.txt')
    #print('load from file')

    if not data:
        print('load from api')
        data = query("https://api-football-v1.p.rapidapi.com/v3/fixtures", querystring)
        cache.save('fixture_' + str(league) + '_' + str(date) + '.txt', data)

    return data

def get_data_by_date(date):

    data = cache.load('fixture_' + str(date) + '.txt')

    if data:
        print('load fixtures from file: ' + 'fixture_' + str(date) + '.txt')
    else:
        querystring = {"date": date}
        data = query("https://api-football-v1.p.rapidapi.com/v3/fixtures", querystring)
        cache.save('fixture_' + str(date) + '.txt', data)
        print('load fixtures from api, ' + date)

    return data
