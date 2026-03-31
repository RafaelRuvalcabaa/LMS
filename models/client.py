from decorators.log_error import log_error_wrap


class Client: 
    @log_error_wrap
    def __init__(self, name: str, last_name: str, address: str, credit_history: int )-> None: 
        self._name = name 
        self.last_name = last_name 
        self.address = address
        self.credit_history = credit_history

    def __str__(self): 
        return f"El nombre del cliente es: {self._name}"

    

