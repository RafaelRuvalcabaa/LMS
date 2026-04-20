from decorators.log_error import log_error_wrap
from errors.errors_borrowed import NoNameClient, DefaultName


class Client: 
    @log_error_wrap
    def __init__(self, name: str, last_name: str, address: str, credit_history: int )-> None:
        if not name or not last_name: 
            raise NoNameClient("Error setting your client")
        self._name = name 
        self._last_name = last_name 
        self._address = address
        self._credit_history = credit_history

    def __str__(self): 
        return f"{self._name} {self._last_name}"

    @property
    def credit_history(self)->int: 
        return self._credit_history
    
    