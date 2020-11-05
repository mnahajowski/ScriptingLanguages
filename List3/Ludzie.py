from abc import ABC, abstractmethod


class Osoba(ABC):

    @abstractmethod
    def __init__(self, name, surname, pesel, gender):
        self.__name = name
        self.__surname = surname
        self.__pesel = pesel
        self.__gender = gender

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, newName):
        self.__name = newName

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, newSurname):
        self.__surname = newSurname

    @property
    def pesel(self):
        return self.__pesel

    @pesel.setter
    def pesel(self, newPesel):
        self.__pesel = newPesel

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, newGender):
        self.__gender = newGender

    @abstractmethod
    def printData(self):
        print(self.name + " " + self.surname + " " + self.pesel + " " + self.gender)
