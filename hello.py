from flask import Flask
from flask import request, jsonify, json

myapp = Flask(__name__)
myapp.config["DEBUG"] = True



@myapp.route("/api/upperCaseService", methods=['GET','POST'])
def caps():
    data = dict(request.get_json())
    cap = {}
    if data:
        for key,value in data.items():
            cap[key] = [word.capitalize() for word in value]
    return jsonify(cap)


myapp.run()
