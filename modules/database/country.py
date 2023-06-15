import modules.database.db_connect as db


def find(country_name):
    country_id = False
    con, cur = db.connect()
    res = cur.execute("SELECT `id` FROM `countries` WHERE `name` = %s", country_name)

    if res:
        row = cur.fetchone()
        country_id = row['id']

    con.close()

    return country_id


def insert(country):
    con, cur = db.connect()

    if find(country['name']):
        return False

    cur.execute("INSERT INTO `countries` (`name`, `code`, `flag`, `img`) VALUES (%s, %s, %s, %s)",
                (country['name'], country['code'], country['flag'], country['filename']))

    country_id = con.insert_id()

    con.commit()

    con.close()

    return country_id


#  заменить на функцию find
def get_id_by_name(country_name):
    con, cur = db.connect()

    cur.execute("SELECT `id` FROM `countries` WHERE `name` = %s", country_name)

    con.commit()

    row = cur.fetchone()

    con.close()

    return row['id']


def set_active(country_names):
    con, cur = db.connect()

    cur.execute("UPDATE `countries` SET `active` = 1 WHERE `name` in %s", [country_names])

    con.commit()

    con.close()

    return True
