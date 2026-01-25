from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"page": "index"}

@app.get("/page1")
def page1():
    return {"page": "page1"}

@app.get("/page2")
def page2():
    return {"page": "page2"}