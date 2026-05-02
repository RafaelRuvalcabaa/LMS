from pydantic import BaseModel, Field, field_serializer
from datetime import datetime
import importlib.util
from typing import Annotated, TypeAlias
from utils.request_id import generate_request_id


_HAS_EMAIL_VALIDATOR = importlib.util.find_spec("email_validator") is not None

if _HAS_EMAIL_VALIDATOR:
    from pydantic import EmailStr as _EmailStr  # type: ignore
    EmailType: TypeAlias = _EmailStr
else:
    # Fallback: avoid hard dependency on `email-validator` while still validating basic format.
    EmailType: TypeAlias = Annotated[str, Field(pattern=r"^[^@\s]+@[^@\s]+\.[^@\s]+$")]


class LoanCreate(BaseModel):
    name: str
    last_name: str
    city: str
    credit_history: int = Field(ge=300, le=850)
    amount: float = Field(gt=10000)
    time: int = Field(ge=6, le=72)
    email: EmailType

class LoanResponse(LoanCreate): 
    status: bool 
    summary: str 

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
