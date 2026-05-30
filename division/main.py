from fastapi import FastAPI

app = FastAPI(
    title="Microservicio de División",
    version="1.0.0",
    root_path="/division"
)

@app.get("/")
def calcular_division(a: int = 100, b: int = 4):
    if b == 0:
        return {"error": "No se puede dividir entre cero"}
    return {"operacion": "división", "valor_a": a, "valor_b": b, "resultado": a / b}