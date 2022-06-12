import email
from pydantic import BaseModel
from typing import List


class Blog(BaseModel):
    title: str
    body: str

    class Config:
        orm_mode = True


class User(BaseModel):
    name: str
    email: str
    password: str


class ShowUser(User):
    name: str
    email: str
    blog: List[Blog] = []
    password: str

    class Config:
        orm_mode = True


class ShowBlog(Blog):
    title: str
    body: str
    creator: ShowUser

    class Config:
        orm_mode = True

class Login(BaseModel):
    username:str
    password:str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str