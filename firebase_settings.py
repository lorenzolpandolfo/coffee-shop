import pyrebase
import firebase_admin
from firebase_admin import auth as admin_auth
from firebase_admin import credentials
from firebase_admin import exceptions
import json
import os

print(os.environ)

segredo = os.environ.get('TEST_SECRET')

print(segredo)


with open('firebaseconfig.json', 'r') as arquivo:
    dados_secretos = json.load(arquivo)

firebaseConfig = dados_secretos

firebase = pyrebase.pyrebase.initialize_app(firebaseConfig)

cred = credentials.Certificate("servicekey.json")
firebase_admin.initialize_app(cred, {"databaseURL": dados_secretos["databaseURL"]})

auth = firebase.auth()
database = firebase.database()
storage = firebase.storage()
