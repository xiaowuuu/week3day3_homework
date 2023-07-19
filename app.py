from flask import Flask
from controllers.events_controller import events_blueprint

app = Flask(__name__)
app.register_blueprint(events_blueprint)
# I always forgot the register
@app.route("/")
def hello_world():
    return "<h1>hello</h1>"