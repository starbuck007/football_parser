import modules.database.db_connect as db_connect


def exist(team_id, season_id):
    con, cur = db_connect.connect()

    res = cur.execute(
        """SELECT 
                `team_id`, 
                `season_id` 
                
        FROM `season_team` 
        
        WHERE `team_id` = %s and `season_id` = %s""", (team_id, season_id))

    con.close()

    if res > 0:
        return True

    return False


def insert(team_id, season_id):
    con, cur = db_connect.connect()

    if exist(team_id, season_id):
        return False

    cur.execute(
        """INSERT INTO `season_team`
            (`team_id`,
            `season_id`) VALUES (%s, %s)""", (team_id, season_id))

    con.commit()

    con.close()

    return True
