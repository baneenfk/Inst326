# Inst326
Final_Project.py - 
The Final_Project.py is our program for the final project. The program consists of one class, eight methods, and one function. It also includes two functions the parse_args 
and if __name__ == "__main"". The program reads a CSV file of credit card charges and determines which charges are potentially fraudulent. 
The program requires the user to input the credit card holder's first and last name. If the name is not in the CSV file, it will raise a KeyError that says "Name not in List". 
To run Final_Project.py you must enter the following into the terminal's command line: 
python Final_Project.py fraudTest1.csv.
The input will require a first name and the last name. The following are some examples that are found in the dataset: 
First/Last:
Adam/Riddle,
Jeff/Elliott,
Arraon/Murray. 
The names are not case-sensitive. You can use any name provided in the testFraud1.csv 
test.py - 
The test.py is the pytest that we created for the final project to test the functionality of our main program. The test script consists of a pytest fixture and three 
different tests. It will test the user method, the irregular_times method, and test_irregular_amount method. 
To run the test.py you must enter the following into the terminal's command line: 
$ pytest test.py
fraudTest1.csv -
The fraudTest1.csv is the dataset we are using for the project. We retrieved the dataset from kaggle.com. The original dataset contains 1000 credit card holder's 
transactions for a year from 2019 to 2020. We edited and condensed the dataset to make it more manageable. The data that we used was posted on Kaggle by 
Kartik Shenoy; howver he was not the owner or creator of the dataset. 
The source of the simulation is as follows: 
"This was generated using Sparkov Data Generation | Github tool created by Brandon Harris. This simulation was run for the duration - 1 Jan 2019 to 31 Dec 2020. 
The files were combined and converted into a standard format." 
References – 
Shenoy, K. (2020, August 5). Credit Card Transactions Fraud Detection Dataset. Kaggle. https://www.kaggle.com/kartik2112/fraud-detection. 
