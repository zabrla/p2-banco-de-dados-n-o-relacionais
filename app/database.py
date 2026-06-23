from motor.motor_asyncio import AsyncIOMotorClient
from app.config import url_mongo

cliente_mongo = AsyncIOMotorClient(url_mongo)
db = cliente_mongo.pedidos_db
colecao = db.pedidos