from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String

from app.db.base_class import Base

# if TYPE_CHECKING:
#     from .user import User  # noqa: F401


class Product(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    desc = Column(String)
    status = Column(Integer, nullable=False)
