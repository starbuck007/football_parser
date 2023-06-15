import modules.api.fixture as af
import modules.api.team as at

import modules.database.league as bl
import modules.database.fixture as bf
import modules.database.season as bs
import modules.database.team as bt
import modules.database.venue as bv
import modules.database.country as bc


import modules.file.file as f


def get_data_by_date(date):
    data = af.get_data_by_date(date)
    return data


def get_active_league():
    rows = bl.get_active()
    return rows


def insert_fixture(fixture):
    season_id = bs.get_id(fixture['league']['id'],fixture['league']['season'])
    bf.insert(fixture, season_id)

    for team_id in [fixture['teams']['home']['id'], fixture['teams']['away']['id']]:

        if not bt.exist(team_id):
            team = at.get_team_by_id(team_id)

            country_id = bc.get_id_by_name(team[0]['team']['country'])

            team[0]['filename'] = f.get_filename_by_url(team[0]['team']['logo'])
            f.download(team[0]['team']['logo'], 'img/teams/')

            bt.insert(team[0], country_id)

            if not bv.exist(team[0]['venue']['id']):

                team[0]['venue']['filename'] = f.get_filename_by_url(team[0]['venue']['image'])
                f.download(team[0]['venue']['image'], 'img/venues/')

                bv.insert(team[0]['venue'])








    return True

