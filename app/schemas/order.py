from enum import Enum
from typing import Optional

from pydantic import BaseModel

class OrderStatus(Enum):
    init: int = 0
    checked: int = 1
    done: int = 2
    cancel: int = 3


# Shared properties
class OrderBase(BaseModel):
    pass

# Properties to receive on item creation
class OrderCreate(OrderBase):
    product_id: int
    master_id: Optional[int] = None
    amount: Optional[int] = 0
    pay_type: Optional[str] = None


# Properties to receive on item update
class OrderUpdate(OrderCreate):
    status: Optional[OrderStatus] = OrderStatus.init

class OrderUpdateDivination(OrderBase):
    divination: Optional[str] = None

# Properties shared by models stored in DB
class OrderInDBBase(OrderCreate):
    id: int
    order_number: str
    owner_id: int
    divination: Optional[str] = None
    create_time: Optional[str] = None
    status: Optional[OrderStatus] = OrderStatus.init

    class Config:
        orm_mode = True


# Properties to return to client
class Order(OrderInDBBase):
    master_name: Optional[str] = None


# Properties properties stored in DB
class OrderInDB(OrderInDBBase):
    pass
