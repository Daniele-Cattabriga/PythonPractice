import csv
import os.path
from typing import Optional

from Model.Banking.Account import Account
from Model.People.BankUser import BankUser
import datetime
class Data:

    def __init__(self):
        if os.path.exists("dataSaved.csv"):
            data=open("dataSaved.csv", mode='r+')
            reader=csv.reader(data)
            self.accounts={}
            rownum=0
            for row in reader:
                if rownum>0:
                    self.accounts.update({str(row[5]): Account(BankUser(row[0], row[1], row[2],
                                                            datetime.datetime.strptime(row[3]).date()), row[5], row[6],
                                                            row[7], float(row[8]))})
                rownum=rownum+1
            reader=None
            data.close()
        else:
            print("No data file detected, instantiating empty account set and creating empty datafile")
            data=open("dataSaved.csv", mode='w+')
            data.close()
            self.accounts={}

    def getAccount(self, AccountID : str) -> Account:
        account = self.accounts[AccountID]
        if account is not None:
            return account
        else:
            return None

    def addAccount(self, Account : Account):
        self.accounts.update({Account.AccountID : Account})
        print("Account added successfully")

    def deleteAccount(self, AccountID:str):
        self.accounts.__delitem__(AccountID)
        print("Account deleted successfully!")

    def updateAccount(self, Account : Account):
        self.accounts.__delitem__(Account.AccountID)
        self.accounts.update({Account.AccountID : Account})
        print("Account updated successfully!")

    def downloadData(self):
        data2 = open("dataSaved2.csv" , mode="w+", newline='')
        writer=csv.DictWriter(data2, fieldnames=["userData","AccountID","password", "IBAN", "balance"])
        for Account in self.accounts.values():
           writer.writerow(Account.readoutInKwarg())
        data2.close()
        os.remove("dataSaved.csv")
        os.rename("dataSaved2.csv", "dataSaved.csv")


