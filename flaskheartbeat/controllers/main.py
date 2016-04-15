from flask import Blueprint, render_template, flash, request, redirect, url_for
from flask.ext.login import login_user, logout_user, login_required

from flaskheartbeat.extensions import cache
from flaskheartbeat.forms import LoginForm
from flaskheartbeat.models import User, Devices, Statuses

#Flask Restful stuff
from flask_restful import Resource
from flask import jsonify

#pushould stuff
from pushould import Pushould


class HeartbeatReceiver(Resource):

    def get(self, deviceID, statuscode):
        device = Devices.query.filter_by(deviceid=deviceID).first()
        statusmessage = Statuses.query.filter_by(statuscode=statuscode).first()

        try:
            print device.devicename
            print statusmessage.statusmessage
            sendAlert("TestSecurity", statusmessage.statuscode,
                      statusmessage.statusmessage,
                      device.deviceid,
                      device.devicename)

            return jsonify(device=device.devicename,
                           status=statusmessage.statusmessage)
        except:
            return jsonify(device="No device found",
                           status="No status found")


def sendAlert(recipients, statuscode, statusmessage, deviceid, devicename):
    pushould = Pushould(server_token="rxz8hxpsr7hbf10hp42h38mt1sz63mmlecul5fe06ow3hxui",
                        url="https://1dvxtg49adq5f5jtzm2a04p2sr2pje3fem1x6gfu2cyhr30p.pushould.com",
                        email="kliknes@gmail.com",
                        password="uNh4ck4bl3")

    pushould.trigger(room=recipients,
                     event="send",
                     data={"statuscode": statuscode,
                           "statusmessage": statusmessage,
                           "deviceid": deviceid,
                           "devicename": devicename})

main = Blueprint('main', __name__)


@main.route('/')
@cache.cached(timeout=1000)
def home():
    return render_template('index.html')


@main.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).one()
        login_user(user)

        flash("Logged in successfully.", "success")
        return redirect(request.args.get("next") or url_for(".home"))

    return render_template("login.html", form=form)


@main.route("/logout")
def logout():
    logout_user()
    flash("You have been logged out.", "success")

    return redirect(url_for(".home"))


@main.route("/restricted")
@login_required
def restricted():
    return "You can only see this if you are logged in!", 200
