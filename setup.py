import os
import pika
from dotenv import load_dotenv
import logging

logging.basicConfig(level=logging.INFO)

load_dotenv()

RABBITMQ_HOST = os.getenv('RABBITMQ_HOST', 'localhost')
RABBITMQ_QUEUE = os.getenv('RABBITMQ_QUEUE', 'local_queue')


def get_connection():
    return pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST))


def get_channel(connection):
    channel = connection.channel()
    channel.queue_declare(queue=RABBITMQ_QUEUE)
    return channel


SEND_INTERVAL = int(os.getenv('SEND_INTERVAL_SEC', 1))
