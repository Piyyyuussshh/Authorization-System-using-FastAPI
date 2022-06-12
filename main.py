from fastapi import FastAPI
from database import engine
import models
from routers import blog,user,authentication


app = FastAPI()

models.Base.metadata.create_all(engine)
# This route is used for blogs
app.include_router(blog.router) 
# Thi route is used for users
app.include_router(user.router) # 

app.include_router(authentication.router)

