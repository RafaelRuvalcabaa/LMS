
from fastapi import APIRouter, Header, HTTPException, status
from schemas import LoanCreate, LoanFinalResponse, LoanMetadata
from app.services.loan_service import LoanService  
from models.bank import Bank
from errors.errors_borrowed import (
    CreditScoreError, ZeroAmount, TimeToPay, 
    NoNameClient, BankCapitalError, DefaultName
)



router = APIRouter(prefix="/loans", tags=["loans"])
bank = Bank.get_instance()
loan_service = LoanService(bank)


@router.post("/bulk", response_model= LoanFinalResponse, status_code=201)
def create_loan( 
    loan_data: LoanCreate, 
    x_user_id: str = Header(default = "Admin")
    ):
    """
    Crea un nuevo préstamo.
    
    - **201:** Préstamo creado exitosamente
    - **422:** Datos inválidos (credit score, montos, tiempos, nombres)
    - **400:** Banco sin capital suficiente
    """
    try:
        loan = loan_service.create_loan(loan_data, created_by=x_user_id)
        
        metadata = LoanMetadata(
            created_at=loan.created_at,
            created_by=loan.created_by,
            request_id=loan.request_id
        )
        
        return LoanFinalResponse(
            data=loan.to_response(), 
            metadata=metadata 
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
    
@router.get("/all", response_model=list[LoanFinalResponse], status_code=200)
def get_all_loans():
    """
    Get all loan registered.
    -**200:** List of loans (could be empty)
    """
    try: 
        loans = loan_service.get_all_loan()
        response = []
        for loan in loans: 
            loan_response = loan.to_response()
            metadata = LoanMetadata(
                created_at=loan.created_at,
                created_by=loan.created_by,
                request_id=loan.request_id
            )
            response.append(LoanFinalResponse(data=loan_response, metadata=metadata))
        return response 

    except Exception as e: 
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")