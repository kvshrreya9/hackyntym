from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect("donors.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/register", methods=["GET","POST"])
def register():

    if request.method == "POST":

        name = request.form["name"]
        blood = request.form["blood"]
        phone = request.form["phone"]
        city = request.form["city"]
        area = request.form["area"]
        availability = request.form["availability"]

        conn = get_db_connection()

        conn.execute(
        "INSERT INTO donors (name,blood,phone,city,area,availability) VALUES (?,?,?,?,?,?)",
        (name,blood,phone,city,area,availability)
        )

        conn.commit()
        conn.close()

        return render_template("success.html", name=name)

    return render_template("register.html")


@app.route("/search", methods=["GET","POST"])
def search():

    if request.method == "POST":

        blood = request.form["blood"]
        city = request.form["city"]

        conn = get_db_connection()

        donors = conn.execute(
        "SELECT * FROM donors WHERE blood=? AND city=? AND availability='Available'",
        (blood,city)
        ).fetchall()

        conn.close()

        return render_template("results.html", donors=donors)

    return render_template("search.html")


# 🚨 Emergency Page
@app.route("/emergency")
def emergency():
    return render_template("emergency.html")


# View All Donors
@app.route("/donors")
def donors():

    conn = get_db_connection()

    donors = conn.execute("SELECT * FROM donors").fetchall()

    conn.close()

    return render_template("donors.html", donors=donors)


if __name__ == "__main__":
    app.run()
