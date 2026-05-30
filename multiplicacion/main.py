from fastapi import FastAPI

app = FastAPI(
    title="Microservicio de Multiplicación",
    version="1.0.0",
    root_path="/multiplicacion"
)

@app.get("/")
def calcular_multiplicacion(a: int = 6, b: int = 7):
    return {"operacion": "multiplicación", "valor_a": a, "valor_b": b, "resultado": a * b}