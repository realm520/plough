from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String

from app.db.base_class import Base

# if TYPE_CHECKING:
#     from .user import User  # noqa: F401


class MPCode(Base):
    id = Column(Integer, primary_key=True, index=True)
    phone = Column(String, index=True, nullable=False)
    code = Column(String, nullable=False)
    request_time = Column(Integer, index=True, nullable=False)
    expire_time = Column(Integer, index=True, nullable=False)
    status = Column(Integer, nullable=False)
