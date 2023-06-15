import modules.api.timezone as api
import modules.database.timezone as db_t

timezones = api.get_timezones()

for timezone in timezones:
    db_t.insert(timezone)
    print(timezone)
    break
