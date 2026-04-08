from decorators.log_error import log_error_wrap
from logs import logger
from models.loan import Loan 


class Bank:
    _instancia = None 

    def __new__(cls, *args, **kwargs):
        if cls._instancia is None: 
            cls._instancia = super().__new__(cls)
        return cls._instancia
    
    @log_error_wrap
    def __init__(self, name: str, capital: float) -> None:
        if hasattr(self, '_name'): return
        
        # Al usar el decorador, solo lanza la excepción y él la loguea
        if capital is None or capital <= 0:
            raise ValueError("Capital must be greater than 0")
        if not name: 
            raise ValueError("Bank needs to have a name")
        self.loan_history = []
        self._name = name 
        self._capital = capital

    def __str__(self): 
        return f"Bank: {self._name} -> Capital: {self._capital}"
    
    # Mostrar capital 
    @property
    def capital(self)-> int: 
        return self._capital
    
    #Modificar capital
    @capital.setter
    @log_error_wrap
    def capital(self, capital_update)-> None: 
        if type(capital_update) not in [int, float]:
            raise TypeError("Must be a number")
        self._capital = capital_update 

    @log_error_wrap
    def withdraw(self, amount: float): 
        if amount > self._capital:
            raise ValueError ("Amount is higher than capital")
        self._capital -= amount 

    def authorized_credit_report(self, loan_list)->str: 
        for user in range(loan_list): 
            yield user