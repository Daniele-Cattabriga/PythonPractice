from datetime import date
from Person import Person

class BankEmployee(Person):

    def __init__(self, name : str, surname : str, SSN : str, birthdate : date, ID:str):
        super().__init__(name , surname , SSN , birthdate)
        self.ID = ID

    def __str__(self):
        return super().__str__() + " " + self.ID

    def returnAsCSV(self) -> str:
        return super().returnAsCSV() + "," + self.ID