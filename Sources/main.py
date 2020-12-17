import pandas as pd


class Account:

    account_number = []
    name = []
    mobile_no = []
    balance = []
    #account_type = []
    data = {'Customer_Name': name, 'Account': account_number,  'Balance': balance, 'Mobile_No': mobile_no}

    df = pd.DataFrame(data)

    def set_data(self):

        self.df = pd.DataFrame(self.data)

    def create_account(self, name1,acc_number,mbl_no,bal):

        #print('Enter name : ')
        self.name.append(name1)
        #print('Enter Account Number')
        self.account_number.append(acc_number)
        #print('Enter Mobile Number')
        self.mobile_no.append(mbl_no)
        #print('Enter amount credit')
        self.balance.append(bal)
        #print('Account is created')
        self.set_data()

    def display_all_records(self):
        self.set_data()
        #print(self.df)
        return self.data

    def display_by_account_number(self,acc_number):
        self.set_data()
        #print('Enter account number')
        #acc_number = input()
        for i in range(0, len(self.account_number)):
            if acc_number == self.account_number[i]:
                acc=self.df.loc[[i]]
                data={}
                data['Customer_Name'] = self.data['Customer_Name'][i]
                data['Account'] = self.data['Account'][i]
                data['Balance'] = self.data['Balance'][i]
                data['Mobile_No'] = self.data['Mobile_No'][i]
                print(data)
                return data
                break

    def credit(self,acc_number,amount):

        #print('Enter account number')
        # acc_number = input()
        #print('Enter amount to credit')
        # amount = input()
        for i in range(0, len(self.account_number)):
            if acc_number == self.account_number[i]:
                self.balance[i] = int(self.balance[i])+int(amount)
                return self.balance[i]
                print('Amount credited')
                self.set_data()
                break

    def debit(self,acc_number,amount):

        #print('Enter account number')
        # acc_number = input()
        #print('Enter amount to credit')
        # amount = input()
        for i in range(0, len(self.account_number)):
            if acc_number == self.account_number[i]:
                self.balance[i] = self.balance[i] - amount
                return self.balance[i]
                print('Account Debited')
                self.set_data()
                break


if __name__ == "__main__":
    s = Account()
    s.create_account('Akshay',1,8421966287,1000)
    s.create_account('AkshaySangar', 2, 8421966287, 1000)
    df1=s.display_all_records()
    s.display_by_account_number(1)
    s.credit(1,1000)
    df1 = s.display_all_records()
    s.debit(1,1000)
    #print(df1)
