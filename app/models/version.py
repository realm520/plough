from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String

from app.db.base_class import Base


class Version(Base):
    id = Column(Integer, primary_key=True, index=True)
    product = Column(String, index=True, nullable=False)
    version = Column(String, index=True, nullable=False)
    desc = Column(String, nullable=False)
    release_time = Column(Integer, index=True, nullable=False)
    status = Column(Integer, nullable=False)
