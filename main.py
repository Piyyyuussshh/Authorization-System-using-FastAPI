from fastapi import FastAPI,Depends,status,Response
from database import SessionLocal
from database import engine 
import schemas
import models
from models import Blog,User
from hashing import bcrypt
from sqlalchemy.orm import Session


app = FastAPI()

'''
This is for Crud Operation

'''
models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

'''
This is for Blog
'''

@app.post('/',status_code=status.HTTP_201_CREATED,tags=["Blogs"]) 
def create(req:schemas.Blog,db:Session=Depends(get_db)):
    new_blog = Blog(title=req.title,body=req.body,user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.get('/blog/',tags=["Blogs"])
def get_blog(db:Session=Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@app.get('/blog/{id}',response_model=schemas.ShowBlog,status_code=200,tags=["Blogs"])
def show(id, response:Response, db:Session=Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"msg" : "data not found"}
    return blog

@app.delete('/blog/{id}',status_code=status.HTTP_204_NO_CONTENT,tags=["Blogs"])
def destroy(id ,response:Response, db:Session=Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id==id).delete(synchronize_session=False)
    db.commit()
    if not blog:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"msg" : "data not found"}
    return blog

@app.put('/blog/{id}',status_code=status.HTTP_202_ACCEPTED,tags=["Blogs"])
def update(id, response:Response, req:schemas.Blog, db:Session=Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id==id).update({"title":req.title,"body":req.body})
    db.commit()
    if not blog:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"msg" : "data not found"}
    return {"msg":"data updted"}


''' 
This is for User Models 

'''


@app.post('/user/',tags=["User"])
def create_user(req:schemas.User, db:Session=Depends(get_db)):
    user = User(name=req.name,email=req.email,password=bcrypt(req.password))
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"msg":"Data updated","data":user}

@app.get('/user/{id}',tags=["User"])
def get_user(id:int, response:Response, db:Session=Depends(get_db)):
    user = db.query(models.User).filter(models.User.id==id).first()
    if not user:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"msg" : "data not found"}
    return {"msg":"success","data":user}

