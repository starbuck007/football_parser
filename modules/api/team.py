from modules.api.query import query
import modules.cache.cache as cache

def get_teams(year, league):
    querystring = {"league": league,"season": year}
    data = cache.load('team-' + str(league) + '-' + str(year) + '.txt')

    if not data:
        print('load from api')
        data = query("https://api-football-v1.p.rapidapi.com/v3/teams", querystring)
        cache.save('team-' + str(league) + '-' + str(year) + '.txt', data)

    return data

def get_team_by_id(id):
    querystring = {"id": id}
    data = cache.load('team-' + str(id) + '.txt')

    if not data:
        print('load from api')
        data = query("https://api-football-v1.p.rapidapi.com/v3/teams", querystring)
        cache.save('team-' + str(id) + '.txt', data)

    return data






