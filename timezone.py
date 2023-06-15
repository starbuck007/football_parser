import modules.api.timezone as api
import modules.database.timezone as db


def add():
    timezones = api.get_timezones()

    for timezone in timezones:
        db.insert(timezone)