from fastapi import FastAPI
from Schemas.schemas import Blog

app = FastAPI()



@app.post('/')
def create(blog : Blog):
    print(blog.title)
    print(blog.body)
    print(blog.published)
    return blog