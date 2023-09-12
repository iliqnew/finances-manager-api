from flask import (
    Flask,
    request,
    jsonify
)

from db import DB


app = Flask(__name__)


@app.route("/fond", methods=["GET", "POST", "PUT"])
def fond():
    if request.method == "GET":

        fond_id = request.args.get("id")
        
        if not fond_id:
            return jsonify({"error": "please, provide an id"}), 404
        if not fond_id.isdigit():
            return jsonify({"error": "id must be a whole number"}), 404
        
        return jsonify(DB().get_fond(fond_id)), 200
    
    elif request.method == "POST":
        data = request.get_json()
        return jsonify(data), 201
    
    elif request.method == "PUT":
        data = request.get_json()
        return jsonify(data), 201


if __name__ == "__main__":
    app.run(debug=True)