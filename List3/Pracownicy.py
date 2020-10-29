from abc import ABC, abstractmethod
from Ludzie import Osoba


class PracownikPwr(Osoba):

    @abstractmethod
    def __init__(self, name, surname, pesel, gender, yearOfStart):
        super().__init__(name, surname, pesel, gender)
        self._yearOfStart = yearOfStart

    @property
    def yearOfStart(self):
        return self.__yearOfStart

    @yearOfStart.setter
    def yearOfStart(self, newYearOfStart):
        self.__yearOfStart = newYearOfStart

    @abstractmethod
    def printData(self):
        super().printData()
        print("rok zaczecia pracy " + str(self.yearOfStart))

class PracownikAdministracyjny(PracownikPwr):

    def __init__(self, name, surname, pesel, gender, yearOfStart, department):
        super().__init__(name, surname, pesel, gender, yearOfStart)
        self.__department = department

    @property
    def department(self):
        return self.__department

    @department.setter
    def department(self, newDepartment):
        self.__department = newDepartment

    def printData(self):
        super().printData()
        print("dzial " + self.department + "\n")

class PracownikNaukowy(PracownikPwr):
    def __init__(self, name, surname, pesel, gender, yearOfStart, domain):
        super().__init__(name, surname, pesel, gender, yearOfStart)
        self.__domain = domain

    @property
    def domain(self):
        return self.__domain

    @domain.setter
    def department(self, newDomain):
        self.__domain = newDomain

    def printData(self):
        super().printData()
        print("dziedzina " + self.domain + "\n")