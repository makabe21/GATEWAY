from fastapi import FastAPI

app = FastAPI()

@app.get("/cursos")
def get_users():
    return {"id": 1, "titulo": "Matematicas"}, {"id": 2, "titulo": "progra"}