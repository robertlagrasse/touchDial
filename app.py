from flask import Flask, render_template, request

# Initialize the Flask app
app = Flask(__name__)

# Define the route for the home page
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # Retrieve the phone number from the form
        phone_number = request.form.get("phone-number")

        # Print the phone number to the console
        print(f"Phone Number Submitted: {phone_number}")

        # Optionally, return a confirmation message or redirect
        return "Phone number submitted successfully!"

    # Render the form for GET requests
    return render_template("index.html")

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
