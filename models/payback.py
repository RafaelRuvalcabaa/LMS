from models.loan import Loan 
from decorators.log_error import log_error_wrap
from errors.errors_borrowed import AmountBackProblems, MoreLoan


class Abono: 
    @log_error_wrap
    def __init__(self, loan: Loan,  amount_back: float| int)->None: 
        if amount_back <= 0: 
            raise AmountBackProblems ("You wrote a amountback wrong")
        if amount_back > loan.amount: 
            raise MoreLoan("You amount_back is higher than you loan amount")
        self.loan = loan
        self.amount_back = amount_back
        self.loan.amount -= self.amount_back
        self.loan.time -= 1

