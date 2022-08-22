from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String

from app.db.base_class import Base


class Version(Base):
    id = Column(Integer, primary_key=True, index=True)
    product = Column(String, index=True, nullable=False)
    vstr = Column(String, index=True, nullable=False)
    desc = Column(String)
    memo = Column(String)
    url = Column(String)
    release_time = Column(Integer, index=True, nullable=False)
    status = Column(Integer, nullable=False)
