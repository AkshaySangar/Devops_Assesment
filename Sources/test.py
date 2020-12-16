import unittest
import main as m
import pandas 
from pandas.util.testing import assert_frame_equal


class Test(unittest.TestCase):
    account_number = []
    name = []
    mobile_no = []
    balance = []
    # account_type = []
    data = {'Customer_Name': name, '  Account': account_number, '  Balance': balance, '  Mobile_No.': mobile_no}
    # df = pd.DataFrame(data)

    s = m.Account()
    s.create_account('Akshay', 1, 8421966287, 1000)
    name.append('Akshay')
    account_number.append(1)
    mobile_no.append(8421966287)
    balance.append(1000)
    df = pandas.DataFrame(data)

    def test_all_record(self):
        s = m.Account()
        df1 = s.display_all_records()
        assert_frame_equal(df1, self.df)

    def test_record_by_acc_no(self):
        s = m.Account()
        acc_number = 1
        df1 = s.display_by_account_number(1)
        for i in range(0, len(self.account_number)):
            if acc_number == self.account_number[i]:
                acc = self.df.loc[[i]]
                assert_frame_equal(df1, acc)
                break

    def test_credit(self):

        s = m.Account()
        bal = s.credit(1,1000)
        acc_number = 1
        amount = 1000
        for i in range(0, len(self.account_number)):
            if acc_number == self.account_number[i]:
                self.balance[i] = int(self.balance[i])+int(amount)
                self.df = pandas.DataFrame(self.data)
                break


        self.assertEqual(bal,2000)

    def test_debit(self):

        s = m.Account()
        bal = s.debit(1,1000)
        acc_number = 1
        amount = 1000
        for i in range(0, len(self.account_number)):
            if acc_number == self.account_number[i]:
                self.balance[i] = self.balance[i] - amount
                self.df = pandas.DataFrame(self.data)
                break

        self.assertEqual(bal,1000)


if __name__ == '__main__':
    unittest.main()
