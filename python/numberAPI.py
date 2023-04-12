import json
from flask_cors import CORS
from flask import Flask, request, jsonify
from contactDAO import ContactDAO
from number import checkNumSize

app = Flask(__name__)
CORS(app)

@app.route("/number", methods=["GET"])
def getNumber():
    return "Mobile Number List"

@app.route("/number", methods=["POST"])
def createNumber():
    records = json.loads(request.data)
    print(records)
    isValidNumber = checkNumSize(records["phoneNumber"])
    if(isValidNumber):
     contactdao = ContactDAO()
     contactdao.insertContactNumber(records)
     return "Registered"
    else:
     return "In valid phonenumber"


app.run(host="0.0.0.0", port="8081")
