from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
	return "<p>hello_world</p>"

if __name__ == "__main__":
	app.run(debug = True)