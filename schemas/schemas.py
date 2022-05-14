from typing import Optional
import datetime
from pydantic import BaseModel

class Blog(BaseModel):
    title:str
    body : str
    published : datetime.date