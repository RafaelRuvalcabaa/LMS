import pytest 
from models.client import Client 
from models.bank import Bank
from models.loan import Loan
from errors.errors_borrowed import ZeroAmount, TimeToPay, CreditScoreError
from unittest.mock import MagicMock

@pytest.fixture
def build_client():  
    name= "Rafael"
    last_name = "Ruvalcaba"
    city = "Guadalajara"
    score = 750
    return Client(name, last_name, city, score)

@pytest.fixture 
def build_bank(): 
    bank = MagicMock()
    bank._name = "Banamex"
    bank.capital = 1_000_000
    return bank

def test_str(build_client, build_bank): 
    loan = Loan(build_client, build_bank, 5000, 12)
    assert "Rafael" in str(loan)

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

def test_score(build_bank):
   client = Client("Rafael", "Ruvalcaba", "Guadalajara",100)
   loan = Loan(client, build_bank, 5000,12)
   with pytest.raises(CreditScoreError): 
       loan.loan()

def test_monthly(build_bank, build_client): 
    loan = Loan(build_client,build_bank, 5000, 12)
    with pytest.raises(ValueError): 
        loan.monthly()
    
def test_aprroved(build_bank, build_client): 
    loan = Loan(build_client,build_bank, 12000, 12)
    loan.prestamo = True
    assert loan.monthly() == 1000

def test_credit(build_bank): 
    client = Client("Rafael", "Ruvalcaba", "Guadalajara",700)
    loan = Loan(client, build_bank, 5000,12)
    loan.loan()
    assert loan.prestamo == True 