from pydantic import BaseModel

class pedido(BaseModel):
    cliente: str
    produto: str
    quantidade: int

class pedidodb(pedido):
    id: str
    status: str = "pendente"