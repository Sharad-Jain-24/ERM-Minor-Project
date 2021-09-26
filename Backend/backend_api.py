
from flask import Flask, request, jsonify, abort
from flask_cors import CORS

try:
    import Backend.manage_op as op
except:
    import manage_op as op

app = Flask(__name__)
CORS(app)

# LIST OF FUNCTIONS
# login
# add_user
# add_part
# add_event
# get_events
# mark_entry
# remove_event
# get_report


@app.route('/')
def hello_world():
    """
    It is demo function to test weather server is working or not.

    :return: A static string.
    """
    return 'Hello from Flask! This is a test site'


@app.route('/login', methods=["Post"])
def login():
    """
    This function will verify credentials.
    It requires user id and hashed password.

    :return: "1"/"2" Password match, "0" Wrong password, "-1" User dose not exists in JSON format.
    """

    req_data = request.get_json()
    id = req_data["id"]
    passw = req_data["password"]

    # "1"/"2" Password match, "0" Wrong password, "-1" User dose not exists
    permission = op.login(uid=id, passw=passw)

    return jsonify({
        "method": "POST",
        "headers": {
            "content-type": "application/json"
        },
        "body": {
            "permission": permission
        }
    })


@app.route('/add_user', methods=["Post"])
def add_user():
    """
    Handles the request to add a user.
    It requires user details, their login credentials and operator authentication.

    :return: "1" if added, "0" Error (User already exists) in JSON format.
    """

    req_data = request.get_json()
    response = "Custom Response"
    e_id = req_data["email_id"]
    passw = req_data["password"]
    phone = req_data["phone"]
    name = req_data["name"]
    perm = req_data["permission"]
    uid = req_data["uid"]
    upassw = req_data["upassw"]

    if op.login(uid=uid, passw=upassw) == 2:
        # "1" if added, "0" if exists
        response = op.add_user(name=name, email_id=e_id,
                               phone=phone, perm=perm, password=passw)
    else:
        abort(404)

    return jsonify({
        "method": "POST",
        "headers": {
            "content-type": "application/json"
        },
        "body": {
            "response": response
        }
    })


@app.route('/add_part', methods=["Post"])
def add_part():
    """
    Handles the request to add a participant.
    It requires participant details, events list and operator authentication.

    :return: "0" some error / no registration for this participant, "1" success, ("2"/"3"/"4") event (1/2/both) registered for this participant in JSON format.
    """

    req_data = request.get_json()
    response = "Custom Response"
    e_id = req_data["email_id"]
    events = req_data["events"]
    p_id = req_data["p_id"]
    phone = req_data["phone"]
    name = req_data["name"]
    uid = req_data["uid"]
    upassw = req_data["upassw"]

    if op.login(uid=uid, passw=upassw) >= 1:
        # "0" some error / no registration for this participant, "1" success,
        # ("2"/"3"/"4") event (1/2/both) registered for this participant
        response = op.add_part(p_id=p_id, name=name,
                               email=e_id, phone=phone, events=events)
    else:
        abort(404)

    return jsonify({
        "method": "POST",
        "headers": {
            "content-type": "application/json"
        },
        "body": {
            "response": response
        }
    })


@app.route('/add_event', methods=["Post"])
def add_event():
    """
    Handles the request to add a event.
    It requires event details and operator authentication.

    :return: "1" success, "0" event name exists in JSON format.
    """

    req_data = request.get_json()
    response = "Custom Response"
    date = req_data["date"]
    time = req_data["time"]
    name = req_data["name"]
    uid = req_data["uid"]
    upassw = req_data["upassw"]

    if op.login(uid=uid, passw=upassw) >= 1:
        # "1" success, "0" event name exists
        response = op.add_event(name=name, date=date, time=time)
    else:
        abort(404)

    return jsonify({
        "method": "POST",
        "headers": {
            "content-type": "application/json"
        },
        "body": {
            "response": response
        }
    })


@app.route('/get_events')
def get_events():
    """
    Handles the request for list of events.

    :return: List of events in JSON format.
    """

    # list of tupple(event_id and name)
    response = op.get_events()

    return jsonify({
        "method": "POST",
        "headers": {
            "content-type": "application/json"
        },
        "body": {
            "response": response
        }
    })


@app.route('/mark_entry', methods=["Post"])
def mark_entry():
    """
    Handles the request to mark entry of a participant in a event.
    It requires participant ID, event name and operator authentication.

    :return: "0" Not Registered, "1" Registered, "2" Participant already entered in JSON format.
    """

    req_data = request.get_json()
    response = "Custom Response"
    p_id = req_data["p_id"]
    event = req_data["event"]
    uid = req_data["uid"]
    upassw = req_data["upassw"]

    if op.login(uid=uid, passw=upassw) >= 1:
        # "0" Not Registered, "1" Registered, "2" Entered
        response = op.mark_entry(p_id=p_id, event=event)
    else:
        abort(404)

    return jsonify({
        "method": "POST",
        "headers": {
            "content-type": "application/json"
        },
        "body": {
            "response": response
        }
    })


@app.route('/remove_event', methods=["Post"])
def remove_event():
    """
    Handles the request to remove an event.
    It requires event name and operator authentication.

    :return: "1" success, "0" event participant registered, "4" wrong event details in JSON format.
    """

    req_data = request.get_json()
    response = "Custom Response"
    date = req_data["date"]
    time = req_data["time"]
    name = req_data["name"]
    uid = req_data["uid"]
    upassw = req_data["upassw"]

    if op.login(uid=uid, passw=upassw) >= 1:
        # "1" success, "0" event participant registered, "4" wrong event details
        response = op.remove_event(name=name, date=date, time=time)
    else:
        abort(404)

    return jsonify({
        "method": "POST",
        "headers": {
            "content-type": "application/json"
        },
        "body": {
            "response": response
        }
    })


@app.route('/get_report')
def get_report():
    """
    Handles the request to remove an event.
    It requires event name and operator authentication.

    :return: List of participant and registered events in JSON format.
    """

    # list of tupple(event_id and name)
    response = op.get_report()

    return jsonify({
        "method": "POST",
        "headers": {
            "content-type": "application/json"
        },
        "body": {
            "response": response
        }
    })


if __name__ == "__main__":
    # app.run(debug=True)
    app.run()
