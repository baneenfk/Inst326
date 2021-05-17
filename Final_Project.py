import sys
import pandas as pd
from argparse import ArgumentParser
import matplotlib.pyplot as plt
import time

class Credit_Card_Holder(): 
    """ A class used to determine potentially fraudulent transactions.
    Attributes:
        file(str): The file is a CSV that holds the transaction records. 
    """
    
    def __init__(self,file):
        """ The method exctarcts the databse as a DataFrame. Then creates a new 
            DataFrame with a filter using only columns required.
        Args:
            file(str): The file is a CSV that holds the transaction records.
        Side effects: 
            Set a value to a copy of a slice from a DataFrame.
        """
        df = pd.read_csv(file)
        df2 = df[["first", "last", "amt"]]
        df2[['date', 'time']] = df['trans_date_trans_time'].str.split(' ', expand=True)
        df2.loc[:,'time'] = df2['time'].apply(lambda x :str(x).split(':')[0])
        self.df2 = df2 

    def user(self, first_name, last_name): 
        """ The method will seperate the date column into two columns date and 
            time.
        Args: 
            first_name(str): The first name of the credit card holder.
            last_name(str): The last name of the credit card holder. 
        Raises: 
            KeyError: The first name must be in the first name column.
            KeyError: The last name must be in the last name column. 
        Returns: 
            str: A filtered dataframe that consist of the information 
            associated with the first and last name entered into the input. 
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
        return user_name.head(20)
    
    def last_20_transactions(self):
        """ The method will print the last 20 transactions.
        """
        user_name2 = self.user_name.sort_values(by='date',ascending=False)
        time.sleep(1)
        print(user_name2.head(20))
        
    def mean_amount(self): 
        """ The method determines the mean of transactions and prints the 
        mean amount. 
        """
        self.means = self.user_name['amt'].mean()
        self.mean = round(self.means, 2)
        time.sleep(1)
        print(f'The mean of all charges is $ {self.mean}')

    def irregular_times(self): 
        """ The method determines if the time a transaction occured is at a 
            irregular time. 
        """
        irr_time = {"0","1","2","3","4","5"}
        irr_time2 = self.user_name["time"]
        return irr_time2[irr_time2.isin(irr_time)].count()

    def irregular_times_count(self,count): 
        """ The method counts how many times transcations occured at irregular 
            times. 
        Args:
            count(int): The count of transcations that occured at irregular 
            times.
        """
        time.sleep(1)
        if count == 1: 
            print(f'There is {count} charge that occured at an irregular time!')
        else:
            print(f'There are {count} charges that occured at irregular times!')
    
    def irregular_amount(self): 
        """The method determines if a transaction is an a irregular 
            amount. 
        Returns:
            int: The number of transcations that occur at an irrgular time.
        """
        self.mean_amount()
        means = self.user_name['amt']
        item = means[means >= 500 + self.mean]
        count = item.count()
        time.sleep(1)
        if count == 1: 
            print(f'There is {count} charge that has an irregular amount!')
        else:
            print(f'There are {count} charges that have an irregular amount!')
        return count
    
    def transactions(self): 
        """The method creates a scatter plot with the date of the transaction 
            and the amount.
        """
        self.user_name.plot.scatter(x = "amt", y = "date", title = "Credit Card Transactions")
        time.sleep(1)
        plt.show()
    
def main(file):
    """ The main function will allow the user of the program to enter a credit 
        card owners name and will display potentially fraudulent transactions.
    Args:
        file(str): The file is a CSV that holds the transaction records.
    """ 
    credit_card = Credit_Card_Holder(file)
    value1 = input("Enter cardholders FIRST Name:\n").title()
    value2 = input("Enter cardholders LAST Name:\n").title()
    credit_card.user(value1,value2)
    credit_card.last_20_transactions()
    y = credit_card.irregular_times()
    credit_card.irregular_times_count(y)
    credit_card.irregular_amount()
    credit_card.transactions()
 
def parse_args(argslist):
    """ Parse command-line arguments.
    Expect three mandatory arguments:
        - file: a path to a CSV file containing credit card transactions
    Args:
        arglist (list of str): arguments from the command line.
    
    Returns:
        namespace: the parsed arguments, as a namespace.
    """
    parser = ArgumentParser()
    parser.add_argument("file", help="a csv file containing credit card transactions")
    return parser.parse_args(argslist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.file)