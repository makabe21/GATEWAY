from fastapi import FastAPI

app = FastAPI()

@app.get("/usuarios")
def get_users():
    return {"id": 1, "titulo": "Matematicas"}, {"id": 2, "titulo": "progra"}