from random import sample
from string import ascii_letters, digits
from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session

from app.core.security import get_password_hash, verify_password
from app.crud.base import CRUDBase
from app.models.master import Master
from app.schemas.master import MasterCreate, MasterUpdate, MasterRegister, MasterStatus


class CRUDMaster(CRUDBase[Master, MasterCreate, MasterUpdate]):
    def get_by_name(self, db: Session, *, name: str) -> Optional[Master]:
        return db.query(Master).filter(Master.name == name).first()

    def get_by_phone(self, db: Session, *, phone: str) -> Optional[Master]:
        return db.query(Master).filter(Master.phone == phone).first()

    def login_or_register(self, db: Session, *, phone: str, verify_code: str) -> Optional[Master]:
        master = self.get_by_phone(db, phone=phone)
        if not master and verify_code == "9999":
            return self.create(db, obj_in=MasterCreate(phone=phone))
        elif verify_code == "9988":
            return master
        else:
            return None

    def create(self, db: Session, *, obj_in: MasterCreate) -> Master:
        master = self.get_by_phone(obj_in.phone)
        if not master or master.status == MasterStatus.refused:
            db_obj = Master(
                hashed_password=get_password_hash("12345678"),
                name=obj_in.name,
                avatar=obj_in.avatar,
                rate=40,
                phone=obj_in.phone,
                price=0,
                status=MasterStatus.inactive.value
            )
            db.add(db_obj)
            db.commit()
            db.refresh(db_obj)
            return db_obj
        else:
            return None

    def register(self, db: Session, *, obj_in: MasterRegister) -> Master:
        if obj_in.verify_code == "9999":
            master = self.get_by_phone(db=db, phone=obj_in.phone)
            if not master or master.status == MasterStatus.refused:
                db_obj = Master(
                    hashed_password=get_password_hash("12345678"),
                    name=obj_in.name,
                    avatar=obj_in.avatar,
                    rate=40,
                    phone=obj_in.phone,
                    status=MasterStatus.inactive.value
                )
                db.add(db_obj)
                db.commit()
                db.refresh(db_obj)
                return db_obj
            else:
                return None
        else:
            return None

    def update(
        self, db: Session, *, db_obj: Master, obj_in: Union[MasterUpdate, Dict[str, Any]]
    ) -> Master:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        if "password" in update_data and update_data["password"]:
            hashed_password = get_password_hash(update_data["password"])
            del update_data["password"]
            update_data["hashed_password"] = hashed_password
        return super().update(db, db_obj=db_obj, obj_in=update_data)

    def is_active(self, master: Master) -> bool:
        return master.status == 1


master = CRUDMaster(Master)
