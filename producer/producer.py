import json
import time
import uuid
from datetime import datetime
import logging
from setup import get_connection, get_channel, RABBITMQ_QUEUE, SEND_INTERVAL


logging.basicConfig(level=logging.INFO)

connection = get_connection()
channel = get_channel(connection)


def send_message():
    while True:
        message_id = str(uuid.uuid4())
        created_on = datetime.now().isoformat()
        message = {
            'message_id': message_id,
            'created_on': created_on,
        }

        logging.info(f"Sending message: {message}")

        channel.basic_publish(
            exchange='',
            routing_key=RABBITMQ_QUEUE,
            body=json.dumps(message).encode('utf-8'),
        )

        time.sleep(SEND_INTERVAL)


if __name__ == '__main__':
    try:
        send_message()
    except KeyboardInterrupt:
        logging.info("Producer stopped")
    finally:
        connection.close()
