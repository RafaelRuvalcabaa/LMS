from functools import wraps
from logs import logger 
from errors.errors_borrowed import ValidationError



def log_error_wrap(func): 
    @wraps(func)
    def wrapper(*args,**kwargs): 
        logger.info(f"Iniciando metodo: {func.__name__} -> Class: {args[0].__class__.__name__}")
        result = None 
        try: 
            result = func(*args, **kwargs)
            logger.info(f"Metodo: {func.__name__} -> Class:  {args[0].__class__.__name__} -> Successfuly")
        except Exception as error: 
            logger.error(f"Error en {func.__name__} -> Detalle: {error}")
            raise 
        return result
    return wrapper 


            
