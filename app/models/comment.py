from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.db.base_class import Base


class Comment(Base):
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("order.id"))
    master_id = Column(Integer, ForeignKey("master.id"))
    user_id = Column(Integer, ForeignKey("user.id"))
    content = Column(String)
    rate = Column(Integer, nullable=False)
    status = Column(Integer, nullable=False)
