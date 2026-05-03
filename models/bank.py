from decorators.log_error import log_error_wrap
from utils.json_handler import save_to_json  # ← AGREGAR ESTA LÍNEA


class Bank:
    _instancia = None 

    def __new__(cls, *args, **kwargs):
        if cls._instancia is None: 
            cls._instancia = super().__new__(cls)
        return cls._instancia

    @classmethod
    def get_instance(cls): 
        if cls._instancia is None: 
            cls._instancia = cls("Banamex", 2_000_000_000)
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

    @log_error_wrap
    def add_loan(self, loan): 
        self.loan_history.append(loan)
        self._save_loans_to_json()

     
    def _save_loans_to_json(self):
        """
        Guarda todos los loans en loans.json
        """
        loans_data = [loan.to_dict() for loan in self.loan_history]
        save_to_json(loans_data, filename="loans.json")


    @log_error_wrap
    def get_loans(self): 
        return self.loan_history
    
    @log_error_wrap
    def get_loan(self, loan_id):
        return self.loan_history[loan_id] 

