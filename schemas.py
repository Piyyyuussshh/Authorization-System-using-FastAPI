from pydantic import BaseModel

class Blog(BaseModel):
    title : str
    body : str



class User(BaseModel):
    name : str
    email : str
    password : str


class ShowUser(User):
    name : str
    email : str
    password : str

    class Config:
        orm_mode = True

class ShowBlog(Blog):
    title : str
    body : str
    creator : ShowUser

    class Config:
        orm_mode = True