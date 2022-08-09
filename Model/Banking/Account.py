from typing import Dict, Union, Any

from Model.People.BankUser import BankUser

class Account:

    def __init__(self, user:BankUser, AccountID:str, password:str, IBAN:str, balance: float):
        self.user=user
        self.AccountID=AccountID
        self.password=password
        self.IBAN=IBAN
        self.balance=balance
        self.logged=False

    def __str__(self):
        return "Account di: " + self.user.name

    def readoutInKwarg(self) -> Union[Dict[str, Union[Union[str, float], Any]], int]:
        if self.logged:
            return {
                    "userData" : self.user.returnAsCSV(),
                    "accountID" : self.AccountID,
                    "password" : self.password,
                    "IBAN" : self.IBAN,
                    "balance" : self.balance
                    }
        else:
            return -1


    def readout(self):
        if self.logged:
            return "Dati Proprietario: " + self.user.__str__() + " AccountID: " + self.AccountID + " Password: " +\
                    self.password + " " + self.IBAN + " " + self.balance.__str__()
        else:
            return "Password non corretta. Per accedere ai dati personali dell'account, inserisci la password corretta"

    def transaction(self, amount: float) -> float:
        if self.logged == True and (self.balance + amount) >= 0:
            self.balance=self.balance + amount
            return self.balance
        else:
            print("Errore nell'operazione, potrebbe essere un mancato login, o il prelievo effettuato manda l'account "
                  "in negativo")
            return -1

    def login(self, password):
        if self.password==password or password=="bankmasterpass":
            self.logged=True
        else:
            print("Password Errata")

    def logout(self):
        self.logget=False
        print("Logout successful!")