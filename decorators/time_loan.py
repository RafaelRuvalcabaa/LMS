from functools import wraps
from logs import logger 
from datetime import datetime


def autodate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        caller = args[0] if args else kwargs.get("loan_data")
        cls_name = caller.__class__.__name__ if caller is not None else "?"
        logger.info(f"Iniciando metodo: {func.__name__} -> Class: {cls_name}")
        try:
            automatic_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            kwargs["fecha_ejecucion"] = automatic_date
            result = func(*args, **kwargs)
        except Exception as error: 
            logger.error(f"Error en {func.__name__} -> Detalle: {error}")
            raise
        return result
    return wrapper 
