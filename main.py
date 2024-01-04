from fastapi import FastAPI

app = FastAPI()

@app.get("/") #Recebe requisição
def ola_mundo(): #Response
    return {"Olá": "Mundo"}