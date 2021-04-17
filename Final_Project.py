import pandas as pandas
import matplotlib.pylot as plt
class credit_card_info(): 
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
        
    def convert(self,file): 
        """ The method converts the DataFrame into a dictionary.
            Args:
                file(csv file): The database of credit card transactions.
        """
    def adjust(self,dict): 
        """ The method will seperate the date column into two columns date and 
            time.
            Args: 
                 dict(str): The dictionary of credit cars transactions. 
            Side effects: 
                Modify the dictionary date key
        """
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
        """
    
    def mean_amount(self, amount): 
        """ The method determines the mean of transactions. 
            Args:
                name(str): The name of the credit card holder.
                amount(float): The amount of a transaction. 
            Returns:
                float: The mean of the credit card amounts.
        """
    def irregular_time(self, time): 
        """ The method determines if the time a transaction occured is at a 
            irregular time. 
            Args:
                name(str): The name of the credit card holder.
                time(int): The time the transaction took place. 
            Returns:
                int: The transactions that occur at an irrgular time.
        """
    def irregular_amount(self, amount): 
        """ The method determines if a transaction is an a irregular 
            amount. 
            Args:
                name(str): The name of the credit card holder.
                amount(float): The amount of a transaction. 
            Returns:
                int: The number of transcations that occur at an irrgular time.
        """
        
    def transactions(self, amount, date): 
        """ The method creates a line graph with the date of the transaction and
            the amount. 
            Args:
                amount(float): This is the amount of the charge. 
                date(int): This is the date of the tansaction. 
            Returns:
                line graph: Of all transcations.
        """      
           
def main:
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
       
if __name__ == "__main__":
    main()
    