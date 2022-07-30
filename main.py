from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/blog/")
def about(limit=10,publish:bool=True,sort:Optional[str]=None):
    x='pup' if publish else 'unpup'
    return {"about": f"about - {limit} - {x} - {sort}"}


@app.get('/items/unpublish/')
def unpublish():
    return {"unpublish": "unpublish"}

@app.get("/items/{item_id}/")
def item(item_id:int):
    return {"item": item_id}

@app.get("/items/{item_id}/comments/")
def comments(item_id,limit=10):
    return {"comments": {item_id,item_id+'1'}}


class BlogPost(BaseModel):
    title: str
    body: str
    published: Optional[bool]=True

@app.post('/blog/')
def create_blog(blog:BlogPost):
    print(blog.body)
    return blog


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)