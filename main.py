from flask import Flask, jsonify, render_template
import json

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def hello_world():

    return render_template("home.html")

if __name__ == "__main__":

    # Lancement de l'application
    app.run(host='localhost', port="5001", debug=True)