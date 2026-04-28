from schemas import LoanCreate, LoanResponse
from models.client import Client
from models.loan import Loan 



class LoanService: 
    def __init__(self, bank_instance): 
        self.bank = bank_instance

    def create_loan(
        self, 
        loan_data: LoanCreate,
        created_by: str
    )-> Loan:  
            client = Client(
                loan_data.name,
                loan_data.last_name,
                loan_data.city, 
                loan_data.credit_history
            )

            loan = Loan(client,
            self.bank,
            loan_data.amount, 
            loan_data.time,
            created_by=created_by  # ← AGREGAR ESTO
)
            loan.loan()
            self.bank.add_loan(loan)
            return loan 


    def get_all_loan(self)-> list[Loan]: 
        return self.bank.get_loans() 
