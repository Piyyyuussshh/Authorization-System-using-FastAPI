from fastapi import FastAPI
from schemas.models import Blog
from Database.database import engine 

app = FastAPI()

models.Base.metadata.create_all(engine)

@app.post('/')
def create(blog : Blog):
    print(blog.title)
    print(blog.body)
    print(blog.published)
    return blog