from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hello():
    return {'message': 'hello world has been excicuted'}

@app.get("/about")
def about():
    return {"me"}