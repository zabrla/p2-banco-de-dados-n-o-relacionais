from kafka import KafkaProducer
import json
from app.config import servidores_kafka, topico_kafka

def publicar_kafka(mensagem: dict):
    try:
        produtor = KafkaProducer(
            bootstrap_servers=servidores_kafka,
            value_serializer=lambda v: json.dumps(v).encode("utf-8")
        )
        produtor.send(topico_kafka, mensagem)
        produtor.flush()
    except Exception:
        pass