import pytest
from models.client import Client
from models.payback import Abono 
from models.bank import Bank 
from models.loan import Loan
from errors.errors_borrowed import AmountBackProblems, MoreLoan




@pytest.fixture 
def loan_fixture(): 
    Banamex = Bank("Banamex", 7899900000)
    Rafael = Client("Rafael", "Ruvalcaba", "Del Coral", 760)
    return Loan(Banamex, Rafael, 9000, 12)

    

def test_payback(loan_fixture):
    abono = Abono(loan = loan_fixture, amount_back=500)
    assert abono.amount_back == 500


def test_amount(loan_fixture): 
    abono = Abono(loan = loan_fixture, amount_back=500)
    assert abono.loan.amount == 8500

def test_less_time(loan_fixture): 
    abono = Abono(loan = loan_fixture, amount_back=500)
    assert abono.loan.time == 11
    

def test_amount_back(loan_fixture): 
    with pytest.raises(AmountBackProblems):
        Abono(loan = loan_fixture, amount_back=-100)


def test_overpayment(loan_fixture): 
    with pytest.raises(MoreLoan):
        Abono(loan = loan_fixture, amount_back=98000)


