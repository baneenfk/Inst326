import numpy as np
import sys
import pandas as pd
from argparse import ArgumentParser
import matplotlib.pyplot as plt



class Credit_Card_Holder(): 
    """ This is our first class used to extract information we want to pull out
        from our datasets.
        Attributes:
            file(csv file): The database consisting of first name, last name, 
            amount, and date. 
            df2(dataframe): The data consisting of first name, last name, 
            amount, and date. 
            first_name(str): The first name of the credit card holder.
            last_name(str): The last name of the credit card holder.
            amount(str): The amount of each transaction. 
            date(str): The date of each transaction.
            time(str): The amount of each transaction.
    """
    
    def __init__(self,file):
        """ The method exctarcts the databse as a DataFrame. Then creates a new 
            DataFrame with only the columns required.
            Args:
                file(csv file): The database of credit card transactions.
        """
        file = 'fraudTest1.csv'
        df = pd.read_csv(file)
        df2 = df[["first", "last", "amt"]]
        df2[['date', 'time']] = df['trans_date_trans_time'].str.split(' ', expand=True)
        self.df2 = df2 
        self.first_name = self.df2["first"]
        self.last_name = self.df2["last"]
        self.amount  = self.df2["amt"]
        self.date = self.df2["date"]
        self.time = self.df2["time"]

    def user(self, first_name, last_name): 
        """ The method will seperate the date column into two columns date and 
            time.
            Args: 
            first_name(str): The first name of the credit card holder.
            last_name(str): The last name of the credit card holder. 

        """
        fname = self.df2["first"].tolist()
        lname = self.df2["last"].tolist()
        self.new = []
        for x in fname:
            if first_name not in fname:
                raise KeyError("Name not in List")
        for y in lname:
            if last_name not in lname:
                raise KeyError("Name not in List") 
        test = self.df2['first'] == first_name
        test2 = self.df2['last'] == last_name
        both = test & test2 
        user_name = self.df2[both]
        self.user_name = user_name
        print(user_name.head(20))
    def mean_amount(self): 
        """ The method determines the mean of transactions and prints the amount. 

        """
        self.mean = self.user_name['amt'].mean()
        print(f'The mean of all charges are {self.mean}')

    def irregular_times(self): 
        """ The method determines if the time a transaction occured is at a 
            irregular time. 
            Args:
        """
        vals = self.user_name["time"].tolist()
        self.new = []
        for x in vals:
            if x[0] == "0" or x[0] == "1" or x[0] == "2" or x[0] == "3" or x[0] == "4" or x[0] == "5":
                result = 1 
                self.new.append(result)
            else:
                result = 0 
                self.new.append(result)
    def irregular_times_count(self,x): 
        """ The method counts how many times transcations occured outside of 
            regular business hours. 
            Args:
                name(str): The name of the credit card holder.
                time(int): The time the transaction took place. 
            Returns:
                int: The transactions that occur at an irrgular time.
        """
        count = 0
        for x in self.new:
            if x == 1:
                count += 1
            else:
                count += 0
        print(f'There are {count} charges that occured at irregular times.')

    
    def irregular_amount(self,x): 
        """The method determines if a transaction is an a irregular 
            amount. 
            Args:
                name(str): The name of the credit card holder.
                amount(float): The amount of a transaction. 
            Returns:
                int: The number of transcations that occur at an irrgular time.
        """
        amount_list = []
        count = 0
        for x in self.user_name["amt"]:
            amount_list.append(x)
            for x in amount_list:
                if x >= 500 + self.mean:
                     count += 1
                else:
                     count += 0
        print(f'There are {count} charges that have an irregular amount!') 
    
    def transactions(self): 
        """The method creates a line graph with the date of the transaction and
            the amount. 
            Args:
                #amount(float): This is the amount of the charge. 
                #date(int): This is the date of the tansaction. 
            Returns:
                line graph: Of all transcations.
        """
        self.user_name.plot.scatter(x = "amt", y = "date", title = "Credit Card Transactions")
        plt.show()
    
def main(file):
    """ The main function will allow the user of the program to enter a credit 
        card owners name then will return the statistical_computaions.
        Args:
            file(csv file): The database consisting of first name, last name, 
            amount, and date.
    """ 
    credit_card = Credit_Card_Holder(file)
    value1 = input("Enter cardholders FIRST Name:\n")
    value2 = input("Enter cardholders LAST Name:\n")
    credit_card.user(value1,value2)
    x =credit_card.mean_amount()
    y = credit_card.irregular_times()
    credit_card.irregular_times_count(x)
    credit_card.irregular_amount(y)
    credit_card.transactions()
 
def parse_args(argslist):
    parser = ArgumentParser()
    parser.add_argument("file", help="a csv file containing credit card info")
    return parser.parse_args(argslist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.file)