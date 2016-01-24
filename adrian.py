from flask import Flask, render_template
from model import Model, HouseHold, User, Chore
app = Flask(__name__)

model = Model()
model.createHouse("Hacks", 3)
y = model.getHouse("Hacks")
model.createUser("Adrian", "test2", "test3", "test4")
model.createUser("NJ", "test2", "test3", "test4")
model.createUser("Jaclyn", "test2", "test3", "test4")
y.addUser(model.users[0])
y.addUser(model.users[1])
y.addUser(model.users[2])
y.addChore("Trash", 3)
y.addChore("Dishes", 4)
y.addChore("Bathroom", 7)
y.addChore("Kitchen", 14)
y.startHouse()

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/sendSass")
def sendSass():
    return render_template('sendSass.html', name="James")


@app.route("/api/chart")
def chart():
    global model
    return model.users[0].to_json()


@app.route("/api/person_chore_dict")
def choreDict():
    global model
    return model.getHouse("Hacks").choreDict()

# @app.route("/api/users/<id>")
# def get_user_id(id):
#     return User.get(id).to_json()

if __name__ == "__main__":
    app.run(debug=True)