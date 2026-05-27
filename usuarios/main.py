from fastapi import FastAPI

app = FastAPI()

@app.get("/usuarios")
def get_users():
    return {"id": 1, "name": "Juan"}, {"id": 2, "name": "Carlos"}