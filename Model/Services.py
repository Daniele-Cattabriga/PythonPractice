from Data import Data
from Banking.Account import Account
from People.BankUser import BankUser
class Services:

    def __init__(self):
        self.dataset=Data()

    def createAccount(self, **kwargs ):
        self.dataset.addAccount(Account(BankUser(kwargs["name"], kwargs["surname"], kwargs["SSN"], kwargs["birthdate"])
                                        ,kwargs["AccountID"],kwargs["password"],kwargs["IBAN"], kwargs["balance"]))

    def deleteAccount(self, AccountID:str):
        self.dataset.deleteAccount(AccountID)

    def getAccount(self, AccountID:str):
        self.dataset.getAccount(AccountID)

    def updateAccount(self, AccountID:str, **kwargs):
        UpdatingAccount = self.dataset.getAccount(AccountID)
        if UpdatingAccount is not None:
            # this process completely violates encapsulation principle in OOP. Although slower to implement with
            # the given restrictions, a better solution would be to recreate the object using data parsed from the
            # datadump, and re-inject it in the dataset through the update method. an example of such operation,
            # with a single argument, will be provided at the end of the function through comment
            for query in kwargs:
                if query == "password":
                    UpdatingAccount.password=kwargs[query]
                elif query=="IBAN":
                    UpdatingAccount.IBAN=kwargs[query]
                elif query=="balance":
                    UpdatingAccount.balance=kwargs[query]
            self.dataset.updateAccount(UpdatingAccount)

            # How would we do if we were to follow the encapsulation principle (i.e. protected variations, don't talk to
            # strangers)?

            # Say, for example, that kwargs contains a single value, and that value is "IBAN". What we would do is
            """
            UpdatingAccount.login("bankmasterpass")                 First we log in the account using the masterpass
            datadump=UpdatingAccount.readoutInKwarg()               Then we would dump the readout in a variable
            ParsedUserData=datadump[userData].split(",")            Then we would create the array with the data
                                                                    needed to recreate the user in the account by
                                                                    splitting by , the value of userData in the dict
            UpdatingAccount.logout()                                We then logout the account 
            if query == "IBAN":                                     Self explanatory and true by definition
            self.dataset.updateAccount(                             Then we recreate the account, maintaining 
                Account(                                            unmodified data and injecting the modified 
                    BankUser(                                       parts, and use it as argument to the updateAccount
                        ParsedUserData[0],ParsedUserData[1],        function in the dataset
                        ParsedUserData[2],ParsedUserData[5]
                    ),
                datadump["AccountID"],
                datadump["password"],
                kwargs["IBAN"],
                datadump["balance"]
                )
            )
            
            
            """

    def login(self, AccountID:str, password:str):
        account= self.dataset.getAccount(AccountID)
        if account is not None:
            account.login()
            self.dataset.updateAccount(account)
        else:
            print("Account does not exist!")

    def logout(self, AccountID:str):
        account=self.dataset.getAccount(AccountID)
        if account is not None:
            account.logout()
            self.dataset.updateAccount(account)
        else:
            print("Account does not exist!")

    def transaction(self, AccountID:str, amount:float):
        account=self.dataset.getAccount(AccountID)
        if account is not None:
            account.transaction(amount)
            self.dataset.updateAccount(account)
        else:
            print("Account does not exist!")



