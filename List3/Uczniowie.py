from Ludzie import Osoba


class Student(Osoba):

    def __init__(self, name, surname, pesel, gender, yearOfStudies, averageOfGrades, fieldOfStudy):
        super().__init__(name, surname, pesel, gender)
        self.__yearOfStudies = yearOfStudies
        self.__averageOfGrades = averageOfGrades
        self.__fieldOfStudy = fieldOfStudy

    @property
    def yearOfStudies(self):
        return self.__yearOfStudies

    @yearOfStudies.setter
    def yearOfStudies(self, newYearOfStudies):
        self.__yearOfStudies = newYearOfStudies

    @property
    def averageOfGrades(self):
        return self.__averageOfGrades

    @yearOfStudies.setter
    def yearOfStudies(self, newaverageOfGrades):
        self.__averageOfGrades = newaverageOfGrades

    @property
    def fieldOfStudy(self):
        return self.__fieldOfStudy

    @fieldOfStudy.setter
    def fieldOfStudy(self, newFieldOfStudy):
        self.__fieldOfStudy = newFieldOfStudy

    def printData(self):
        super().printData()
        print(str(self.yearOfStudies) + " rok studiow\tśrednia " + str(self.averageOfGrades) + "\tkierunek " + self.fieldOfStudy + "\n")

