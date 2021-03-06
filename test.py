import pytest 
import Final_Project as fp 

@pytest.fixture
def credit_card():
    return fp.Credit_Card_Holder("fraudTest1.csv")

def test_user(credit_card):
    """ Does credit_card.user() check to see if the first name and last name are 
        in the CSV, does it return the last 20 transactions, and does it raise 
        the correct error if first name and last name are not in the CSV?
    """
    x = credit_card.user("Jeff", "Elliott")
    assert (x['first'] == "Jeff").all()
    assert (x['last'] == "Elliott").all()
    assert len(x) == 20 
    with pytest.raises(KeyError):
        credit_card.user("Jakd",("10"))
    with pytest.raises(KeyError):
        credit_card.user("7",("1fjjf"))
    
def test_irregular_times(credit_card):
    """ Does credit_card.irregular_times() return the correct count of 
        transactions that occured at irregular hours. 
    """
    credit_card.user("Aaron", "Murray")
    assert credit_card.irregular_times() == 22
    credit_card.user("Joseph", "Murray")
    assert credit_card.irregular_times() == 18
    
def test_irregular_amount(credit_card):
    """ Does credit_card.irregular_amount() return the correct count of 
        transactions that had an irregular amount. 
    """
    credit_card.user("Adam", "Riddle")
    assert credit_card.irregular_amount() == 0 
    credit_card.user("Jeff", "Elliott")
    assert credit_card.irregular_amount() == 1
