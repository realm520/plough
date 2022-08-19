from typing import Optional
import uuid
import time

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.version import Version
from app.schemas.version import VersionUpdate, VersionCreate


class CRUDVersion(CRUDBase[Version, VersionCreate, VersionUpdate]):
    pass
    def get_by_product(self, db: Session, *, product: str) -> Optional[Version]:
        return db.query(Version) \
            .filter(Version.product == product) \
            .order_by(Version.release_time.desc()) \
            .first()


version = CRUDVersion(Version)
