import datetime
import modules.database.season as db_season
import modules.api.fixture as api_fixture
import modules.database.fixture as db_fixture
import modules.database.team as db_team
import modules.api.team as api_team
import modules.database.country as db_country
import modules.database.venue as db_venue
import modules.file.file as file

yesterday = datetime.datetime.utcnow().date() - datetime.timedelta(days=1)

year = yesterday.year

leagues = db_season.get_active([year])

team_ids = []

api_fixture.get_day('2021-04-07')

for league in leagues:
    league = league['league_id']

    fixtures = api_fixture.get_day(yesterday, year, league)

    for fixture in fixtures:

        season_id = db_season.get_id(league, year)

        # db_fixture.insert(fixture, season_id)

        print(fixtures)

        team_ids.extend((fixture['teams']['home']['id'], fixture['teams']['away']['id']))

        print(team_ids)

team_ids = []

for team_id in team_ids:
    if not db_team.exist(team_id):

        team = api_team.get_team_by_id(team_id)

        country_id = db_country.get_id_by_name(team[0]['team']['country'])

        team[0]['filename'] = file.get_filename_by_url(team[0]['team']['logo'])

        file.download(team[0]['team']['logo'], 'img/teams/')

        db_team.insert(team[0], country_id)



        if not db_venue.exist(team[0]['venue']['id']):
        
            team[0]['venue']['filename'] = file.get_filename_by_url(team[0]['venue']['image'])

            file.download(team[0]['venue']['image'], 'img/venues/')

            db_venue.insert(team[0]['venue'])
            















