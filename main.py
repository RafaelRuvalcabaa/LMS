
from fastapi import FastAPI
from routers.loan_post import router as loan_router


def create_app(): 
    app = FastAPI(
        title= "Loan System API",
        description= "Loan System by Rafael Ruvalcaba",
        version="1.0.0"
)
    app.include_router(loan_router)
    @app.get("/")
    def root(): 
        return {"status": "Ok", "message": "Loan System is running"}
    
    return app 

app = create_app()