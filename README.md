# RabbitMQ Producer-Consumer Example

This project demonstrates a simple producer-consumer system using RabbitMQ, Docker, and Python. It includes a producer that sends messages to a RabbitMQ queue and a consumer that reads and processes those messages.

## Prerequisites

- Docker
- Docker Compose
- Python 3.11 or later

## Setup

1. Clone this repository to your local machine.
2. Navigate to the project directory.

## Configuration

The project uses environment variables for configuration. Copy the `.env-example` file to a new file named `.env` and adjust the values as necessary.

```
cp .env-example .env
```

## Building and Running

To build and run the producer and consumer services along with RabbitMQ, use Docker Compose:

```
docker-compose up --build
```

This command builds the Docker images for the producer and consumer, starts the RabbitMQ service, and runs the producer and consumer containers.

## Architecture

- **RabbitMQ**: Acts as the message broker.
- **Producer**: A Python script that sends messages to a RabbitMQ queue.
- **Consumer**: A Python script that consumes messages from the RabbitMQ queue.

## Services

- `rabbitmq`: The RabbitMQ server accessible on ports 5672 (AMQP) and 15672 (management interface).
- `producer`: The Python script that produces messages.
- `consumer`: The Python script that consumes messages.

## Environment Variables

- `RABBITMQ_HOST`: The hostname of the RabbitMQ server.
- `RABBITMQ_QUEUE`: The name of the RabbitMQ queue to use.
- `RABBITMQ_DEFAULT_USER`: The default user for RabbitMQ.
- `RABBITMQ_DEFAULT_PASS`: The password for the default RabbitMQ user.
- `SEND_INTERVAL_SEC`: Interval in seconds between messages sent by the producer.