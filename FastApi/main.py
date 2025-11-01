from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def message_hello():
    return {'message': 'hello world has been excicuted'}