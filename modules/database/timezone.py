import modules.database.db_connect as db


def exist(timezone):
    con, cur = db.connect()

    res = cur.execute("SELECT `name` FROM `timezones` WHERE `name` = %s", timezone)

    con.close()

    if res > 0:
        return True

    return False


def insert(timezone):
    con, cur = db.connect()

    if exist(timezone):
        return False

    cur.execute("INSERT INTO `timezones` (`name`) VALUES (%s)", timezone)

    timezone_id = con.insert_id()

    con.commit()
    con.close()

    return timezone_id
