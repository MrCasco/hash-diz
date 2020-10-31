import os
import sys
from flask import Flask, request
from flask import jsonify
import requests
import json


app = Flask(__name__)


def getISR(s):
    sueldo = float(s)
    ISR_TABLE=[[0.01,	578.52,	0.00,	1.92]]
    ISR_TABLE.append([578.53,	4910.18,	11.11,	6.40])
    ISR_TABLE.append([4910.19,	8629.20,	288.33,	10.88])
    ISR_TABLE.append([8629.21,	10031.07,	692.96,	16.00])
    ISR_TABLE.append([10031.08,	12009.94,	917.26,	17.92])
    ISR_TABLE.append([12009.95,	24222.31,	1271.87,	21.36])
    ISR_TABLE.append([24222.32,	38177.69,	3880.44,	23.52])
    ISR_TABLE.append([38177.70,	72887.50,	7162.74,	30.00])
    ISR_TABLE.append([72887.51,	97183.33,	17575.69,	32.00])
    ISR_TABLE.append([97183.34,	291550.00,	25350.35,	34.00])
    ISR_TABLE.append([291550.01,	1000000000.00,	91435.02,	35.00])
    for row in ISR_TABLE:
        if sueldo >= row[0] and sueldo <=row[1]:
            resto = sueldo-row[0]
            porcentaje = resto * (row[3]/100)
            ISR=porcentaje+row[2]
            exit
    isr = "${0:,.2f}".format(ISR)
    jsonRaw = {
            'ISR': isr
        }
    jsonResponse = app.response_class(
        response=json.dumps(jsonRaw),
        status=200,
        mimetype='application/json'
    )
    return jsonResponse

@app.route('/ISR/<sueldo>', methods=['GET'])
def calcularISR(sueldo):
    try:
        return getISR(sueldo)
    except BaseException as error:
        return('An exception occurred: {}'.format(error), 400)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
