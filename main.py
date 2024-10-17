from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/welcome")
def read_welcome():
    return {"welcome": "world"}