from flask import Flask
from flask import render_template, jsonify, request
import json

app = Flask(__name__)
app.my_age = 20

@app.route('/')
def index():
    """
    Render a Hello World response.

    :return: Flask response
    """
    return render_template('index.html')


@app.route('/myAge', methods=['GET', 'POST'])
def myAge():
    if request.method == 'GET':
        return jsonify({'Age': app.my_age })

    if request.method == 'POST':
        received_data = json.loads(request.data)
        app.my_age  = received_data.get("newAge")
        return jsonify({'log': "success"})

if __name__ == '__main__':
    app.run()