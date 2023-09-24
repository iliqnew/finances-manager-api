from flask import (
    Flask,
    request,
    jsonify
)

from db import DB
from fond import (
    get_fond,
    get_fonds,
    post_fond,
    put_fond
)
from transaction import (
    get_transaction,
    post_transaction,
    put_transaction
)

from views import (
    get_expenses
)


app = Flask(__name__)


DATABASE = DB()


@app.route("/fond", methods=["GET", "POST", "PUT"])
def fond():
    
    if request.method == "POST":
        data = request.get_json()
        fond = post_fond(DATABASE, data)
        return jsonify(fond), 201
    
    fond_id = request.args.get("id")

    if not fond_id:
        return jsonify({"error": "please, provide an id"}), 404
    if not fond_id.isdigit():
        return jsonify({"error": "id must be a whole number"}), 404

    fond_id = int(fond_id)

    if request.method == "GET":
        return jsonify(get_fond(DATABASE, fond_id)), 200
    
    if request.method == "PUT":
        data = request.get_json()
        fond = put_fond(DATABASE, fond_id, data)
        return jsonify(fond), 200


@app.route("/transaction", methods=["GET", "POST", "PUT"])
def transaction():
    
    if request.method == "POST":
        data = request.get_json()
        transaction = post_transaction(DATABASE, data)
        return jsonify(transaction), 201
    
    transaction_id = request.args.get("id")

    if not transaction_id:
        return jsonify({"error": "please, provide an id"}), 404
    if not transaction_id.isdigit():
        return jsonify({"error": "id must be a whole number"}), 404

    transaction_id = int(transaction_id)

    if request.method == "GET":
        return jsonify(get_transaction(DATABASE, transaction_id)), 200
    
    if request.method == "PUT":
        data = request.get_json()
        transaction = put_transaction(DATABASE, transaction_id, data)
        return jsonify(transaction), 200


@app.route("/fonds", methods=["GET"])
def fonds():
    if request.method == "GET":
        return jsonify(get_fonds(DATABASE)), 200


@app.route("/balance", methods=["GET"])
def balance():
    if request.method == "GET":
        return jsonify(get_expenses(DATABASE)), 200


if __name__ == "__main__":
    app.run(debug=True)