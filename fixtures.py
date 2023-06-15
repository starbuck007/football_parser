import modules.api.fixture as api_fixture
import modules.api.venue as api_venue

import modules.database.fixture as db_fixture
import modules.database.venue as db_venue
import modules.database.season as db_season


seasons = db_season.get_active(['2020'])

for season in seasons:

    year = season['year']
    league = season['league_id']

    fixtures = api_fixture.get_fixtures(year, league)

    for fixture in fixtures:

        season_id = db_season.get_id(league, year)

        db_fixture.insert(fixture, season_id)

        if not db_venue.exist(fixture['fixture']['venue']['id']):
            venue = api_venue.get_venue(fixture['fixture']['venue']['id'])
            db_venue.insert(venue['response'][0])


        break





