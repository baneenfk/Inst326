#import numpy as np
import sys
import pandas as pd
from argparse import ArgumentParser
#import matplotlib.pylot as plt


class Credit_Card_Holder(): 
    """ This is our first class used to extract information we want to pull out
        from our datasets.
        Attributes:
            file(csv file): The database consisting of first name, last name, 
            amount, and date. 
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
        self.df2 = df2 #(df2[['date', 'time']] = df['trans_date_trans_time'].str.split(' ', expand=True))
        self.first_name = self.df2["first"]
        self.last_name = self.df2["last"]
        self.amount  = self.df2["amt"]
        self.date = self.df2["date"]
        self.time = self.df2["time"]

    def user(self, first_name, last_name): 
        """ The method will seperate the date column into two columns date and 
            time.
            Args: 
                 dict(str): The dictionary of credit cars transactions. 
            Side effects: 
                Modify the dictionary date key
        """
        
        first_filter = self.df2['first'] == self.first_name
        last_filter = self.df2['last'] == self.last_name
        combo_filter = first_filter & last_filter
        self.first_last = self.df2[combo_filter]
        
    
    def mean_amount(self): 
        """ The method determines the mean of transactions. 
            Args:
                name(str): The name of the credit card holder.
                amount(float): The amount of a transaction. 
            Returns:
                float: The mean of the credit card amounts.
        """
        self.mean = self.first_last['self.amt'].mean()
        print(f'The mean of all charges are {self.mean}')

    def irregular_times(self): 
        """ The method determines if the time a transaction occured is at a 
            irregular time. 
            Args:
                name(str): The name of the credit card holder.
                time(int): The time the transaction took place. 
            Returns:
                int: The transactions that occur at an irrgular time.
        """
        time_list = []
        for x in self.time:
            line = x.split(" ")
            time_list.append(line)
            for x in time_list:
                line1 = x.split(':')
                time_list1.apend(line1)
                for x[0] in time_list1:
                    if hour == 0 or hour == 1 or hour == 2 or hour ==3 or hour ==4 or hour ==5 or hour == 22:
                        result = 1 
                    else:
                        result = 0 
                    return result
    
    def irregular_times_count(self, time): 
        """ !!! Change These DOCSTRINGS!!!
            Args:
                name(str): The name of the credit card holder.
                time(int): The time the transaction took place. 
            Returns:
                int: The transactions that occur at an irrgular time.
        """
        count = 0
            for x in self.time:
            line = x.split(" ")
            time_list.append(line)
            for x in time_list:
                line1 = x.split(':')
                time_list1.apend(line1)
        
        if time == 1:
            count += 1
        else:
            count += 0
        print(f'There are {count} charges that occured at irregular times.')
        return count
    
    def irregular_amount(self, amount): 
        """ The method determines if a transaction is an a irregular 
            amount. 
            Args:
                name(str): The name of the credit card holder.
                amount(float): The amount of a transaction. 
            Returns:
                int: The number of transcations that occur at an irrgular time.
        """
        count = 0
        if amount >= 200 + self.mean:
            count += 1
        else:
            count += 0
        print(f'There are {count} charges that raise a flag!') 
        return count
    
    #def transactions(self, amount, date): 
        #""" The method creates a line graph with the date of the transaction and
           # the amount. 
           # Args:
                #amount(float): This is the amount of the charge. 
                #date(int): This is the date of the tansaction. 
            #Returns:
                #line graph: Of all transcations.
       #"""      
        #amount =  df['amt']
        #date = df['date']
        #line_graph = df.plot.line(x=amount, y=date)
        #return(line_graph)
        
def main(file):
    """ The main function will allow the user of the program to enter a credit 
        card owners name then will return the statistical_computaions.
        Args:
            first_name(str): This is the first name of the card holder.
            last_name(str): This is the last name of the card holder.
            amount(float): This is the amount of the charge. 
            date(int): This is the date of the tansaction.  
        Raises:
            KeyValueError: The name must be in the CSV file.
        Returns:
            str: The iregular credit card transcations. 
    """ 
    credit_card = Credit_Card_Holder(file)
    value1 = input("Enter cardholders FIRST Name:\n")
    value2 = input("Enter cardholders LAST Name:\n")
    credit_card.user(value1,value2)
    credit_card.mean_amount()
    x = credit_card.irregular_times
    credit_card.irregular_times_count(x)
    credit_card.irregular_amount()
    credit_card.transaction()
 
    '''return 
    
    return credit_card.mean_amount()
    return credit_card.irregular_times_count()
    return credit_card.irregular_amount()
    return credit_card.transaction()'''

def parse_args(argslist):
    parser = ArgumentParser()
    parser.add_argument("file", help="a csv file containing credit card info")
    return parser.parse_args(argslist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.file)