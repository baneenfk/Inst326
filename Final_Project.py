import numpy as np
import pandas as pd
import matplotlib.pylot as plt


class Credit_Card_Holder(): 
    """ This is our first class used to extract information we want to pull out
        from our datasets.
        Attributes:
            file(csv file): The database consisting of first name, last name, 
            amount, and date. 
    """
    
    def __init__(self,file,df,df2):
        """ The method exctarcts the databse as a DataFrame. Then creates a new 
            DataFrame with only the columns required.
            Args:
                file(csv file): The database of credit card transactions.
        """
        self.first_name = first
        self.last_name = last
        self.amount  = amt
        self.date = date
        self.time = time
        
        file = 'fraudTest1.csv'
        df = df = pd.read_csv(file)
        df2 = df[["first", "last", "amt"]]
        df2[['date', 'time']] = df['trans_date_trans_time'].str.split(' ', expand=True)

    def user(self,dict): 
        """ The method will seperate the date column into two columns date and 
            time.
            Args: 
                 dict(str): The dictionary of credit cars transactions. 
            Side effects: 
                Modify the dictionary date key
        """
        first_filter = df2['first'] == "Jeff"
        last_filter = df2['last'] == "Elliott"
        combo_filter = first_filter & last_filter
        first_last = df2[combo_filter]
        value1 = input("Enter cardholders FIRST Name:\n")
        value2 = input("Enter cardholders LAST Name:\n")

        
class statistical_computaions(): 
    """ This class will determine if transactions are irregualr and identify 
        means. 
        Attributes:
            first_name(str): This is the first name of the card holder.
            last_name(str): This is the last name of the card holder.
            amount(float): This is the amount of the charge. 
            date(int): This is the date of the tansaction. 
     """       
    def __init__(self):
        """ Inititalizes the first name, last name, amount and date.
            Args:
                first_name(str): This is the first name of the card holder.
                last_name(str): This is the last name of the card holder.
                amount(float): This is the amount of the charge. 
                date(int): This is the date of the tansaction.
                time(int): This is the time of the transaction. 
        """
        self.first_name = first
        self.last_name = last
        self.amount  = amt
        self.date = date
        self.time = time
    
    def mean_amount(self, amount): 
        """ The method determines the mean of transactions. 
            Args:
                name(str): The name of the credit card holder.
                amount(float): The amount of a transaction. 
            Returns:
                float: The mean of the credit card amounts.
        """
        mean = first_last['amt'].mean()
        print(f{'The mean of all charges are {mean}')

    def irregular_times(self, time): 
        """ The method determines if the time a transaction occured is at a 
            irregular time. 
            Args:
                name(str): The name of the credit card holder.
                time(int): The time the transaction took place. 
            Returns:
                int: The transactions that occur at an irrgular time.
        """
        if hour == 0 or hour == 1 or hour == 2 or hour ==3 or hour ==4 or 
        hour ==5 or hour == 22 
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
        if time == 1:
            count += 1
        else:
            count += 0
        return count
        print(f{'There are {count} charges that occured at irregular times.')
        
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
        if amount >= 200 + mean:
            count += 1
        else:
            count += 0
        return count
        print(f{'There are {count} charges that raise a flag!') 
        
    def transactions(self, amount, date): 
        """ The method creates a line graph with the date of the transaction and
            the amount. 
            Args:
                amount(float): This is the amount of the charge. 
                date(int): This is the date of the tansaction. 
            Returns:
                line graph: Of all transcations.
        """      
        amount =  df['amt']
        date = df['date']
        line_graph = df.plot.line(x=amount, y=date)
        return(line_graph)
        
def main(first_name, last_name, amount, date):
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
    credit_card = Credit_card_holder():
    credit_card.user()
    credit_card.mean_amount()
    credit_card.irregular_times_count()
    credit_card.
 
if __name__ == "__main__":
    main()
    