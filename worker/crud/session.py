import models
from crud.base import CRUDBase


class CRUDSession(CRUDBase):
    ...


session = CRUDSession(models.Session)
