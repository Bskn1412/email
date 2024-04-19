from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin # type: ignore
from mail_notes import send_notes_email

app = Flask(__name__)
CORS(app)  

@app.route('/submit/<email>/<notes>', methods=['POST', 'GET'])
def submit(email, notes):
    if request.method == "POST" or request.method == 'GET':
        result = send_notes_email(email, notes)
        if result == 'done':
            return jsonify({"key": "sent"})
        else:
            return jsonify({"key": "not sent"})

if __name__ == "_main_":
    app.run(debug=True)
    
