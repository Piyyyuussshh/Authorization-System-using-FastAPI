from fastapi import APIRouter, Depends, HTTPException,status,Response
from fastapi.security import OAuth2PasswordRequestForm
from requests import Session
from sqlalchemy.orm import Session
import schemas,database,models,hashing,token



router = APIRouter(
    tags=['authentication']
)

@router.post('/login')
def login(req:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email==req.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    if not hashing.verify(req.password,user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'incorrect password')
    
    access_token = token.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}