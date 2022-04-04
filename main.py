from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def collect_data():
    return render_template("Login.html")


@app.route("/register")
def Register():
    return render_template("Register.html")


if __name__ == "__main__":
    app.run()
