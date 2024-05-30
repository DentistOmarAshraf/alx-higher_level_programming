#!/usr/bin/python3

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/first")
def page():
    return render_template("page_1.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0' ,port=5000)
