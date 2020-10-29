import tabulate

studentsDatabase = [
    {
        'imie': "Pawel",
        'nazwisko': "Nowak",
        'PESEL': '97082700565',
        'plec': "mezczyzna",
        'rok studiow': 2,
        'srednia ocen': 4.81,
        'kierunek studiow': "informatyka"
    },
    {
        'imie': "Michal",
        'nazwisko': "Morski",
        'PESEL': "98082700465",
        'plec': "mezczyzna",
        'rok studiow': 2,
        'srednia ocen': 4.17,
        'kierunek studiow': "informatyka"
    },
    {
        'imie': "Marcin",
        'nazwisko': "Osadcow",
        'PESEL': "98082700365",
        'plec': "mezczyzna",
        'rok studiow': 2,
        'srednia ocen': 4.665,
        'kierunek studiow': "informatyka"
    },
    {
        'imie': "Kamil",
        'nazwisko': "Kaminski",
        'PESEL': "98082700265",
        'plec': "mezczyzna",
        'rok studiow': 2,
        'srednia ocen': 4.89,
        'kierunek studiow': "informatyka"
    },
    {
        'imie': "Bartosz",
        'nazwisko': "Bąk",
        'PESEL': "98082700165",
        'plec': "mezczyzna",
        'rok studiow': 2,
        'srednia ocen': 5.11,
        'kierunek studiow': "informatyka"
    },
    {
        'imie': "Jan",
        'nazwisko': "Lewandowski",
        'PESEL': "98082700765",
        'plec': "mezczyzna",
        'rok studiow': 2,
        'srednia ocen': 4.43,
        'kierunek studiow': "informatyka"
    },
    {
        'imie': "Karol",
        'nazwisko': "Mielcarek",
        'PESEL': "98082700665",
        'plec': "mezczyzna",
        'rok studiow': 2,
        'srednia ocen': 3.70,
        'kierunek studiow': "informatyka"
    },
    {
        'imie': "Adam",
        'nazwisko': "Panczyszyn",
        'PESEL': "98082700568",
        'plec': "mezczyzna",
        'rok studiow': 2,
        'srednia ocen': 4.12,
        'kierunek studiow': "informatyka"
    },
    {
        'imie': "Piotr",
        'nazwisko': "Poziomek",
        'PESEL': "98082700165",
        'plec': "mezczyzna",
        'rok studiow': 2,
        'srednia ocen': 4.42,
        'kierunek studiow': "informatyka"
    },
    {
        'imie': "Pawel",
        'nazwisko': "Konter",
        'PESEL': "98081700565",
        'plec': "mezczyzna",
        'rok studiow': 2,
        'srednia ocen': 3.89,
        'kierunek studiow': "informatyka"
    }
]


def printAllStudents():
    header = studentsDatabase
    rows = [x.values() for x in studentsDatabase]
    print(tabulate.tabulate(rows, header))
    #print(studentsDatabase)


def printAllStudentsSortedBySurname():
    print(sorted(studentsDatabase, key=lambda k: k['nazwisko']))


def printAllStudentSortedByAverage():
    print(sorted(studentsDatabase, key=lambda k: k['srednia ocen'], reverse=True))


def findStudentInDatabase():
    print("Enter PESEL of the student you want to find ")
    findPESEL = input()
    print(list(filter(lambda person: person['PESEL'] == findPESEL, studentsDatabase)))


def deleteStudentFromDatabase():
    global studentsDatabase
    print("Enter PESEL of the student you want to delete ")
    peselUcznia = input()
    new_list = [i for i in studentsDatabase if i['PESEL'] != peselUcznia]
    studentsDatabase = new_list
    print(f"Student with PESEL {peselUcznia} successfully deleted ")


def copyDatabaseWithWantedAverage():
    sredniaOcen = inputFloat("Enter maximum average allowed ")
    uczniowieSrednia = list(filter(lambda person: person['srednia ocen'] < sredniaOcen, studentsDatabase))
    choose = inputInteger("Do you want to display values? 1 - TAK ")
    if choose == 1:
        print(uczniowieSrednia)


def addStudent():
    newStudent = {}
    print("Enter name")
    newStudent['imie'] = input()
    print("Enter surname")
    newStudent['nazwisko'] = input()
    print("Enter PESEL")
    newStudent['PESEL'] = input()
    print("Enter sex")
    newStudent['plec'] = input()
    newStudent['rok studiow'] = inputInteger("Enter year of studies\n")
    newStudent['srednia ocen'] = inputFloat(("Enter average\n"))
    print("Enter what is he studying")
    newStudent['kierunek studiow'] = input()
    studentsDatabase.append(newStudent)
    print(newStudent)


def inputInteger(message):
    while True:
        try:
            userInput = int(input(message))
        except ValueError:
            print("Not an integer! Try again.")
        else:
            return userInput


def inputFloat(message):
    while True:
        try:
            userInput = float(input(message))
        except ValueError:
            print("Not a float! Try again.")
        else:
            return userInput

def exitProgram():
    print("Leaving the database...")

def errorHandler():
    print("Invalid number")


actions = {'1': printAllStudents,
           '2': printAllStudentsSortedBySurname,
           '3': printAllStudentSortedByAverage,
           '4': findStudentInDatabase,
           '5': deleteStudentFromDatabase,
           '6': copyDatabaseWithWantedAverage,
           '7': addStudent,
           '0': exitProgram}

if __name__ == "__main__":

    for key in actions:
        print(key, '=>', actions[key].__name__)

    selectedAction = input("Plesase select an action from the menu: ")
    while selectedAction != '0':
        actions.get(selectedAction, errorHandler)()
        selectedAction = input("Please select an action from the menu: ")
