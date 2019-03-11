from flask import Flask

'''This API is a microservice used for Make School's Unconference Slack Bot reminder utility'''

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    app.run(debug=True)
