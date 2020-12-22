"""
Name             : Akshay S. Sangar
Emp_Id           : 214925
Application Name : Bank Management System
"""


import sys


class Account:

    account_number = []
    name = []
    mobile_no = []
    balance = []
    data = {'Customer_Name': name, 'Account': account_number,  'Balance': balance, 'Mobile_No': mobile_no}

    # Function for vreating new account
    def create_account(self, name1, acc_number2, mbl_no1, bal1):
        self.name.append(name1)
        self.account_number.append(acc_number2)
        self.mobile_no.append(mbl_no1)
        self.balance.append(bal1)

    # Function for displaying all records
    def display_all_records(self):
        print(self.data)
        return self.data

    # Function for diplaying record by account number
    def display_by_account_number(self, acc_number3):
        data_bank = {}
        for i in range(0, len(self.account_number)):
            if acc_number3 == self.account_number[i]:
                data_bank['Customer_Name'] = self.data['Customer_Name'][i]
                data_bank['Account'] = self.data['Account'][i]
                data_bank['Balance'] = self.data['Balance'][i]
                data_bank['Mobile_No'] = self.data['Mobile_No'][i]
                print(data_bank)
                return data_bank

    # Function for adding amount into balance
    def credit(self, acc_number4, amount2):
        for i in range(0, len(self.account_number)):
            if acc_number4 == self.account_number[i]:
                self.balance[i] = int(self.balance[i])+int(amount2)
                return self.balance[i]

    # Function for withdraw amount from current balance balance
    def debit(self, acc_number5, amount3):
        for i in range(0, len(self.account_number)):
            if acc_number5 == self.account_number[i]:
                self.balance[i] = int(self.balance[i]) - int(amount3)
                return self.balance[i]


if __name__ == "__main__":
    s = Account()
    # Continue while loop
    while True:
        print('1. Create Account\n2. Display Record\n3. Credit Amount\n4. Debit')
        ch = int(input())
        if ch == 1:
            print('Enter name : ')
            name = input()
            print('Enter Account Number')
            acc_number = input()
            print('Enter Mobile Number')
            mbl_no = input()
            print('Enter amount credit')
            bal = input()
            s.create_account(name, acc_number, mbl_no, bal)
            print('Account is created')

        elif ch == 2:
            s.display_all_records()
            s.display_by_account_number(1)

        elif ch == 3:
            print('Enter account number')
            acc_number = input()
            print('Enter amount to credit')
            amount = input()
            s.credit(acc_number, amount)

        elif ch == 4:
            print('Enter account number')
            acc_number1 = input()
            print('Enter amount to debit')
            amount1 = input()
            s.debit(acc_number1, amount1)

        if ch < 1 or ch > 4:
            sys.exit()
