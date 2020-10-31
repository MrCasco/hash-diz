# Libraries for running our app on the cloud
import os
from flask import Flask, request
from flask import jsonify
import requests
import json

# Hash and OTP purposes libraries
import hashlib
import pandas as pd
from numpy import random as rand

app = Flask(__name__)

# @app.route('/ISR/<sueldo>', methods=['GET'])
# def calcularISR(sueldo):
#     try:
#         return getISR(sueldo)
#     except BaseException as error:
#         return('An exception occurred: {}'.format(error), 400)

@app.route('/otp', methods=['GET'])
def otp():
    alphabet = dict(zip([x for x in range(1, 37)], 'abcdefghijklmnopqrstuvwxyz0123456789'))
    data = ''.join([alphabet[x] for x in rand.randint(1, 37, size=10)])
    rawJson = {'otp':data}
    resultJson = app.response_class(
        response=json.dumps(rawJson),
        status=200,
        mimetype='application/json'
    )
    print(data)
    return resultJson

@app.route('/hash/<passw>', methods=['GET'])
#En esta función se van a hashear todos los datos recibidos.
def hash_file(passw):
   h = hashlib.sha1()
   h.update(passw.encode())

   # se regresa la representación hexadecimal de los dígitos.
   rawJson = {'hash':h.hexdigest()}
   resultJson = app.response_class(
       response=json.dumps(rawJson),
       status=200,
       mimetype='application/json'
   )
   return resultJson

#LA = 'json.txt'
#print(LA)
'''LA = {'Data': {'Surname': 'Emmanuel',
'Flastname': 'Moctezuma', 'Mlastname': 'Hernández'}
}'''
passw = 'hola'
#passw = LA['Data']['Surname']
#print(json.dumps(LA, indent=2))
#print(passw)

#Se asigna el parámetro que queremos a una varibale.
#passw = LA['Data']['password']

#Se manda a llamar la función para el hasheo de los datos tokenizados.
message = hash_file(passw)
#print(message)
#LA['Data']['Surname'] = message
#print(json.dumps(LA, indent=2))

#Reescribir el json.
#LA['Data']['password'] = message

#Enviar json a la app o sitio web.
#return LA

print(otp())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
