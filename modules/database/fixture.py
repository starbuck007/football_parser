import modules.database.db_connect as db

def exist(fixture_id):

    con, cur = db.connect()

    res = cur.execute("SELECT `id` FROM `fixtures` WHERE `id` = %s", fixture_id)

    con.close()

    if res > 0:
        return True

    return False


def insert(fixture, season_id):

    con, cur = db.connect()

    if exist(fixture['fixture']['id']):
        return False

    cur.execute(

        """INSERT INTO `fixtures` 
        (
        `id`, 
        `referee`, 
        `timezone`, 
        `date`, 
        `timestamp`, 
        `period_first`, 
        `period_second`, 
        `venue_id`,
        `status_long`,
        `status_short`,
        `status_ elapsed`,
        `league_id`,
        `season_id`,
        `round`,
        `team_id_home`,
        `team_id_away`,
        `team_winner_home`,
        `team_winner_away`,
        `goal_home`,
        `goal_away`,
        `score_halftime_home`,
        `score_halftime_away`,
        `score_fulltime_home`,
        `score_fulltime_away`,
        `score_extratime_home`,
        `score_extratime_away`,
        `score_penalty_home`,
        `score_penalty_away`
        ) 

        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
        %s, %s, %s)""",

        (
            fixture['fixture']['id'],
            fixture['fixture']['referee'],
            fixture['fixture']['timezone'],
            fixture['fixture']['date'],
            fixture['fixture']['timestamp'],
            fixture['fixture']['periods']['first'],
            fixture['fixture']['periods']['second'],
            fixture['fixture']['venue']['id'],
            fixture['fixture']['status']['long'],
            fixture['fixture']['status']['short'],
            fixture['fixture']['status']['elapsed'],
            fixture['league']['id'],
            season_id,
            fixture['league']['round'],
            fixture['teams']['home']['id'],
            fixture['teams']['away']['id'],
            fixture['teams']['home']['winner'],
            fixture['teams']['away']['winner'],
            fixture['goals']['home'],
            fixture['goals']['away'],
            fixture['score']['halftime']['home'],
            fixture['score']['halftime']['away'],
            fixture['score']['fulltime']['home'],
            fixture['score']['fulltime']['away'],
            fixture['score']['extratime']['home'],
            fixture['score']['extratime']['away'],
            fixture['score']['penalty']['home'],
            fixture['score']['penalty']['away']
        )

    )

    con.commit()

    con.close()

    return True
