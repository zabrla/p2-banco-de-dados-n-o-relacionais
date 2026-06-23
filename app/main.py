from fastapi import FastAPI
from app.models import pedido, pedidodb
from app.database import colecao
from app.rabbitmq_service import publicar_rabbitmq
from app.kafka_service import publicar_kafka
import uuid

app = FastAPI()

@app.post("/pedidos", response_model=pedidodb)
async def criar_pedido(p: pedido):
    novo_pedido = pedidodb(
        id=str(uuid.uuid4()),
        cliente=p.cliente,
        produto=p.produto,
        quantidade=p.quantidade,
        status="pendente"
    )
    pedido_dict = novo_pedido.model_dump()
    await colecao.insert_one(pedido_dict.copy())
    
    publicar_rabbitmq({"id": novo_pedido.id})
    publicar_kafka(pedido_dict)
    
    return novo_pedido

@app.get("/pedidos")
async def listar_pedidos():
    cursor = colecao.find({}, {"_id": 0})
    pedidos = await cursor.to_list(length=100)
    return pedidos