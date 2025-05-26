#I pokemon sono pucciosissimi
from flask import Flask
from flask import send_file
from flask_cors import CORS
import random
import json

# Creating a new "app" by using the Flask constructor. Passes __name__ as a parameter.
app = Flask(__name__)
CORS(app)

#Aprire il file json
#caricare l'oggetto dentro data
f = open('pokemon.json')
data = json.load(f)
data_rand = data['pokemon'][random.randrange(0,10)]

# app route di base
@app.route("/")
def index():
    return send_file('pokemon.json')

@app.route("/random")
def random():
    return data_rand

@app.route("/search/<name>")
def search(name):
    for pokemon in data['pokemon']:
        if pokemon['Name'] == name:  # Check if the 'Name' key matches the given name
            return pokemon 
            
    return "Nessun pokemon trovato"

# Checks to see if the name of the package is the run as the main package.
if __name__ == "__main__":
    # Runs the Flask application only if the main.py file is being run.
    app.run(debug= True)

    

