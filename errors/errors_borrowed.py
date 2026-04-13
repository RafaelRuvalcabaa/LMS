class ValidationError (Exception):  pass 

class NoNameClient (ValidationError): pass 

class CreditScoreError(Exception): pass 

class ZeroAmount(Exception): pass

class TimeToPay(Exception): pass 

class AmountBackProblems(Exception): pass

class MoreLoan(Exception): pass