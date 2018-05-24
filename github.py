from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return "manager的index页面"


if "__main__" == "__name__":
	app.run()

