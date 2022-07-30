from schemas import BlogSchema
from fastapi import Depends, FastAPI, HTTPException,status,Response
from models import *
from database import SessionLocal, engine
from sqlalchemy.orm import Session

app = FastAPI()
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/blog/",status_code=status.HTTP_201_CREATED)
def Create(blog:BlogSchema,db:Session=Depends(get_db)):
    new_blog = Blog(**blog.dict())
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog
    
@app.get("/blog/")
def all_blogs(db:Session=Depends(get_db)):
    return db.query(Blog).all()

@app.get("/blog/{id}/",status_code = status.HTTP_200_OK)
def show(id:int,response:Response,db:Session=Depends(get_db)):
    blog_filter = db.query(Blog).filter(Blog.id == id).first()
    blog_get = db.query(Blog).get(id)
    if not blog_filter or not blog_get:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog {id} not found")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"message": f"Blog {id} not found"}
    return blog_get

@app.delete("/blog/{id}/",status_code = status.HTTP_204_NO_CONTENT)
def destroy(id:int,db:Session=Depends(get_db)):
    blog_get = db.query(Blog).get(id)
    if not blog_get:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog {id} not found")
    db.delete(blog_get)
    db.commit()
    return {"message": f"Blog {id} deleted"}

@app.delete("/blog2/{id}/",status_code = status.HTTP_204_NO_CONTENT)
def destroy2(id:int,db:Session=Depends(get_db)):
    blog_get = db.query(Blog).filter(Blog.id == id)
    if not blog_get.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog {id} not found")
    blog_get.delete(synchronize_session=False)
    db.commit()
    return 'done'

@app.put("/blog/{id}/",status_code = status.HTTP_200_OK)
def update(id:int,blog:BlogSchema,db:Session=Depends(get_db)):
    nedata = db.query(Blog).filter(Blog.id == id)
    if not nedata.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog {id} not found")
    nedata.update(blog.dict())
    db.commit()
    return {"message": f"Blog {id} updated"}