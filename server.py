from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    """
    home route to deliver react frontend app to client
    """
    return "Hello world!"


@app.route('/api/bool')
def boolean():
    """
    sends sample boolean data to client
    """
    return jsonify({
        'result': True
    })


@app.route('/api/line')
def line():
    """
    sends time series data to client for line chart
    """
    return jsonify([1, 2, 3, 4, 5])


@app.route('/api/pie')
def pie():
    """
    sends dict-based pie chart quantity data to client
    """
    return jsonify({
        "AAA": 15,
        "BBB": 20,
        "CCC": 40
    })
