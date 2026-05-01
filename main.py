
from fastapi import FastAPI
from routers.loan_post import router as loan_router
from app.config import get_settings

settings = get_settings()

def create_app(): 
    app = FastAPI(
        title= settings.app_name,
        description= settings.app_description,
        version= settings.app_version,
        debug=settings.debug
    )
    app.include_router(loan_router)
    @app.get("/")
    def root(): 
        return {"status": "Ok", "message": "Loan System is running"}
    
    return app 

app = create_app()