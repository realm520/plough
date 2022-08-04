from typing import Optional

from pydantic import BaseModel, EmailStr


# Shared properties
class MasterBase(BaseModel):
    phone: Optional[str] = None

# Properties to receive via API on creation
class MasterCreate(MasterBase):
    pass


class MasterRegister(MasterBase):
    password: Optional[str] = None
    name: Optional[str] = None

# Properties to receive via API on update
class MasterUpdate(MasterBase):
    name: Optional[str] = None
    status: Optional[int] = True
    phone: Optional[str] = None
    rate: Optional[int] = None
    password: Optional[str] = None


class MasterInDBBase(MasterBase):
    id: Optional[int] = None
    name: Optional[str] = None
    rate: Optional[int] = None
    order_number: Optional[int] = None
    order_amount: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class Master(MasterInDBBase):
    pass


# Additional properties stored in DB
class MasterInDB(MasterInDBBase):
    hashed_password: str
