from datetime import datetime
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException
from models.bank import Bank
from models.client import Client
from models.loan import Loan 
from schemas import LoanCreate
from errors.errors_borrowed import CreditScoreError, ZeroAmount, TimeToPay, NoNameClient, BankCapitalError
import json


def loan_created_at() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# ---------------------
app = FastAPI()
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

@app.post("/loans/bulk")
def create_loan(
    loan_data: LoanCreate,
    fecha_ejecucion: Annotated[str, Depends(loan_created_at)],
):
    try:
        date_execution = fecha_ejecucion

        client = Client(loan_data.name, loan_data.last_name, loan_data.city, loan_data.credit_history)
        loan = Loan(client, bank, loan_data.amount, loan_data.time)
        loan.fecha = date_execution
        loan.loan()
        bank.add_loan(loan)
        return {"message": "Loan created", "loan": str(loan), "fecha": date_execution}
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


@app.get("/loans/all")
def get_loan_json(): 
    result = []
    for loan in bank.get_loans():
        result.append({
            "name": loan.cliente._name,
            "last_name": loan.cliente._last_name,
            "city": loan.cliente._address,
            "credit_history": loan.cliente._credit_history,
            "amount": loan.amount,
            "time": loan.time,
            "status": loan.prestamo,
            "fecha": getattr(loan, "fecha", None),
        })
    if result: 
        with open("loans_history.json", "w") as file:
            json.dump(result, file, indent=4,  ensure_ascii=False)
    return result

@app.delete("/loans/delete/{loan_id}")
def delete_loan(loan_id: int):
    try:
        loans = bank.get_loans()
        deleted = loans.pop(loan_id)
        return {"message": "loan deleted", "loan": str(deleted)}
    except IndexError:
        raise HTTPException(status_code=404, detail="Loan not found")
