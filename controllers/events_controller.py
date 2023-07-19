from flask import Flask, render_template, request
from flask import Blueprint
from models.event import Event
from models.event_list import events

# INDEX, display all events
events_blueprint = Blueprint("events", __name__)
# GET /events
@events_blueprint.route("/events")
def index():
    return render_template("index.jinja", title="Events Page", event_list = events)

# create a new event
@events_blueprint.route("/events", methods=["POST"])
def create_event():
    # get the fields from the form
    name = request.form["name"]
    date = request.form["date"]
    location = request.form["location"]
    number_of_guest = request.form["num_of_guest"]
    description = request.form["description"]
    recurring = request.form.get_json["recurring"]
    # create the new event using the fields
    new_event = Event(name, date, number_of_guest, location, description, recurring)
    # add the new event to the list events
    events.append(new_event)
    # return render_template
    return render_template("index.jinja", title="Events Page", event_list = events)

# delete a event from list
# @events_blueprint.route("/events/<index>/delete", methods=["POST"])
# def delete_event():
