import json
import logging
from setup import get_channel, get_connection, RABBITMQ_QUEUE

logging.basicConfig(level=logging.INFO)

connection = get_connection()
channel = get_channel(connection)

logging.info(f"Connected to RabbitMQ. Queue: {RABBITMQ_QUEUE}")
logging.info(f"Connection: {connection}")


def callback(ch, method, properties, body):
    message = body.decode('utf-8')
    json_message = json.loads(message)
    logging.info(f"Received message: {json_message}")


channel.basic_consume(
    queue=RABBITMQ_QUEUE,
    on_message_callback=callback,
    auto_ack=True
)

logging.info("Waiting for messages. To exit press CTRL+C")
try:
    channel.start_consuming()
except KeyboardInterrupt:
    logging.info("Consumer stopped")
finally:
    connection.close()
