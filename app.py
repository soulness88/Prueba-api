from flask import Flask, jsonify, request
app = Flask(__name__)

def checker(name):
  return "heheh"

@app.route('/page', methods=['GET'])
def new():
  name = request.args-get('name'=
  if name == 'DHRUV':
    checker(name)
  return jsonify({
    'name': 'Dhru'
  })
