from datetime import datetime
from fastapi import Header, FastAPI, HTTPException
from models.bank import Bank
from models.client import Client
from models.loan import Loan 
from typing import List
from schemas import LoanFinalResponse, LoanCreate, LoanMetadata, LoanResponse
from errors.errors_borrowed import CreditScoreError, ZeroAmount, TimeToPay, NoNameClient, BankCapitalError
import json



def loan_created_at() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# ---------------------
app = FastAPI(version= "1.2.2")
# ---------------------


# Build a bank 
bank = Bank("Banamex", 1_000_000)
#--------------------------------------


@app.get("/")
def root(): 
    return {"message": "Loan System API"}

@app.get("/bank")
def get_bank(): 
    return {
        "name": bank._name,
        "capital": bank._capital
    }

"""
#---------------------------------------
client1 = Client("Rafa", "Ruvalcaba", "Guadalajara", 650)
loan1 = Loan(client1, bank, 5000, 12)
loan1.loan()
loan1.fecha = None
bank.add_loan(loan1)
#-----------------------------------------
"""


@app.get("/loans")
def get_loans(): 
    return {"loans": [str(loan) for loan in bank.get_loans()]}

"""
@app.get("/loans/{loan_id}")
def get_loan(loan_id: int): 
    try: 
        loan = bank.get_loan(loan_id)
        return {"loan": str(loan)}
    except IndexError: 
        status_code = 404
        raise HTTPException(status_code, detail="Loan Not Found")
"""

@app.post("/loans/bulk", response_model= LoanFinalResponse)
def create_loan( 
    loan_data: LoanCreate, 
    x_user_id: str = Header(default = "Admin")
    ):
    try:
        metadata_info = LoanMetadata(created_by = x_user_id)
        client = Client(loan_data.name, loan_data.last_name, loan_data.city, loan_data.credit_history)
        loan = Loan(client, bank, loan_data.amount, loan_data.time)
        loan.loan()
        bank.add_loan(loan)
        return LoanFinalResponse(
            data= loan.to_response(),
            metadata = metadata_info
        )     
    except CreditScoreError:
        raise HTTPException(status_code=400, detail="Credit score too low") 
    except BankCapitalError:
        raise HTTPException(status_code=400, detail="Bank doesn't have enough capital")
    except ZeroAmount: 
        raise HTTPException(status_code=400, detail="Amount must be greater than 0")
    except TimeToPay:
        raise HTTPException(status_code=400, detail="Time to pay must be greater than 0")
    except NoNameClient:
        raise HTTPException(status_code=400, detail="Client must have a name")


@app.get("/loans/all", response_model= List[LoanFinalResponse])
def get_loan_json(x_user_id: str = Header(default = "Admin")): 
    result = []
    for loan in bank.get_loans():
        metadata_info = LoanMetadata(created_by = x_user_id)
        loan_data = loan.to_response()
        result.append({
            "data": loan_data, 
            "metadata": metadata_info
        })
    if result: 
        with open("loans_history.json", "w", encoding="utf-8") as file:
            historial_dict = [
                LoanFinalResponse(data=item["data"], metadata=item["metadata"]).model_dump() 
                for item in result
            ]
            json.dump(historial_dict, file, indent=4, ensure_ascii=False)
    return result



@app.delete("/loans/delete/{loan_id}")
def delete_loan(loan_id: int):
    try:
        loans = bank.get_loans()
        deleted = loans.pop(loan_id)
        return {"message": "loan deleted", "loan": str(deleted)}
    except IndexError:
        raise HTTPException(status_code=404, detail="Loan not found")
