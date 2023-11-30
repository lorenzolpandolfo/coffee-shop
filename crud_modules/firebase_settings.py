# import http.client
import pyrebase
import firebase_admin
from firebase_admin import auth as admin_auth, credentials, exceptions, db
import json

# para ver o que esta sendo enviado no login (no caso, email e senha)
# http.client.HTTPConnection.debuglevel = 1

with open('firebase_credentials.json', 'r') as arquivo:
    dados_secretos = json.load(arquivo)

firebase_credentials = dados_secretos

firebase = pyrebase.pyrebase.initialize_app(firebase_credentials)

cred = credentials.Certificate("service_key.json")
firebase_admin.initialize_app(cred, {"databaseURL": dados_secretos["databaseURL"]})

auth = firebase.auth()
database = firebase.database()
storage = firebase.storage()

admin_db = db
