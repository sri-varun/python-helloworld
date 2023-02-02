from flask import Flask, jsonify, request
app = Flask(__name__)
import traceback

def create_app():
    app = Flask(__name__)
    app.config['WTF_CSRF_ENABLED'] = False
    with app.app_context():
        highlow()
    return app

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/highlow", methods=['POST'])
def highlow():
 print("called ....")
 try:
    value1 = request.get_json().get('value')
    if isinstance(value1, int):
        foo = jsonify(value="1",rating="high") if (value1 > 99) else jsonify(value="0",rating="low")
        return foo
    else:
        return "error"
 except Exception:
    traceback.print_exc()
    
app.run(host="localhost", port=9001)
