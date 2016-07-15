import json


def jsonify(dictionary):
    return json.dumps(dictionary, indent=4)
