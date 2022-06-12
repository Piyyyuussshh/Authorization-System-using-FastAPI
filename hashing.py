from passlib.context import CryptContext


pwd_cxt = CryptContext(schemes=["bcrypt"],deprecated="auto")

def bcrypt(password:str):
    hashed_pwd = pwd_cxt.hash(password)
    return hashed_pwd

def verify(plain_pwd,hashed_pwd):
    return pwd_cxt.verify(plain_pwd,hashed_pwd)
