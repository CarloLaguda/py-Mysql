#I pokemon sono pucciosissimi
from flask import Flask
from flask import send_file
from flask_cors import CORS

# Creating a new "app" by using the Flask constructor. Passes __name__ as a parameter.
app = Flask(__name__)
CORS(app)

# app route di base
@app.route("/")
def index():
    return send_file('pokemon.json')

# Checks to see if the name of the package is the run as the main package.
if __name__ == "__main__":
    # Runs the Flask application only if the main.py file is being run.
    app.run(debug= True)