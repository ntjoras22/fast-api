from fastapi import FastAPI
from typing import Optional
import uvicorn
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
   
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


@app.get("/blog")
def index (limit = 10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {"data": f"{limit} published blog posts from the db"}
    else:
        return {"data": f"{limit} blog posts from the db"}

@app.get("/blog/unpublished")
def unpublished():
    return {"data": "all unpublished blog posts from the db"}
@app.get("/blog/{id}")
def show(id: int):
    return {"data": f"blog post with id {id}"}  
@app.get("/blog/{id}/comments")
def comments(id, limit=10):
    return {"data": {'1','2','3'}}
class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]
@app.post("/blog")
def create_blog(blog: Blog):
    return {"data": f"blog was created with title as {blog.title} and body as {blog.body} "}

if __name__ == "__main__":
    
    uvicorn.run(app, host="127.0.0.1", port=8001)