import json
from flask import Flask, render_template, request
from twilio.rest import Client

# Load credentials from creds.json
with open("creds.json") as f:
    creds = json.load(f)

# Twilio credentials
TWILIO_ACCOUNT_SID = creds["TWILIO_ACCOUNT_SID"]
TWILIO_AUTH_TOKEN = creds["TWILIO_AUTH_TOKEN"]
TWILIO_PHONE_NUMBER = creds["TWILIO_PHONE_NUMBER"]

# Initialize the Twilio client
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# Initialize the Flask app
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # Retrieve the phone number from the form
        phone_number = request.form.get("phone-number")

        # Make a call to the phone number
        try:
            call = client.calls.create(
                to=phone_number,
                from_=TWILIO_PHONE_NUMBER,
                twiml="<Response><Say>What's up, dog?</Say></Response>"
            )
            print(f"Call initiated. SID: {call.sid}")
            return "Call successfully placed!"
        except Exception as e:
            print(f"Error placing call: {e}")
            return "Failed to place call. Check the logs."

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
