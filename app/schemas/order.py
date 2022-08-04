from typing import Optional

from pydantic import BaseModel


# Shared properties
class OrderBase(BaseModel):
    product_name: str
    master: Optional[str] = None
    master_id: Optional[int] = None
    amount: Optional[int] = 0
    pay_type: Optional[str] = None

# Properties to receive on item creation
class OrderCreate(OrderBase):
    pass


# Properties to receive on item update
class OrderUpdate(OrderBase):
    status: Optional[int] = 0


# Properties shared by models stored in DB
class OrderInDBBase(OrderBase):
    id: int
    order_number: str
    owner_id: int
    status: Optional[int] = 0

    class Config:
        orm_mode = True


# Properties to return to client
class Order(OrderInDBBase):
    pass


# Properties properties stored in DB
class OrderInDB(OrderInDBBase):
    pass
