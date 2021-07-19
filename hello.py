from flask import Flask
from flask import request, jsonify

myapp = Flask(__name__)
app.config["DEBUG"] = True

words = [
    {
        "words": ["james", "may", "jeremy", "clarkson", "richard", "hammond"]
    }
]

@myapp.route("/", methods=['GET'])
def caps():
    for word in words:
        word = word.capitalize()
    return jsonify(words)

app.run()
