import mysql.connector

# LIST OF FUNCTIONS
# sql_connect ()
# add_event (name, date, time)
# add_participant (p_id, name, email, phone)
# add_user (name, email, phone, passw, perm)
# add_reg (p_id, event_id)
# get_event_id (name)
# get_events ()
# get_user ()
# get_reg (p_id, event_id)
# get_pid (phone)
# remove_event (name, date, time)
# get_report ()
# mark_entry (p_id, event_id)
# check_part (p_id)


def sql_connect():
    """
    Make a connection to the database.

    :return: database name, Cursor object of database, connector of database.
    """

    # mydb = mysql.connector.connect(
    #     host="KKSJminorproject.mysql.pythonanywhere-services.com",
    #     user="KKSJminorproject",
    #     password="mpdbkksj"
    # )

    try:
        mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="minor",
            password="1234"
        )
    except:
        mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="pass"
        )
    mycursor = mydb.cursor()
    db_name = "minor_db"
    return db_name, mycursor, mydb


def add_event(name: str, date: str, time: str) -> int:
    """
    Command database to add an event.

    :param name: Name of event.
    :param date: Date of event.
    :param time: Time of event.
    :return: "1" success, "0" event name exists.
    """

    db_name, mycursor, mydb = sql_connect()
    mycursor.execute("USE " + db_name)

    # Date "yyyy-mm-dd" Time "hh:mm:ss"
    try:
        sql = "INSERT INTO events (name, date, time) VALUES (%s, %s, %s)"
        val = (name, date, time)
        mycursor.execute(sql, val)

        mydb.commit()
        return 1
    except:
        # Name already exists
        return 0


def add_participant(p_id: str, name: str, email: str, phone: str) -> int:
    """
    Command database to add a new participant.

    :param p_id: Participant ID.
    :param name: Participant name.
    :param email: Participant E-mail ID.
    :param phone: Participant phone number.
    :return: "0" some error, "1" success.
    """

    db_name, mycursor, mydb = sql_connect()
    mycursor.execute("USE " + db_name)

    try:
        sql = "INSERT INTO participants (p_id, name, email_id, phone) VALUES (%s, %s, %s, %s)"
        val = (p_id, name, email, phone)
        mycursor.execute(sql, val)

        mydb.commit()
        return 1
    except:
        # Participant already exists
        return 0


def add_user(name: str, email: str, phone: str, passw: str, perm: int) -> int:
    """
    Command database to add a new user.

    :param name: Name of user.
    :param email: E-mail ID of user.
    :param passw: Hash of password of new user.
    :param phone: Phone number of new user.
    :param perm: Permission level provided to user.
    :return: "1" if added, "0" Error (user already exists).
    """

    db_name, mycursor, mydb = sql_connect()
    mycursor.execute("USE " + db_name)
    phone = str(phone)
    passw = str(passw)

    try:
        sql = "INSERT INTO user (name, email_id, phone, password, permission) VALUES (%s, %s, %s, %s, %s)"
        val = (name, email, phone, passw, perm)
        mycursor.execute(sql, val)

        mydb.commit()
        return 1
    except:
        # E-mail already exists
        return 0


def add_reg(p_id: str, event_id: str) -> int:
    """
    Command database to register a participant in an event.

    :param p_id: Participant ID.
    :param event_id: Event ID.
    :return: "0" some error, "1" success.
    """

    db_name, mycursor, mydb = sql_connect()
    mycursor.execute("USE " + db_name)

    try:
        sql = "INSERT INTO registration (p_id, event_id, present) VALUES (%s, %s, %s)"
        val = (p_id, event_id, 1)
        mycursor.execute(sql, val)
        mydb.commit()
        return 1
    except:
        # p_id or event_id incorrect
        return 0


def get_event_id(name: str) -> int:
    """
    Retrieve event ID from database using the event name.

    :param name: Event name.
    :return: Event ID.
    """

    db_name, mycursor, mydb = sql_connect()
    mycursor.execute("USE " + db_name)

    sql = "SELECT event_id FROM events WHERE name = \"" + name + "\""
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    return myresult


