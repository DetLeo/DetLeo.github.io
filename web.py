from flask import Flask

app = Flask(__name__)

@app.route("/")
def test():
	return "賴博猴 蘇水梨 阿寶雄 吳柏榕樹"

if __name__ == "__main__":
	app.run(debug=True)