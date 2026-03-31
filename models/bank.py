from decorators.log_error import log_error_wrap
from logs import logger


class Bank:
    _instancia = None 

    def __new__(cls, *args,**kwargs):
        if cls._instancia is None: 
            cls._instancia = super().__new__(cls)
        return cls._instancia
    
    def __init__(self, name: str, capital: float)-> None:
        if hasattr(self, '_name'):
            return
        if capital <= 0:
            logger.error(f"Error en clase {self.__class__.__name__}: capital must be greater than 0")
            raise ValueError ("Capital must be greater than 0")
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