import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app

@pytest.mark.asyncio(scope="session")
async def test_criar_pedido():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        resposta = await ac.post("/pedidos", json={"cliente": "joao", "produto": "notebook", "quantidade": 1})
    assert resposta.status_code == 200
    dados = resposta.json()
    assert dados["cliente"] == "joao"
    assert dados["status"] == "pendente"
    assert "id" in dados

@pytest.mark.asyncio(scope="session")
async def test_listar_pedidos():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        resposta = await ac.get("/pedidos")
    assert resposta.status_code == 200
    assert isinstance(resposta.json(), list)