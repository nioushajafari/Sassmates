from time import gmtime, strftime

from datetime import datetime
from dateutil import relativedelta

import json

#     def to_json(self):
#         return json.dumps({
#             "email": self.email,
#         })
#


# write

#     def save(self):
#         with open("users.txt", "a") as f:
#             f.write(self.id,)

#read

#     @staticmethod
#     def load():
#         return map(User.from_json, eval(open("users").read())

#    @staticmethod
#    def all(users):
#        with open("users", "w") as f:
#            f.write(str(map(User.to_json, users)))

class User:
    'a user'

    def __init__(self, name, email, phone, password):
        self.name = name
        self.email = email
        self.phone = phone
        self.password = password
        self.houseCode = None

    def setCode(self, newCode):
        self.houseCode = newCode

    # dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};

    def to_json(self):
        return json.dumps(self.__dict__)


class Chore:
    'a single chore in a household'

    # String name, int days per reset
    def __init__(self, name, dpr):
        self.name = name
        self.dpr = dpr
        self.lastDone = None
        self.currentUser = None

    def to_json(self):
        return json.dumps(self.__dict__)

class HouseHold:
    'a full household'

    def __init__(self, code, numPeople):
        self.houseCode = code
        self.numPeople = numPeople
        self.chores = [] # list of chores
        self.people = [] # list of names
        self.started = False

    def choreDict(self):
        people_dict = "{"
        for user in self.people:
            chores = str(self.getUserChores(user.name))
            people_dict += ("\'" + user.name + "\': " + chores + ", ")
        people_dict = people_dict[:-2]
        people_dict += "}"
        return json.dumps(people_dict)

    # void adds chore, name and days per reset
    def addChore(self, name, dpr):
        newChore = Chore(name, dpr)
        self.chores.append(newChore)

    # void adds user
    def addUser(self, user):
        if self.numPeople > len(self.people):
            self.people.append(user)

    # returns boolean
    def startHouse(self):
        # checks house start is valid
        if (len(self.people) == self.numPeople) and not self.started:
            assigned = False
            choresAssigned = 0
            while (choresAssigned < len(self.chores)):
                for x in self.people:
                    if (choresAssigned < len(self.chores)):
                        today = datetime.now()
                        self.chores[choresAssigned].currentUser = x.name
                        self.chores[choresAssigned].lastDone = today
                        choresAssigned += 1
            self.started = True
            return True
        else:
            return False

    # String representing the chore -> void (move the chore to the next person)
    def doChore(self, chore):
        oldUser = "" #string
        oldUserPlace = -1 #user order place
        choreNum = -1 #indicy
        # for each chore, find the chore num and get the old user
        for x in range(0, len(self.chores)):
            if (self.chores[x].name == chore):
                oldUser = self.chores[x].currentUser
                choreNum = x

        # if not error, get the user place
        if (oldUser != -1):
            for y in range(0, len(self.people)):
                if (self.people[y].name == oldUser):
                    oldUserPlace = y

        # if not error, move the user
        if (oldUserPlace != -1):
            if oldUserPlace == (len(self.people) - 1):
                self.chores[choreNum].currentUser = self.people[0].name
            else:
                self.chores[choreNum].currentUser = self.people[oldUserPlace + 1].name


    # User Name -> List of Chores For Person
    def getUserChores(self, user):
        userChores = []
        for chore in self.chores:
            if (chore.currentUser == user):
                userChores.append(chore.name)
        return userChores

    def compareDates(date1, date2):
        # TODO which came first
        return relativedelta.relativedelta(date1, date2).days

    # Return the list of chores sorted by time
    def choresByTime(self):
        self.chores.sort(compareDates)
        return self.chores

    # String representing the chore -> number
    def daysLeftForChore(self, chore):
        for c in self.chores:
            if(c.name == chore):
                today = datetime.datetime.now()
                return self.compareDates(today, c.lastDone)

    # User Name -> List of Chores For Person Immediatly Before
    def userBeforeChores(self, user):
        if user == self.people[0].name:
            return getUserChores(self.people[len(self.people) - 1].name)
        else:
            for x in range(1, len(self.people)):
                if self.people[x].name == user:
                    return getUserChores(self.people[x - 1].name)

    def to_json(self):
        return json.dumps(self.__dict__)

class Model:
    'represents all the data in the application so far'

    def __init__(self):
        self.users = []
        self.households = []

    def createUser(self, name, email, phone, password):
        newUser = User(name, email, phone, password)
        self.users.append(newUser);

    # sets the string house code of a string user to the given code
    def setHouseCode(self, user, code):
        for x in self.users:
            if x.name == user:
                x.setCode(code)

    def createHouse(self, code, numPeople):
        newHouse = HouseHold(code, numPeople)
        self.households.append(newHouse)

    def getHouse(self, code):
        for h in self.households:
            if h.houseCode == code:
                return h
        return False

    def to_json(self):
        return json.dumps(self.__dict__)