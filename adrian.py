from flask import Flask, render_template
from model import Model, HouseHold, User, Chore
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/sendSass")
def sendSass():
    return render_template('sendSass.html', name="James")


@app.route("/api/chart")
def chart():
    model = Model()
    model.createHouse("Hacks", 3)
    y = model.getHouse("Hacks")
    model.createUser("Adrian", "test2", "test3", "test4")
    y.addUser("Adrian")
    return model.users[0].to_json()

# @app.route("/api/users/<id>")
# def get_user_id(id):
#     return User.get(id).to_json()

if __name__ == "__main__":
    app.run(debug=True)