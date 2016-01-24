from time import gmtime, strftime

from datetime import datetime
from dateutil import relativedelta

class User:
    'a user'
    userNum = 1001

    def __init__(self, email, phone, password):
        self.id = User.userNum
        self.email = email
        self.phone = phone
        self.password = password
        self.houseCode = None
        User.userNum += 1

    def setCode(self, newCode):
        self.houseCode = newCode

class Chore:
    'a single chore in a household'

    def __init__(self, name, desc, dpr):
        self.name = name
        self.desc = desc
        self.dpr = dpr
        self.lastDone = None
        self.currentUser = None

class HouseHold:
    'a full household'

    def __init__(self, code, numPeople):
        self.houseCode = code
        self.numPeople = numPeople
        self.chores = []
        self.people = []
        self.started = False

    # void adds chore
    def addChore(self, name, desc, dpr):
        newChore = Chore(name, desc, dpr)
        self.chores.append(newChore)

    # void adds user
    def addUser(self, userNum):
        if self.numPeople > len(self.people):
            self.people.append(userNum)

    # List of List of Ints representing
    def startHouse(self, groupings):
        # checks house start is valid
        if (len(self.people) == self.numPeople) and not self.started:
            for x in range(0, len(self.groupings):
                personid = self.people[x]
                for y in range(0, self.groupings[x]):
                    today = datetime.fromtimestamp(mktime(struct))
                    self.chores[self.groupings[x][y]].currentUser = personid
                    self.chores[self.groupings[x][y]].lastDone = today
                    self.started = True
                    return True
        else:
            return False

    # String representing the chore -> void (move the chore to the next person)
    def doChore(self, chore):
        oldUser = -1
        oldUserPlace = -1
        choreNum = -1
        for x in range(0, len(self.chores):
            if (self.chores[x].name == chore):
                oldUser = self.chores[x].currentUser
                choreNum = x

        if (oldUser != -1):
            for y in range(0, len(self.people):
                if (self.people[y] == oldUser):
                    oldUserPlace = y

        if (oldUserPlace != -1):
            if oldUserPlace == (len(self.people) - 1):
                self.chores[choreNum] = self.people[0]
            else:
                self.chores[choreNum] = self.people[oldUserPlace + 1]




    # User ID Number -> List of Chores For Person
    def getUserChores(self, user):
        userChores = []
        for chore in self.chores:
            if (chore.currentUser == user)
                userChores.append(chore)
        return userChores

    def __compareDates

    # Return the list of chores sorted by time
    def choresByTime(self):

    # String representing the chore -> boolean
    def daysLeftForChore(self, chore):
    # TODO Calculate Date Code



    # User ID Number -> List of Chores For Person Immediatly Before
    def userBeforeChores(self, user):
        if user == (len(self.people) - 1):
            return getUserChores(self.people[0])
        else:
            return getUserChores(user + 1)



class Model:
    'represents all the data in the application'

    def __init__(self):
        self.users = []
        self.households = []

    def createUser(self, email, phone, password):
        newUser = User(email, phone, password)
        self.users.append(newUser);

    def setHouseCode(self, user, code):
        self.users[user - 1001].setCode(code)

    def createHouse(self, code, numPeople):
        newHouse = HouseHold(code, numPeople)
        self.households.append(newHouse)

    def getHouse(self, code):
        for x in range(0, len(households)):
            if self.households[x].houseCode == code:
                return self.households[x]
        return False