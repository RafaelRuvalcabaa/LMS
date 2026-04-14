from fastapi import FastAPI, HTTPException
from models.bank import Bank 
from models.client import Client
from models.loan import Loan 

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
#---------------------------------------
client1 = Client("Rafa", "Ruvalcaba", "Guadalajara", 650)
loan1 = Loan(client1, bank, 5000, 12)
loan1.loan()
bank.add_loan(loan1)
#-----------------------------------------

@app.get("/loans")
def get_loans(): 
    return {"loans": [str(loan) for loan in bank.get_loans()]}

@app.get("/loans/{loan_id}")
def get_loan(loan_id: int): 
    try: 
        loan = bank.get_loan(loan_id)
        return {"loan": str(loan)}
    except IndexError: 
        status_code = 404
        raise HTTPException(status_code, detail="Loan Not Found")