from pydantic import BaseModel, Field, field_serializer
from datetime import datetime
from utils.request_id import generate_request_id


class LoanCreate(BaseModel):
    name: str
    last_name: str
    city: str 
    credit_history: int = Field(..., ge=300, le=850)
    amount: float = Field(..., gt=10000)
    time: int = Field(..., ge=6, le=72)

class LoanResponse(LoanCreate): 
    status: bool 
    summary : str 

class LoanMetadata(BaseModel): 
    created_at: datetime = Field(default_factory=datetime.now)
    created_by: str 
    request_id: str = Field(default_factory=generate_request_id)
    @field_serializer('created_at')
    def formate_time(self, dt: datetime, __info): 
        return dt.strftime("%Y-%m-%d %H:%M:%S")


class LoanFinalResponse(BaseModel): 
    data: LoanResponse
    metadata: LoanMetadata
