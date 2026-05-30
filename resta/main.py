from fastapi import FastAPI

app = FastAPI(
    title="Microservicio de Resta",
    version="1.0.0",
    root_path="/resta"
)

@app.get("/")
def calcular_resta(a: int = 50, b: int = 20):
    return {"operacion": "resta", "valor_a": a, "valor_b": b, "resultado": a - b}