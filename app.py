from flask import Flask, render_template, jsonify

app = Flask(__name__)

desk_status = "Empty"

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
def status():
    global desk_status
    desk_status = "Occupied" if desk_status == "Empty" else "Empty"
    return jsonify({
        "desk": desk_status,
        "distance": "45 cm" if desk_status == "Occupied" else "> 80 cm",
        "last_updated": "Just now"
    })
