from fastapi import FastAPI

app = FastAPI(
    title="Microservicio de Suma",
    version="1.0.0",
    root_path="/suma"
)

@app.get("/")
def calcular_suma(a: int = 10, b: int = 5):
    return {"operacion": "suma", "valor_a": a, "valor_b": b, "resultado": a + b}