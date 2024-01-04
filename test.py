import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_ola_mundo(): #Response
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Olá": "Mundo"}

    
def test_listar_produtos(): #Response
    response = client.get("/produtos")
    assert response.status_code == 200
    assert len(response.json()) == 3

def test_pegar_produtos(): #Response
    response = client.get("/produtos/1")
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "nome": "Smartphone",
        "descricao": "Um telefone que é inteligente",
        "preco": 1500.0,
    }