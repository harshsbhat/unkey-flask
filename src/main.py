from flask import Flask, jsonify
from middleware import with_auth


app = Flask(__name__)

@app.route('/public', methods=['GET'])
def public_route():
    return jsonify({"message": "Hello World!"})

@app.route('/protected', methods=['GET'])
@with_auth(permission="withAuth")
def protected_route():
    return jsonify({"message": "Hello protected world!"})

if __name__ == "__main__":
    app.run(port=3000)
