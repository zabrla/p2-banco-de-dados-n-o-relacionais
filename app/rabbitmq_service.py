import pika
import json
from app.config import url_rabbitmq, fila_rabbitmq

def publicar_rabbitmq(mensagem: dict):
    try:
        parametros = pika.URLParameters(url_rabbitmq)
        conexao = pika.BlockingConnection(parametros)
        canal = conexao.channel()
        canal.queue_declare(queue=fila_rabbitmq, durable=True)
        canal.basic_publish(
            exchange="",
            routing_key=fila_rabbitmq,
            body=json.dumps(mensagem)
        )
        conexao.close()
    except Exception:
        pass