from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/about/")
def about():
    return {"about": "about"}


@app.get('/items/unpublish/')
def unpublish():
    return {"unpublish": "unpublish"}

@app.get("/items/{item_id}/")
def item(item_id:int):
    return {"item": item_id}

