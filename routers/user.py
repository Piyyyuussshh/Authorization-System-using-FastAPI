from fastapi import Depends,status,Response
from fastapi import APIRouter
from sqlalchemy.orm import Session
from models import User
import hashing
import schemas
import database
import models

router = APIRouter()

@router.post('/user/',tags=["User"])
def create_user(req:schemas.User, db:Session=Depends(database.get_db)):
    user = User(name=req.name,email=req.email,password=hashing.bcrypt(req.password))
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"msg":"Data updated","data":user}

@router.get('/user/{id}',tags=["User"])
def get_user(id:int, response:Response, db:Session=Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.id==id).first()
    if not user:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"msg" : "data not found"}
    return {"msg":"success","data":user}