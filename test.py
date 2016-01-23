from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello"


@app.route("/sendSass")
def sendSass():
    return render_template('sendSass.html', name="James")

if __name__ == "__main__":
    app.run(debug=True)