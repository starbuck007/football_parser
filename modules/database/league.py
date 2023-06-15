import modules.database.db_connect as db

def insert(league, country_id):

    con, cur = db.connect()

    cur.execute(

                    """INSERT INTO `leagues` 
                        (
                        `id`, 
                        `name`, 
                        `type`, 
                        `logo`, 
                        `img`, 
                        `country_id`
                        ) 
                        
                    VALUES (%s, %s, %s, %s, %s, %s)""",

                    (
                        league['league']['id'],
                        league['league']['name'],
                        league['league']['type'],
                        league['league']['logo'],
                        league['filename'],
                        country_id
                    )

                )

    con.commit()

    con.close()

    return True


def set_active(league_ids):

    con, cur = db.connect()

    cur.execute("UPDATE `leagues` SET `active` = 1 WHERE `id` in %s", [league_ids])

    con.commit()

    con.close()

    return True

def get_active():
    con, cur = db.connect()
    cur.execute("SELECT `id` FROM `leagues` WHERE `active` = 1")
    rows = cur.fetchall()
    con.close()

    ids = []

    for row in rows:
        ids.append(row['id'])

    return ids