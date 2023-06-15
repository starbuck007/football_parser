import modules.database.db_connect as db

def insert(venue):

    con, cur = db.connect()

    if exist(venue['id']):
        return False

    cur.execute(

        """INSERT INTO `venues` 
        (
        `id`, 
        `name`, 
        `address`, 
        `city`, 
        `capacity`, 
        `surface`, 
        `image`, 
        `image_name`
        ) 

        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""",

        (
            venue['id'],
            venue['name'],
            venue['address'],
            venue['city'],
            venue['capacity'],
            venue['surface'],
            venue['image'],
            venue['filename']
        )

    )

    con.commit()

    con.close()

    return True


def exist(venue_id):

    con, cur = db.connect()

    res = cur.execute("SELECT `id` FROM `venues` WHERE `id` = %s", venue_id)

    con.close()

    if res > 0:
        return True

    return False