def get_events() -> [str]:
    """
    Retrieve List of events from database.

    :return: List of events.
    """

    db_name, mycursor, mydb = sql_connect()
    mycursor.execute("USE " + db_name)

    mycursor.execute("SELECT name FROM events")
    myresult = mycursor.fetchall()
    return myresult


def get_user() -> [[str]]:
    """
    Retrieve e-mail id, password and permission level of user from database.

    :return: List of e-mail id, password and permission level of all users.
    """

    db_name, mycursor, mydb = sql_connect()
    mycursor.execute("USE " + db_name)

    mycursor.execute("SELECT email_id, password, permission FROM user")
    myresult = mycursor.fetchall()
    return myresult


def get_reg(p_id: str, event_id: str) -> int:
    """
    Retrieve entry detail of a participant in a particular event.

    :param p_id: Participant ID.
    :param event_id: Event ID.
    :return: "1" Not Entered, "2" Entered, "0" Dose not exists.
    """

    db_name, mycursor, mydb = sql_connect()
    mycursor.execute("USE " + db_name)
    event_id = str(event_id)
    try:
        sql = "SELECT present FROM registration WHERE p_id = %s AND event_id = %s"
        val = (p_id, event_id)
        mycursor.execute(sql, val)
        myresult = mycursor.fetchall()
        return myresult[0][0]
    except:
        # Dose not exist
        return 0


def get_pid(phone: str) -> str:
    """
    Retrieve participant id of a participant from phone number.
    :param phone: Phone number of participant.
    :return: Participant ID.
    """

    db_name, mycursor, mydb = sql_connect()
    mycursor.execute("USE " + db_name)
    phone = str(phone)

    mycursor.execute("SELECT p_id FROM participants WHERE phone = " + phone)
    myresult = mycursor.fetchall()
    return myresult[0][0]


def remove_event(name: str, date: str, time: str) -> int:
    """
    Command database to delete an event.

    :param name: Name of event.
    :param date: Date of event.
    :param time: Time of event.
    :return: "1" success, "0" event participant registered, "4" wrong event details.
    """

    db_name, mycursor, mydb = sql_connect()
    mycursor.execute("USE " + db_name)

    # Date "yyyy-mm-dd" Time "hh:mm:ss"
    try:
        sql = "DELETE FROM events WHERE name = %s AND date = %s AND time = %s"
        val = (name, date, time)
        mycursor.execute(sql, val)
        mydb.commit()

        if mycursor.rowcount == 0:
            # no change
            return 4
        return 1
    except:
        # Someone is registered
        return 0


def get_report() -> [[str]]:
    """
    Retrieve participant details and events they registered in from database.

    :return: List of participant details.
    """

    db_name, mycursor, mydb = sql_connect()
    mycursor.execute("USE " + db_name)

    sql = "SELECT `" + db_name + "`.`participants`.*, GROUP_CONCAT(`" + db_name + "`.`events`.name, `" + db_name + "`.`registration`.present) as \"events\" FROM ((`" + db_name + "`.`participants` INNER JOIN `" + db_name + "`.`registration` ON `" + \
        db_name + "`.`participants`.p_id = `" + db_name + "`.`registration`.p_id) INNER JOIN `" + db_name + \
        "`.`events` ON `" + db_name + "`.`events`.event_id = `" + \
        db_name + "`.`registration`.event_id) group by p_id;"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    return myresult


def mark_entry(p_id: str, event_id: str):
    """
    Command database to mark a participant entry in a event.

    :param p_id: Participant ID.
    :param event_id: Event ID.
    """

    db_name, mycursor, mydb = sql_connect()
    mycursor.execute("USE " + db_name)

    sql = "UPDATE `" + db_name + \
        "`.`registration` SET `present` = '2' WHERE p_id = %s AND event_id = %s"
    val = (p_id, event_id)
    mycursor.execute(sql, val)
    mydb.commit()


def check_part(p_id: str) -> int:
    """
    Retrieve all details of participant from database.

    :param p_id: Participant ID.
    :return: List of details of participant.
    """

    db_name, mycursor, mydb = sql_connect()
    mycursor.execute("USE " + db_name)

    sql = "SELECT * FROM participants WHERE p_id = \"" + p_id + "\""
    mycursor.execute(sql)
    mycursor.fetchall()

    return mycursor.rowcount
