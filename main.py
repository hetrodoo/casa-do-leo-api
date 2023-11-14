import os

import waitress
from firebase_admin import credentials, initialize_app
from google.cloud import datastore
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

cred = credentials.Certificate('./casa-do-leo-firebase-admin.json')
default_app = initialize_app(cred)

client = datastore.Client()

kind = "casadoleo_sub"


@app.route("/newsletter", methods=['POST'])
def newsletter():
    data = request.get_json()
    print(data)

    entity_key = client.key(kind)

    entity = datastore.Entity(key=entity_key)
    entity["name"] = data["name"]
    entity["email"] = data["email"]
    entity["phone"] = data["phone"]
    entity["useWhatsapp"] = data["useWhatsapp"]

    client.put(entity)

    return "Ok"


@app.route("/notify", methods=['GET'])
def notify():
    query = client.query(kind=kind)

    return list(query.fetch())


if __name__ == '__main__':
    waitress.serve(app.wsgi_app, port=os.environ.get('PORT', '3000'), url_scheme='http')
