from flask import Flask

app = Flask(__name__)

@app.route("/")
def test():
	return "吳柏榕腦到被驢踢到"

if __name__ == "__main__":
	app.run(debug=True)