from flask import Flask
from flask import request, jsonify

myapp = Flask(__name__)
myapp.config["DEBUG"] = True

words =  {"word":["james", "may", "jeremy", "clarkson", "richard", "hammond"]}


@myapp.route("/api/upperCaseService", methods=['GET'])
def caps():
    data = dict(words)
    cap = {}
    for key,value in data.items():
        cap[key] = [word.capitalize() for word in value]
    return jsonify(cap)

myapp.run()
