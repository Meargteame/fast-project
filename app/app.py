from fastapi import FastAPI
app = FastAPI()



@app.get('/hello-world')
def helloworld():
    return {"message":"Hello World"}



