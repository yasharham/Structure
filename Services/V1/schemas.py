from pydantic import BaseModel
from typing import Optional, List

class SchemaName(BaseModel):
    request_1:str
    request_2:Optional[List]


class ResponseSchema():
    class Config:
        orm_mode = True
