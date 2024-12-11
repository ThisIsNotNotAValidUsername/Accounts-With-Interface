from tkinter import *
from accounts import *

class Gui:
    def __init__(self, root) -> None:
        #Creates an array to hold every account
        self.accounts = []
        self.selectedAccount = None

        #Creates the tkinter window
        self.root = root

        #Creates the frame that holds the account manager header
        self.frame_managerHeader = Frame(self.root)
        self.frame_managerHeader['borderwidth'] = 1
        self.frame_managerHeader['relief'] = 'solid'
        self.label_header1 = Label(self.frame_managerHeader, text='Account Manager')
        self.label_header1.configure(font=('Arial', 15))

        #Packs everything in the account manager header
        self.label_header1.pack()

        #Creates the frame that holds the account manager body (Holds the multiple different screens)
        self.frame_managerBody = Frame(self.root)
        self.frame_managerBody['borderwidth'] = 1
        self.frame_managerBody['relief'] = 'solid'

        #Creates the managerMenu frame which is the 'main screen' of the Account Manager
        self.frame_managerMenu = Frame(self.frame_managerBody)
        self.button_openManagerCreator = Button(self.frame_managerMenu, text="Create New Account", command=lambda: self.switchMenu("frame_managerMenu", "frame_managerCreator"))
        self.button_openManagerStatus = Button(self.frame_managerMenu, text="Select Account", command=self.displayAccount)
        #self.button_testButton = Button(self.frame_managerMenu, text='Test', command=self.updateAccountList)
        self.label_managerMenu1 = Label(self.frame_managerMenu, wraplength=200, text='Welcome to the Account Manager, if you already have an account, select it from the list on the right and then press "Select Account". If do not have an account or would like to make a new one, click "Create New Account" to make a new account.')

        #Packs everything in the managerMenu
        self.button_openManagerCreator.pack(pady=10)
        self.button_openManagerStatus.pack(pady=10)
        #self.button_testButton.pack()
        self.label_managerMenu1.pack(pady=50)

        #Creates the managerCreator frame which is the screen where you create new accounts for the Account Manager
        self.frame_managerCreator = Frame(self.frame_managerBody)
        self.label_managerCreator_1 = Label(self.frame_managerCreator, text='Making New Account')
        self.frame_managerCreator_1 = Frame(self.frame_managerCreator)
        self.label_managerCreator_2 = Label(self.frame_managerCreator_1, text='Name of Account: ')
        self.entry_managerCreator_accountName = Entry(self.frame_managerCreator_1)
        self.frame_managerCreator_2 = Frame(self.frame_managerCreator)
        self.label_managerCreator_3 = Label(self.frame_managerCreator_2, text='Balance of Account: ')
        self.entry_managerCreator_accountBalance = Entry(self.frame_managerCreator_2)
        self.label_managerCreator_4 = Label(self.frame_managerCreator, text='Type of Account: ')
        self.accountType = StringVar()
        self.accountType.set('BasicAccount')
        self.frame_managerCreator_3 = Frame(self.frame_managerCreator)
        self.radiobutton_managerCreator_accountBasic = Radiobutton(self.frame_managerCreator_3, variable=self.accountType, value='BasicAccount', text='Basic Account')
        self.radiobutton_managerCreator_accountSavings = Radiobutton(self.frame_managerCreator_3, variable=self.accountType, value='SavingsAccount', text='Savings Account')
        self.button_managerCreator_makeNewAccount = Button(self.frame_managerCreator, text="Create Account", command=self.makeNewAccount)
        self.button_managerCreator_openManagerMenu = Button(self.frame_managerCreator, text="Return To Main Menu", command=lambda: self.switchMenu("frame_managerCreator", "frame_managerMenu"))

        #Packs everything in managerCreator
        self.label_managerCreator_1.pack(padx=10, pady=5)
        self.label_managerCreator_2.pack(side='left', padx=10, pady=5)
        self.entry_managerCreator_accountName.pack(side='right', padx=10, pady=5)
        self.frame_managerCreator_1.pack(fill='x')
        self.label_managerCreator_3.pack(side='left', padx=10, pady=5)
        self.entry_managerCreator_accountBalance.pack(side='right', padx=10, pady=5)
        self.frame_managerCreator_2.pack(fill='x')
        self.label_managerCreator_4.pack(padx=10, pady=5)
        self.radiobutton_managerCreator_accountBasic.pack(side='left')
        self.radiobutton_managerCreator_accountSavings.pack(side='left')
        self.frame_managerCreator_3.pack(fill='x')
        self.button_managerCreator_makeNewAccount.pack(anchor='w', pady=30, padx=10)
        self.button_managerCreator_openManagerMenu.pack(anchor='w', padx=10)

        #Creates the managerStatus frame which shows the user details on an account and allows deposits, withdrawals and deletion of the selected account
        self.frame_managerStatus = Frame(self.frame_managerBody)
        self.frame_managerStatus_1 = Frame(self.frame_managerStatus)
        self.label_managerStatus_1 = Label(self.frame_managerStatus_1, text='Name of Account: ')
        self.label_managerStatus_accountName = Label(self.frame_managerStatus_1, text='N/A')
        self.frame_managerStatus_2 = Frame(self.frame_managerStatus)
        self.label_managerStatus_2 = Label(self.frame_managerStatus_2, text='Type of Account: ')
        self.label_managerStatus_accountType = Label(self.frame_managerStatus_2, text='N/A')
        self.frame_managerStatus_3 = Frame(self.frame_managerStatus)
        self.label_managerStatus_3 = Label(self.frame_managerStatus_3, text='Account Balance: ')
        self.label_managerStatus_accountBalance = Label(self.frame_managerStatus_3, text='N/A')
        self.frame_managerStatus_4 = Frame(self.frame_managerStatus)
        self.button_managerStatus_1 = Button(self.frame_managerStatus_4, text='Deposit Money', command=self.deposit_money)
        self.entry_managerStatus_1 = Entry(self.frame_managerStatus_4)
        self.frame_managerStatus_5 = Frame(self.frame_managerStatus)
        self.button_managerStatus_2 = Button(self.frame_managerStatus_5, text='Withdraw Money', command=self.withdraw_money)
        self.entry_managerStatus_2 = Entry(self.frame_managerStatus_5)
        self.frame_managerStatus_6 = Frame(self.frame_managerStatus)
        self.button_managerStatus_3 = Button(self.frame_managerStatus_6, text='Change Account Name', command=self.change_account_name)
        self.entry_managerStatus_3 = Entry(self.frame_managerStatus_6)
        self.button_managerStatus_deleteAccount = Button(self.frame_managerStatus, text='Delete Selected Account', command=self.delete_account)
        self.button_managerStatus_openManagerMenu = Button(self.frame_managerStatus, text="Return To Main Menu", command=lambda: self.switchMenu("frame_managerStatus", "frame_managerMenu"))

        #Packs everything in managerStatus
        self.label_managerStatus_1.pack(side='left', padx=10, pady=5)
        self.label_managerStatus_accountName.pack(side='right', padx=10, pady=5)
        self.frame_managerStatus_1.pack(fill='x')
        self.label_managerStatus_2.pack(side='left', padx=10, pady=5)
        self.label_managerStatus_accountType.pack(side='right', padx=10, pady=5)
        self.frame_managerStatus_2.pack(fill='x')
        self.label_managerStatus_3.pack(side='left', padx=10, pady=5)
        self.label_managerStatus_accountBalance.pack(side='right', padx=10, pady=5)
        self.frame_managerStatus_3.pack(fill='x')
        self.button_managerStatus_1.pack(side='left', padx=10, pady=5)
        self.entry_managerStatus_1.pack(side='right', padx=10, pady=5)
        self.frame_managerStatus_4.pack(fill='x')
        self.button_managerStatus_2.pack(side='left', padx=10, pady=5)
        self.entry_managerStatus_2.pack(side='right', padx=10, pady=5)
        self.frame_managerStatus_5.pack(fill='x')
        self.button_managerStatus_3.pack(side='left', padx=10, pady=5)
        self.entry_managerStatus_3.pack(side='right', padx=10, pady=5)
        self.frame_managerStatus_6.pack(fill='x')
        self.button_managerStatus_deleteAccount.pack(pady=30, anchor='w', padx=10)
        self.button_managerStatus_openManagerMenu.pack(anchor='w', padx=10)

        #Packs the manager frames into managerBody and forgets all but 1 of them (the main screen)
        self.frame_managerMenu.pack()
        self.frame_managerCreator.pack()
        self.frame_managerStatus.pack()

        self.frame_managerCreator.pack_forget()
        self.frame_managerStatus.pack_forget()

        #Creates the frame that holds the accounts header
        self.frame_accountsHeader = Frame(self.root)
        self.frame_accountsHeader['borderwidth'] = 1
        self.frame_accountsHeader['relief'] = 'solid'
        self.label_header2 = Label(self.frame_accountsHeader, text='Accounts')
        self.label_header2.configure(font=('Arial', 15))

        #Packs everything in the accounts header
        self.label_header2.pack()

        #Creates the frame that holds the accounts body
        self.frame_accountsBody = Frame(self.root)
        self.frame_accountsBody['borderwidth'] = 1
        self.frame_accountsBody['relief'] = 'solid'
        self.scrollbar_accounts = Scrollbar(self.frame_accountsBody, orient="vertical")
        self.listbox_accounts = Listbox(self.frame_accountsBody, yscrollcommand = self.scrollbar_accounts.set)

        self.scrollbar_accounts.pack(side='right', fill='y')
        self.listbox_accounts.pack(side='left', fill='both', expand=True)

        #Packs the prepared frames into a grid for ease of placement
        self.frame_managerHeader.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)
        self.frame_managerBody.grid(row=1, column=0, sticky='nsew', padx=5, pady=5)
        self.frame_accountsHeader.grid(row=0, column=1, sticky='nsew', padx=5, pady=5)
        self.frame_accountsBody.grid(row=1, column=1, sticky='nsew', padx=5, pady=5)

        #Makes the grid expand as the window expands
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=9)
        self.root.grid_columnconfigure(0, weight=5)
        self.root.grid_columnconfigure(1, weight=2)

        self.startup()

    def startup(self) -> None: #Function ran the moment the program starts to load up some 'default' accounts
        account0 = Account('John', 520)
        account1 = Account('Davidson', 20040)
        account2 = SavingAccount('Hartley', 800)
        self.accounts.append(account0)
        self.accounts.append(account1)
        self.accounts.append(account2)
        self.updateAccountList()

    def switchMenu(self, currentMenu, wantedMenu) -> None: #Swaps the menu your on
        self.updateAccountList()
        exec(f"self.{currentMenu}.pack_forget()")
        exec(f"self.{wantedMenu}.pack()")

    def listAccount(self, accountName) -> None: #Adds the name of an account to the listbox
        self.listbox_accounts.insert(END, accountName)

    def unlistAccount(self) -> None: #Removes the name of an account in the listbox
        selection = self.listbox_accounts.curselection()
        if selection:
            self.listbox_accounts.delete(selection[0])

    def updateAccountList(self) -> None: #Updates the list of accounts on the right side of the screen
        self.listbox_accounts.delete(0, END)
        for item in self.accounts:
            self.listbox_accounts.insert(END, item.get_name())

    def makeNewAccount(self) -> None: #Function to create a new account
        account_name = self.entry_managerCreator_accountName.get()
        account_balance = self.entry_managerCreator_accountBalance.get()
        try:
            account_balance = float(account_balance)
        except ValueError:
            print(f'Warning: {account_balance} could not be converted to a float')
            return
        if self.accountType.get() == 'BasicAccount':
            exec(f'Account{len(self.accounts)} = Account("{account_name}", {account_balance})')
        elif self.accountType.get() == 'SavingsAccount':
            exec(f'Account{len(self.accounts)} = SavingAccount("{account_name}", {account_balance})')
        else:
            print(f'Warning: accountType not found, {self.accountType.get()} is not a valid account type')
        exec(f'self.accounts.append(Account{len(self.accounts)})')
        self.listAccount(f'{account_name}')
        self.entry_managerCreator_accountName.delete(0, END)
        self.entry_managerCreator_accountBalance.delete(0, END)
        self.accountType.set('BasicAccount')
        self.entry_managerCreator_accountName.focus()

    def selectAccount(self): #Function that selects the account the user has clicked on in the account list
        try:
            selection = int(list(self.listbox_accounts.curselection())[0])  #The listbox.curselection returns a tuple, this converts the tuple into a list, then a string, then an integer.
            try:
                self.selectedAccount = self.accounts[selection]
            except TypeError:
                print('No account is selected, please select an account')
            return selection
        except IndexError:
            print('Error: Selected account is not within range')

    def displayAccount(self, selectedAccount=None) -> None: #This function displays an account when the user presses 'Select Account', displaying general information on the account
        self.selectAccount()
        if self.selectedAccount is not None:
            selectedAccount = self.selectedAccount
        else:
            return
        self.switchMenu("frame_managerMenu", "frame_managerStatus")
        self.label_managerStatus_accountName.configure(text=selectedAccount.get_name())
        self.label_managerStatus_accountType.configure(text=selectedAccount.get_type())
        self.label_managerStatus_accountBalance.configure(text=selectedAccount.get_balance())
        self.entry_managerStatus_1.delete(0, END)
        self.entry_managerStatus_2.delete(0, END)
        self.entry_managerStatus_3.delete(0, END)
        self.entry_managerStatus_1.focus()

    def deposit_money(self) -> None: #Function to deposit money into the selected account
        amount = self.entry_managerStatus_1.get()
        try:
            amount = float(amount)
        except ValueError:
            print('Please enter a float only')
        self.selectedAccount.deposit(amount)
        self.displayAccount(self.selectedAccount)

    def withdraw_money(self) -> None: #Function to withdraw money form the selected account
        amount = self.entry_managerStatus_2.get()
        try:
            amount = float(amount)
        except ValueError:
            print('Please enter a float only')
        self.selectedAccount.withdraw(amount)
        self.displayAccount(self.selectedAccount)

    def change_account_name(self) -> None: #Function to change the name of the selected account
        newName = self.entry_managerStatus_3.get()
        self.selectedAccount.set_name(newName)
        self.displayAccount(self.selectedAccount)

    def delete_account(self) -> None: #Function to delete the selected account
        if self.selectedAccount is not None:
            pass
        else:
            return
        index = self.accounts.index(self.selectedAccount)
        del self.accounts[index]
        self.switchMenu("frame_managerStatus", "frame_managerMenu")