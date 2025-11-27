from fastapi import FastAPI,HTTPException
from app.schemas import PostCreate
app = FastAPI()



# @app.get('/hello-world')
# def helloworld():
#     return {"message":"Hello World"}



text_posts = {
     1:{"title":"New Post","content":"cool test post"},
     2:{"title":"New Post","content":"cool test post"},
     3:{"title":"New Post","content":"cool test post"},
     4:{"title":"New Post","content":"cool test post"},
     5:{"title":"New Post","content":"cool test post"},
     6:{"title":"New Post","content":"cool test post"},
     7:{"title":"New Post","content":"cool test post"},
     8:{"title":"New Post","content":"cool test post"},

}

@app.get("/posts")
def get_all_posts(limit:int=None):
    if limit:
        return list(text_posts.values())[:limit]
    return text_posts 



# path parameters
@app.get("/post/{id}")
def get_post(id:int):
    if id not in text_posts:
        raise HTTPException(status_code=404,detail="Post not found")
    return text_posts.get(id)



# request body // POST

@app.post("/posts")
def create_post(post:PostCreate):
    new_post = {"title":post.title,"content":post.content}
    text_posts[max(text_posts.keys)+1] = new_post
    return new_post


