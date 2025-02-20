from flask import Flask, request, jsonify

app = Flask(__name__)
config = {}

@app.route('/config', methods=['POST'])
def receive_config():
    global config
    config = request.json
    return jsonify({"message": "Config received"}), 200

@app.route('/validate', methods=['POST'])
def validate_data():
    data = request.json
    if 'size' in data and data['size'] <= config['daily_limit']:
        if data['format'] in config['accepted_data_formats']:
            return jsonify({"message": "Data valid"}), 200
        else:
            return jsonify({"message": "Invalid data format"}), 400
    else:
        return jsonify({"message": "Data exceeds daily limit"}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5001)
