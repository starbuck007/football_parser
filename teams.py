import modules.api.team as api_team
import modules.database.team as db_team
import modules.database.season as db_season
import modules.database.season_team as db_season_team
import modules.database.country as db_country
import modules.database.venue as db_venue
import modules.file.file as file

seasons = db_season.get_active(['2021', '2020'])

for season in seasons:

    year = season['year']
    league = season['league_id']

    teams = api_team.get_teams(year, league)

    for team in teams:

        season_id = db_season.get_id(league, year)

        country_id = db_country.get_id_by_name(team['team']['country'])

        team['filename'] = file.get_filename_by_url(team['team']['logo'])

        file.download(team['team']['logo'], 'img/teams/')

        db_season_team.insert(team['team']['id'], season_id)

        db_team.insert(team, country_id)

        team['venue']['filename'] = file.get_filename_by_url(team['venue']['image'])

        file.download(team['venue']['image'], 'img/venues/')

        db_venue.insert(team['venue'])
