import pytest 
from models.client import Client 
from models.bank import Bank
from models.loan import Loan
from errors.errors_borrowed import ZeroAmount, TimeToPay


@pytest.fixture
def build_client():  
    name= "Rafael"
    last_name = "Ruvalcaba"
    city = "Guadalajara"
    score = 750
    return Client(name, last_name, city, score)

@pytest.fixture 
def build_bank(): 
    name = "Banamex"
    capital = 788979966
    return Bank(name, capital)


def test_loan_amount(build_client, build_bank):
    loan = Loan(build_client, build_bank, 5000, 12)
    assert loan.amount == 5000
  
def test_loan_time(build_client, build_bank): 
    loan = Loan(build_client, build_bank, 5000, 12)
    assert loan.time == 12


@pytest.mark.parametrize("amount",[0,-1,-1000])
def test_without_amount(amount, build_client, build_bank):
    with pytest.raises(ZeroAmount):
        Loan(build_client, build_bank, amount, 12)

@pytest.mark.parametrize("time",[ 0,-1,-1000])
def test_without_time( time, build_client, build_bank):
    with pytest.raises(TimeToPay):
        Loan(build_client, build_bank, 5000, time)