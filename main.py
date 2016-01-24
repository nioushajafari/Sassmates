from flask import Flask, render_template
from model import HouseHold
import json
app = Flask(__name__)

houseHold = HouseHold("fake", 6)
houseHold.addUser("Jaclyn", "test2", "test3", "test4")
houseHold.addUser("NJ", "test2", "test3", "test4")
houseHold.addUser("Adrian", "test2", "test3", "test4")
houseHold.addUser("Ali", "test2", "test3", "test4")
houseHold.addUser("Spencer", "test2", "test3", "test4")
houseHold.addUser("James", "test2", "test3", "test4")
houseHold.addChore("Trash", 3)
houseHold.addChore("Dishes", 4)
houseHold.addChore("Bathroom", 7)
houseHold.addChore("Kitchen2", 14)
houseHold.addChore("Trash2", 3)
houseHold.addChore("Dishes2", 4)
houseHold.addChore("Bathroom2", 7)
houseHold.addChore("Kitchen2", 14)
houseHold.startHouse()


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/sendSass")
def sendSass():
    return render_template('sendSass.html', name="James")

@app.route("/household")
def household():
    global houseHold
    return json.dumps(houseHold.__dict__)


if __name__ == "__main__":
    app.run(debug=True)

