from dataclasses import dataclass
from typing import TypeVar

from pydantic import BaseModel
from sqlalchemy import orm

from db import Base

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)


@dataclass
class CRUDBase:
    model: ModelType

    def create(self, db: orm.Session, obj_in: CreateSchemaType):
        obj_in_data = obj_in.dict()
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
