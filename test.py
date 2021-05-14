import Final_Project as fp 
import pytest

def user():
    #Test
    assert fp.user(Jeff) == Jeff
def irregular_times():
    #Test
    assert fp.irregular_times_count(0) == 1 
def irregular_amount():
    #Test
    assert fp.irregular_amount(650) == 1