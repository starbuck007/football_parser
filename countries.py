import modules.api.country as api
import modules.database.country as db
import modules.file.file as file
import modules.log.log as log


def add():
    countries = api.get_countries()

    added_countries = []

    for country in countries:

        country['filename'] = file.get_filename_by_url(country['flag'])

        file.download(country['flag'], 'img/countries/')

        country_id = db.insert(country)

        if country_id:
            added_countries.append(country)

    action = 'add countries'

    path = '/countries'

    log.add(added_countries, path, action)


def active_country(active_country):

    db.set_active(active_country)

    return True
