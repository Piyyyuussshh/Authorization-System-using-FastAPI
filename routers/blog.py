from fastapi import Depends,status,Response
from fastapi import APIRouter
from sqlalchemy.orm import Session
from models import Blog
import Oauth2
import schemas
import database
import models


router = APIRouter(
    tags=['blogs']
)


@router.get('/blog/')
def get_blog(db:Session=Depends(database.get_db),current_user:schemas.User=Depends(Oauth2.get_current_user)):
    blogs = db.query(models.Blog).all()
    return blogs


@router.post('/',status_code=status.HTTP_201_CREATED) 
def create(req:schemas.Blog,db:Session=Depends(database.get_db),current_user:schemas.User=Depends(Oauth2.get_current_user)):
    new_blog = Blog(title=req.title,body=req.body,user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@router.get('/blog/{id}',response_model=schemas.ShowBlog,status_code=200)
def show(id, response:Response, db:Session=Depends(database.get_db),current_user:schemas.User=Depends(Oauth2.get_current_user)):
    blog = db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"msg" : "data not found"}
    return blog

@router.delete('/blog/{id}',status_code=status.HTTP_204_NO_CONTENT)
def destroy(id ,response:Response, db:Session=Depends(database.get_db),current_user:schemas.User=Depends(Oauth2.get_current_user)):
    blog = db.query(models.Blog).filter(models.Blog.id==id).delete(synchronize_session=False)
    db.commit()
    if not blog:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"msg" : "data not found"}
    return blog

@router.put('/blog/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id, response:Response, req:schemas.Blog, db:Session=Depends(database.get_db),current_user:schemas.User=Depends(Oauth2.get_current_user)):
    blog = db.query(models.Blog).filter(models.Blog.id==id).update({"title":req.title,"body":req.body})
    db.commit()
    if not blog:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"msg" : "data not found"}
    return {"msg":"data updted"}

