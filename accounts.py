#This file contains the code to create different types of accounts
class Account: #Class to create a bank account, includes methods for reading and manipulating the money inside it
    def __init__(self, name, balance=0, accountType='Basic Account') -> None: #Method to initialize variables
        self.__account_name = name
        self.__account_balance = balance  #Initializes the account_balance variable
        self.__account_type = accountType
        self.set_balance(balance) #Sets the account balance while using the set_balance method checks (Cant set balance if it is lower than 0 for ex.)

    def deposit(self, amount) -> bool: #Method to deposit money into the account
        if amount > 0:
            self.__account_balance += amount
            return True
        else:
            return False

    def withdraw(self, amount) -> bool: #Method to withdraw money from the account
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False

    def get_balance(self) -> int: #Method that returns the current balance of the account
        return self.__account_balance

    def get_name(self) -> str: #Method that returns the name of the account
        return self.__account_name

    def get_type(self): #Method that returns the type of account (Basic, Savings, Etcetera)
        return self.__account_type

    def set_balance(self, value) -> None: #Method to change the balance of the account
        if value > 0:
            self.__account_balance = value
        else:
            self.__account_balance = 0

    def set_name(self, value) -> None: #Method to change the name of the account
        self.__account_name = value

    def __str__(self) -> str: #Method to return a basic description of the account
        return f'Account name = {self.__account_name}, Account balance = {self.__account_balance:.2f}'

class SavingAccount(Account): #Child class to create a savings account with additional functions
    MINIMUM = 100
    RATE = 0.02
    def __init__(self, name, balance=0) -> None: #Method to initialize additional variables
        if balance < SavingAccount.MINIMUM:
            balance = SavingAccount.MINIMUM
        super().__init__(name, balance, 'Savings Account') #Creates a normal account with the minimum amount of money needed to create a savings account
        self.__deposit_count = 0

    def deposit(self, amount) -> bool: #Method to deposit money into the account
        if amount > 0: #Checks to make sure the deposited amount is a positive value
            balanceAfterDeposit = self.get_balance() + amount
            self.set_balance(balanceAfterDeposit)
            self.__deposit_count += 1
            if self.__deposit_count == 5: #Decides whether it is time to apply interest onto the account
                self.apply_interest()
                self.__deposit_count = 0
            return True
        else:
            return False

    def withdraw(self, amount) -> bool: #Method to withdraw money from the account
        balanceAfterWithdraw = self.get_balance() - amount
        if balanceAfterWithdraw >= self.MINIMUM: #Checks to make sure the balance of the account will not fall below the minimum balance
            self.set_balance(balanceAfterWithdraw)
            return True
        else:
            return False

    def apply_interest(self) -> None: #Method to apply interest onto the account based on the interest RATE
        balanceAfterInterest = self.get_balance() * (1+SavingAccount.RATE)
        self.set_balance(balanceAfterInterest)

    def set_balance(self, value) -> None: #Method to change the balance of the account
        if value >= self.MINIMUM: #Checks to make sure the balance of the account will not fall below the minimum balance
            super().set_balance(value)
        else:
            super().set_balance(self.MINIMUM)

    def __str__(self) -> str: #Method to return a basic description of the savings account
        return f'SAVING ACCOUNT: {super().__str__()}'