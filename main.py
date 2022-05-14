from fastapi import FastAPI,Depends
from database import SessionLocal
from database import engine 
import schemas
import models
from models import Blog
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/')
def create(req:schemas.Blog,db:Session=Depends(get_db)):
    new_blog = Blog(title=req.title,body=req.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog