import modules.database.db_connect as db_connect

def get_active(years):

    con, cur = db_connect.connect()

    cur.execute("""
        SELECT `year`,`league_id` 
        FROM `seasons` 
        WHERE `league_id` in (SELECT `id` FROM `leagues` WHERE `active` = 1) AND `year` in %s""", [years])

    rows = cur.fetchall()

    con.close()

    return rows


def insert(season, league):

    con, cur = db_connect.connect()

    cur.execute("""
    
        INSERT INTO `seasons` 
    
        (
            `year`, 
            `start`, 
            `end`, 
            `current`, 
            `events`, 
            `lineups`, 
            `statistics_fixture`, 
            `statistics_players`, 
            `standings`, 
            `players`, 
            `top_scorers`, 
            `top_assists`, 
            `top_cards`, 
            `injuries`, 
            `predictions`, 
            `odds`, 
            `league_id`
        ) 

        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",

            (
                season['year'],
                season['start'],
                season['end'],
                season['current'],
                season['coverage']['fixtures']['events'],
                season['coverage']['fixtures']['lineups'],
                season['coverage']['fixtures']['statistics_fixtures'],
                season['coverage']['fixtures']['statistics_players'],
                season['coverage']['standings'],
                season['coverage']['players'],
                season['coverage']['top_scorers'],
                season['coverage']['top_assists'],
                season['coverage']['top_cards'],
                season['coverage']['injuries'],
                season['coverage']['predictions'],
                season['coverage']['odds'],
                league

            )

                )

    con.commit()

    con.close()

    return True


def get_id(league, year):

    con, cur = db_connect.connect()

    cur.execute("SELECT `id` FROM `seasons` WHERE `league_id` = %s and `year` = %s", (league, year))

    row = cur.fetchone()

    con.close()

    return row['id']
