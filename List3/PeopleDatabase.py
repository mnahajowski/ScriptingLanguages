from Uczniowie import Student
import pickle


def printAllPeople(people: list):
    for key in people:
        print(people.index(key) + 1)
        key.printData()


def printAllStudentsSortedBySurname(people: list):
    people.sort(key=lambda k: k.surname)
    printAllPeople(people)


def printAllStudentSortedByAverage(people: list):
    people.sort(key=lambda k: k.averageOfGrades)
    printAllPeople(people)


def findStudentInDatabase(people: list):
    print("Enter PESEL of the student you want to find ")
    findPESEL = input()
    printAllPeople(list(filter(lambda person: person.pesel == findPESEL, people)))


def deleteStudentFromDatabase(people: list):
    print("Enter PESEL of the student you want to delete ")
    peselUcznia = input()
    new_list = [i for i in people if i.pesel != peselUcznia]
    people[:] = new_list
    print(f"Student with PESEL {peselUcznia} successfully deleted ")


def exitProgram():
    print("Leaving the database...")


def copyDatabaseWithWantedAverage(people: list):
    sredniaOcen = inputFloat("Enter maximum average allowed ")

    uczniowieSrednia = [student for student in
                        (person for person in people if isinstance(person, Student))
                        if student.averageOfGrades < sredniaOcen]
    choose = inputInteger("Do you want to display values? 1 - TAK ")
    if choose == 1:
        printAllPeople(uczniowieSrednia)


def addStudent(people: list):
    print("Enter name")
    newName = input()
    print("Enter surname")
    newSurname = input()
    print("Enter PESEL")
    newPesel = input()
    print("Enter gender")
    newGender = input()
    newYearOfStudies = inputInteger("Enter year of studies\n")
    newAverageOfGrades = inputFloat(("Enter average\n"))
    print("Enter what is he studying")
    newFieldOfStudy = input()
    newStudent = Student(newName, newSurname, newPesel, newGender, newYearOfStudies, newAverageOfGrades,
                         newFieldOfStudy)
    people.append(newStudent)
    print("Student successfully added")
    newStudent.printData()


def saveToFile(people : list):
    pickle.dump(people, open('peopleData', 'wb'))
    print("Data successfully saved")


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


actions = {'1': printAllPeople,
           '2': printAllStudentsSortedBySurname,
           '3': printAllStudentSortedByAverage,
           '4': findStudentInDatabase,
           '5': deleteStudentFromDatabase,
           '6': copyDatabaseWithWantedAverage,
           '7': addStudent,
           '8': saveToFile,
           '0': exitProgram}


def errorHandler():
    print("Invalid number")
