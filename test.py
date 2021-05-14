import pytest 
import Final_Project as fp 


def test_user():
    #Test
    assert fp.user(Jeff) == Jeff
def test_irregular_times():
    #Test
    assert fp.irregular_times_count(0) == 1 
def test_irregular_amount():
    #Test
    assert fp.irregular_amount(650) == 1