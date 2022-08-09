from datetime import date
class Person(object):

    def __init__(self, name : str, surname : str, SSN : str, birthdate : date):
        self.name = name
        self.surname = surname
        self.SSN = SSN
        self.birthdate = birthdate

    def __str__(self):
        return self.name + " " + self.surname + " " + self.SSN + " " + self.birthdate.__str__()

    def returnAsCSV(self) -> str:
        return self.name + "," + self.surname + "," + self.SSN + "," + self.birthdate.__str__()
