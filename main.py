from flask import Flask, render_template
from model import HouseHold
import json
app = Flask(__name__)

houseHold = HouseHold("fake", 6)
houseHold.addUser("Jaclyn", "test2", "test3", "test4")
houseHold.addUser("Adrian", "test2", "test3", "test4")
houseHold.addUser("NJ", "test2", "test3", "test4")
houseHold.addUser("James", "test2", "test3", "test4")
houseHold.addUser("Ali", "test2", "test3", "test4")
houseHold.addUser("Spencer", "test2", "test3", "test4")
houseHold.addChore("Trash", 3)
houseHold.addChore("Dishes", 4)
houseHold.addChore("Bathroom", 7)
houseHold.addChore("Shower", 7)
houseHold.addChore("Attic", 14)
houseHold.addChore("Kitchen", 3)
houseHold.startHouse()


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/api/do-chore/<chore>")
def completeChore(chore):
    global houseHold
    houseHold.doChore(chore)
    return houseHold.choreDict()

@app.route("/sendSass")
def sendSass():
    return render_template('sendSass.html', name="James")

@app.route("/api/person_chore_dict")
def choreDict():
    global houseHold
    return houseHold.choreDict()

@app.route("/login")
def login():
    return render_template('login.html')


if __name__ == "__main__":
    app.run(debug=True)

