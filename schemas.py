import imp
from pydantic import BaseModel

class Blog(BaseModel):
    title : str
    body : str
