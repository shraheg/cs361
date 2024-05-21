import re
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/validate_email', methods=['POST'])
def validate_email():
    data = request.get_json()
    if 'email' not in data:
        return jsonify({'error': 'Email address not provided'}), 400

    email = data['email']

    if not re.match(r'^\S+@\S+\.\S+$', email):
        return jsonify({'valid': False, 'message': 'Invalid email address format'}), 200

    return jsonify({'valid': True, 'message': 'Email address is valid'}), 200

if __name__ == '__main__':
    app.run(debug=True)