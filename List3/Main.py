from Ludzie import Osoba
from Uczniowie import Student
from Pracownicy import PracownikPwr, PracownikAdministracyjny, PracownikNaukowy
import PeopleDatabase
import pickle

if __name__ == '__main__':
    stud = Student("Marcin", "Nahajowski", '98082700958', "mezczyzna", 3, 5.01, "informatyka")
    stud.printData()
    prac1 = PracownikNaukowy("Harry", "Pajac", '68051100657', "mezczyzna", 2000, "Bazy danych")
    prac1.printData()

    stud1 = Student("Pawel", "Nowak", '97082700565', "mezczyzna", 2, 4.81, "informatyka")
    stud2 = Student("Michal", "Morski", '98082700465', "mezczyzna", 2, 4.17, "informatyka")
    stud3 = Student("Marcin", "Osadcow", '98082700365', "mezczyzna", 2, 4.665, "informatyka")
    stud4 = Student("Kamil", "Kaminski", '98082700265', "mezczyzna", 2, 4.89, "informatyka")
    stud5 = Student("Bartosz", "Bąk", '98082700165', "mezczyzna", 2, 5.11, "informatyka")
    stud6 = Student("Jan", "Lewandowski", '98082700765', "mezczyzna", 2, 4.43, "informatyka")
    stud7 = Student("Karol", "Mielcarek", '98082700665', "mezczyzna", 2, 3.70, "informatyka")
    stud8 = Student("Adam", "Panczyszyn", '98082700568', "mezczyzna", 2, 4.12, "informatyka")
    stud9 = Student("Piotr", "Poziomek", '97082700565', "mezczyzna", 2, 4.42, "informatyka")
    stud10 = Student("Pawel", "Konter", '98081700565', "mezczyzna", 2, 3.89, "informatyka")

    people = [stud1, stud2, stud3, stud4, stud5, stud6, stud7, stud8, stud9, stud10, prac1]

    for key in PeopleDatabase.actions:
        print(key, '=>', PeopleDatabase.actions[key].__name__)




    selectedAction = input("Please select an action from the menu: ")
    while selectedAction != '0':
        PeopleDatabase.actions.get(selectedAction, PeopleDatabase.errorHandler)(people)
        selectedAction = input("Please select an action from the menu: ")


    choose = PeopleDatabase.inputInteger("Do you want to import data? 1- YES ")

    if choose == 1:
        path = input("Please select name of the data ")

        try:
            newPeople = pickle.load(open(path, 'rb'))
            print("Data loaded")
            PeopleDatabase.printAllPeople(newPeople)
        except Exception:
            print("File does not exist")
