import os

url_mongo = os.getenv("MONGO_URL", "mongodb://localhost:27017")
servidores_kafka = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9094")
topico_kafka = os.getenv("KAFKA_TOPIC", "pedidos-criados")
url_rabbitmq = os.getenv("RABBITMQ_URL", "amqp://guest:guest@localhost:5672/%2F")
fila_rabbitmq = os.getenv("RABBITMQ_QUEUE", "pedidos-criados")