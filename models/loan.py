from models.client import Client
from models.bank import Bank
from decorators.log_error import log_error_wrap
from errors.errors_borrowed import CreditScoreError, TimeToPay, ZeroAmount, BankCapitalError
from schemas import LoanResponse



class Loan:
    @log_error_wrap
    def __init__(self, cliente: Client, bank: Bank, amount: float, time: int)-> None: 
        if amount <=0: 
            raise ZeroAmount("Amount was less than 0")
        if time <=0:
            raise TimeToPay("Time to pay cannot be less than 0")
        if bank.capital < amount:
            raise BankCapitalError("Bank doesn't have enough capital")
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
        return f"Prestamo creado por {self.amount}"

    @log_error_wrap
    def monthly(self): 
        if not self.prestamo: 
            raise ValueError("Loan is not approved yet")
        self.amount = self.amount / self.time 
        return self.amount  
    
    def to_response(self)-> LoanResponse:
        """Convierte tu prestamo a schema de respuesta de API"""
        return LoanResponse(
            name=self.cliente._name,
            last_name=self.cliente._last_name,
            city=self.cliente._address,
            credit_history=self.cliente._credit_history,
            amount=self.amount,
            time=self.time,
            status=self.prestamo,
            summary= str(self)
       )