from pydantic import BaseModel

class LoanCreate(BaseModel): 
    name: str
    last_name: str
    city: str 
    credit_history: int
    amount: float
    time: int

class LoanResponse(BaseModel): 
    name: str
    last_name: str
    city: str 
    credit_history: int
    amount: float
    time: int
    status: bool 
    