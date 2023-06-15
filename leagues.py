import modules.api.league as api
import modules.file.file as file
import modules.database.country as db_country
import modules.database.league as db_league
import modules.database.season as db_season

leagues = api.get_leagues()

for league in leagues:

    league['filename'] = file.get_filename_by_url(league['league']['logo'])

    file.download(league['league']['logo'], 'img/leagues/')

    country_id = db_country.get_id_by_name(league['country']['name'])

    db_league.insert(league, country_id)

    for season in league['seasons']:

        db_season.insert(season, league['league']['id'])

db_league.set_active(['39', '78', '135', '140'])
