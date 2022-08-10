from typing import TYPE_CHECKING
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, func
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .user import User  # noqa: F401

class Order(Base):
    id = Column(Integer, primary_key=True, index=True)
    order_number = Column(String, unique=True, index=True)
    product_name = Column(String, index=True)
    amount = Column(Integer, comment="金额，单位'分'")
    pay_type = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("user.id"))
    owner = relationship("User", back_populates="orders")
    master_id = Column(Integer, index=True)
    divination = Column(String)
    create_time = Column(DateTime, server_default=func.now(), index=True, comment="创建时间")
    status = Column(Integer, comment="状态：0 - 未确认, 1 - 已支付, 2 - 已确认, 3 - 作废")