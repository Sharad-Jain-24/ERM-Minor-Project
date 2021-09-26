try:
    import Backend.db_operations as db
    import Backend.database as db_init
except:
    import database as db_init
    import db_operations as db

# LIST OF FUNCTIONS
# login (uid, passw)
# add_user (name, email_id, password, phone, perm)
# add_part (p_id, name, e_id, phone, events)
# event_registry (p_id, events)
# add_event (name, date, time)
# get_events ()
# mark_entry (p_id, event_id)
# remove_event (name, date, time)
# get_report ()


def login(uid: str, passw: str) -> int:
    """
    Process the login data for database operation.

    :param uid: User ID.
    :param passw: Hash of password of user.
    :return: "1"/"2" Password match, "0" Wrong password, "-1" User dose not exists.
    """

    try:
        users = db.get_user()
    except:
        db_init.db_init()
        users = db.get_user()

    for i in users:
        if i[0] == uid:
            # User email exists
            if passw == i[1]:
                # "1"/"2" Password match
                return i[2]
            # "0" Wrong password
            return 0
    # "-1" User dose not exists
    return -1


def add_user(name: str, email_id: str, password: str, phone: str, perm: int) -> int:
    """
    Request database to add new user data.

    :param name: Name of user.
    :param email_id: E-mail ID of user.
    :param password: Hash of password of new user.
    :param phone: Phone number of new user.
    :param perm: Permission level provided to user.
    :return: "1" if added, "0" Error (user already exists).
    """

    success = db.add_user(name=name, email=email_id,
                          phone=phone, passw=password, perm=perm)
    # "1" if added, "0" if exists
    return success


def add_part(p_id: str, name: str, email: str, phone: str, events: str) -> int:
    """
    Process participant data to add into database.

    :param p_id: Participant ID.
    :param name: Participant name.
    :param email: Participant E-mail ID.
    :param phone: Participant phone number.
    :param events: List of events in which participant needs to register.
    :return: "0" some error, "1" success, ("2"/"3"/"4") event (1/2/both) registered for this participant.
    """

    if name == "":
        resp = db.check_part(p_id)
        if resp == 0:
            # No registration for this participant
            return 0
    else:
        # Registering participant
        status = db.add_participant(
            p_id=p_id, name=name, email=email, phone=phone)
        if status == 0:
            # User exists
            p_id = db.get_pid(phone)

    # "0" some error, "1" success, ("2"/"3"/"4") event (1/2/both) registered for this participant
    return event_registry(p_id=p_id, events=events)


def event_registry(p_id: str, events: str) -> int:
    """
    Process data to register participant in each event.

    :param p_id: Participant ID.
    :param events: List of events in which participant needs to register.
    :return: "0" some error, "1" success, ("2"/"3"/"4") event (1/2/both) registered for this participant.
    """

    ex_event = []
    for i in events:
        # Registering participant in selected events
        e_id = db.get_event_id(i)
        resp = db.get_reg(p_id=p_id, event_id=e_id[0][0])
        if resp == 0:
            resp = db.add_reg(p_id=p_id, event_id=e_id[0][0])
            if resp == 0:
                return 0
            ex_event.append(0)
        else:
            ex_event.append(1)

    # "0" some error, "1" success, ("2"/"3"/"4") event (1/2/both) registered for this participant
    if len(ex_event) == 2:
        if ex_event[0] == 1 and ex_event[1] == 1:
            return 4
        elif ex_event[0] == 1:
            return 2
        elif ex_event[1] == 1:
            return 3
    elif ex_event[0] == 1:
        return 4
    return 1


def add_event(name: str, date: str, time: str) -> int:
    """
    Request database to add new event.

    :param name: Name of event.
    :param date: Date of event.
    :param time: Time of event.
    :return: "1" success, "0" event name exists.
    """

    resp = db.add_event(name=name, date=date, time=time)
    # "1" success, "0" event name exists
    return resp


def get_events() -> [str]:
    """
    Request database for list of events.

    :return: List of events.
    """

    events = db.get_events()
    # list of tupple(name)
    return events


def mark_entry(p_id: str, event: str) -> int:
    """
    Mark entry of a participant into to the event.

    :param p_id: Participant ID.
    :param event: Event name.
    :return: "0" Not Registered, "1" Registered, "2" Entered.
    """

    event_id = db.get_event_id(event)

    resp = db.get_reg(p_id=p_id, event_id=event_id[0][0])
    if resp == 1:
        db.mark_entry(p_id=p_id, event_id=event_id[0][0])
    # "0" Not Registered, "1" Registered, "2" Entered
    return resp


def remove_event(name: str, date: str, time: str) -> int:
    """
    Remove an event from database.

    :param name: Name of event.
    :param date: Date of event.
    :param time: Time of event.
    :return: "1" success, "0" event participant registered, "4" wrong event details.
    """

    resp = db.remove_event(name=name, date=date, time=time)
    # "1" success, "0" event participant registered, "4" wrong event details
    return resp


def get_report() -> [[str]]:
    """
    Return the list of participant data and events they are registered in.

    :return: List of participant data.
    """

    return db.get_report()
