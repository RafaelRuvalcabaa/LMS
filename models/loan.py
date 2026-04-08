from models.client import Client
from models.bank import Bank
from decorators.log_error import log_error_wrap
from errors.errors_borrowed import CreditScoreError

class Loan: 
    def __init__(self, cliente: Client, bank: Bank, amount: float, time: int)-> None: 
        self.cliente = cliente
        self.bank = bank 
        self.amount = amount 
        self.time = time 
        self.prestamo = None

    def __str__(self): 
        return f"Prestamo a nombre de {self.cliente}, una cantidad de: {self.amount}, por un tiempo de {self.time} meses"
    
    @log_error_wrap
    def loan(self):
        if self.cliente._credit_history < 600: 
            self.prestamo = False 
            raise CreditScoreError("User doesn't have enough credit history")
        self.prestamo = True 
        self.bank.withdraw(self.amount)
        self.bank.loan_history.append(self)
        return f"Prestamo creado por {self.amount}"
