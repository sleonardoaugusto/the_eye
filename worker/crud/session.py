from sqlalchemy import orm

import models
from crud.base import CRUDBase, CreateSchemaType


class CRUDSession(CRUDBase):
    def get_or_create(self, db: orm.Session, obj_in: CreateSchemaType):
        instance = db.query(self.model).filter_by(**obj_in.dict()).first()
        if instance:
            return instance
        else:
            obj_in_data = obj_in.dict()
            db_obj = self.model(**obj_in_data)
            db.add(db_obj)
            db.commit()
            db.refresh(db_obj)
            return db_obj


session = CRUDSession(models.Session)
