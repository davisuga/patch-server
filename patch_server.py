from flask import Flask, jsonify, request, send_from_directory, render_template
import re

app = Flask(__name__)
UPLOAD_DIRECTORY = './uploads'

 
@app.route('/')
@app.route('/update')
def update(methods=['POST', 'GET']):
        return render_template('patchs.html')

@app.route('/static/img/<path:filename>', methods=['GET'])
def getimage(filename):
        return send_from_directory('./static/img', filename=filename, as_attachment=True)

@app.route('/uploads/<path:filename>', methods=['POST'])
def download(filename):
        return send_from_directory(UPLOAD_DIRECTORY, filename=filename, as_attachment=True)


app.run(debug=True, host='0.0.0.0')