
from fastapi import APIRouter, Header, HTTPException
from schemas import LoanCreate, LoanFinalResponse, LoanMetadata
from app.services.loan_service import LoanService  
from models.bank import Bank
from errors.errors_borrowed import (
    CreditScoreError, ZeroAmount, TimeToPay, 
    NoNameClient, BankCapitalError, DefaultName
)



router = APIRouter(prefix="/loans", tags=["loans"])
bank = Bank("Banamex", 1_000_000)
loan_service = LoanService(bank)


@router.post("/bulk", response_model= LoanFinalResponse, status_code=201)
def create_loan( 
    loan_data: LoanCreate, 
    x_user_id: str = Header(default = "Admin")
    ):
    try:
        loan = loan_service.create_loan(loan_data)
        metadata = LoanMetadata(created_by = x_user_id)
        return LoanFinalResponse(
            data = loan.to_response(), 
            metadata = metadata 
        )

    except CreditScoreError:
        raise HTTPException(
            status_code=422, 
            detail="Credit score must be between 300-850"
            ) 
    except (NoNameClient, DefaultName):
        raise HTTPException(
            status_code=422, 
            detail="Invalid client name"
            )
    except (ZeroAmount, TimeToPay): 
        raise HTTPException(
            status_code = 422,
            detail= "Invalid amount or time period"
        )
    except BankCapitalError:
        raise HTTPException(status_code=400, detail="Bank lacks sufficient capital for this loan")
    