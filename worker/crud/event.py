import models
from crud.base import CRUDBase


class CRUDEvent(CRUDBase):
    ...


event = CRUDEvent(models.Event)
