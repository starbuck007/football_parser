import modules.database.db_connect as db

def exist(team_id):

    con, cur = db.connect()

    res = cur.execute("SELECT `id` FROM `teams` WHERE `id` = %s", team_id)

    con.close()

    if res > 0:
        return True

    return False


def insert(team, country_id):

    con, cur = db.connect()

    if exist(team['team']['id']):
        return False

    cur.execute(

        """INSERT INTO `teams` 
        (
        `id`, 
        `name`, 
        `country_id`, 
        `founded`, 
        `national`, 
        `logo`, 
        `logo_name`, 
        `venue_id`
        ) 
    
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""",

        (
            team['team']['id'],
            team['team']['name'],
            country_id,
            team['team']['founded'],
            team['team']['national'],
            team['team']['logo'],
            team['filename'],
            team['venue']['id']
        )

    )

    con.commit()

    con.close()

    return True




