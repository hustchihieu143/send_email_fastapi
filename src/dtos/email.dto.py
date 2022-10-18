from typing import Optional
from pydantic import BaseModel
from pydantic.networks import EmailStr
from pydantic.types import conint

class CreateEmailDto(BaseModel):
    password: str
    name: Optional[str]