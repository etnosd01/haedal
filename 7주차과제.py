from flask import Flask, render_template
import random
app = Flask(__name__)

@app.route("/")
def hello():
    return "2020110116 음악학과 송나흔"

@app.route("/me/")
def lunch():
    menu = ["경북대학교.jpg"]
    return render_template("index.html", food_img=menu)

if __name__ == "__main__":
    app.run(debug=True)