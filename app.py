# Libraries for running our app on the cloud
import os
from flask import Flask, request
from flask import jsonify
import json
import requests

# Hash and OTP purposes libraries
import hashlib
from numpy import random as rand

app = Flask(__name__)

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
    return resultJson

@app.route('/hash/<query>', methods=['GET'])
def hash_password(query):
    h = hashlib.sha1()
    try:
        if not query[query.rindex('&')+1:]=='':
            passw = query[:query.rindex('&')]
            h.update(passw.encode())
            card = query[query.rindex('&')+1:]
            c = hashlib.sha1()
            c.update(card.encode())
            rawJson = {'Password':h.hexdigest(),'Card':c.hexdigest()}
        else:
            raise Exception('Only Password')
    except:
        h.update(query.encode())
        rawJson = {'Password':h.hexdigest()}
    resultJson = app.response_class(
    response = json.dumps(rawJson),
    status = 200,
    mimetype = 'application/json'
    )
    return resultJson

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
