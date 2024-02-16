from pydantic import BaseModel, validator
from src.enums.User_enums import Gender, Statuses, UserError


class User(BaseModel):
    id: int
    name: str
    email: str
    gender: Gender
    status: Statuses

    @validator('email')
    def check_that_in_email_address(cls, email):
        if '@' in email:
            return email
        else:
            raise ValueError(UserError.WRONG_EMAIL.value)

