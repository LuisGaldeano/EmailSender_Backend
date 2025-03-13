# EmailSender_Backend

EmailSender_Backend is a backend service designed for automatic email dispatching in the background. 
It listens to a Kafka topic and processes messages asynchronously, ensuring scalable and efficient email handling.

## Features

* **Asynchronous Email Sending**: Processes and sends emails without blocking the main application thread.

* **Kafka Integration**: Subscribes to Kafka topics to receive email request messages.

* **Scalability**: Built to handle high message volumes and scale dynamically.

## Prerequisites

* Docker and Docker Compose installed.

## Installation

### Clone the repository:

```shell
git clone https://github.com/LuisGaldeano/EmailSender_Backend.git
```

### Navigate to the project directory:

```shell
cd EmailSender_Backend
```

### Create and configure the .env file:

Copy `.env-dist` and rename it to `.env`, then update the required environment variables like email credentials and Kafka configurations.

### Start all services using Make:

To launch all services, simply run the following command:

```shell
make
```

Running make will automatically start all required services and dependencies as defined in the Makefile.

## Usage

Once the services are running, the backend will subscribe to the Kafka topic and process incoming messages, 
sending them as emails accordingly.

## Project Structure

* **src/**: Contains the main application source code.

* **docker/**: Holds Docker-related configuration files.

* **.env-dist**: Example environment configuration file.

* **docker-compose.yml**: Defines the service structure for Docker Compose.

* **Makefile**: Includes useful commands for project management.