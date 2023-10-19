from fastapi import FastAPI

app = FastAPI()

@app.get("/animals")
def get_all_animals():
    return {"Animals": "animals list"}

@app.post("/animals")
def add_animal():
    return {"Nothing yet": "same here"}