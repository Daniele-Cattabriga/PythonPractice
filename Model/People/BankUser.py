from datetime import date
from Person import Person

class BankUser(Person):

    def __init__(self, name : str, surname : str, SSN : str, birthdate : date):
        super().__init__(name , surname , SSN , birthdate)

    def __str__(self):
        return super().__str__()

    def returnAsCSV(self) -> str:
        return super().returnAsCSV()
