from flask import Flask, render_template, jsonify

app = Flask(__name__)

status = "Empty"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/hardware")
def hardware():
    return render_template("hardware.html")

@app.route("/team")
def team():
    return render_template("team.html")

@app.route("/status")
def get_status():
    global status
    status = "Occupied" if status == "Empty" else "Empty"

    return jsonify({
        "desk": status,
        "distance": "45 cm" if status=="Occupied" else "No person",
        "device": "Arduino Uno",
        "location": "Lab 1"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0")
