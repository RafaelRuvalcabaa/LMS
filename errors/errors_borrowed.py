class ValidationError (Exception): 
    pass 

class NoNameClient (ValidationError): 
    pass 

class CreditScoreError(Exception): 
    pass 