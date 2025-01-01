# Flask Web App Development

This is a simple web application built using the Flask framework in Python.

## Requirements

- Python 3.x
- Flask

Check version of python that is installed:
```python
python3 --version
```

## Installation

1. Clone the repository:
```
git clone https://github.com/Petro96/Market.git
```
2. Navigate to the project directory:
```
cd file_name where you save clone_directory
```
3. Create a virtual environment:
```
python -m venv venv
```
4. Activate the virtual environment:
- On Windows:
```
venv\Scripts\activate
```
- On macOS/Linux:
```
source venv/bin/activate
```
5. Install the required packages:
```
pip install -r requirements.txt
```

## Running the Application

1. Set the Flask app environment variable:
```
set FLASK_APP=app.py
```
or on macOS/Linux:
```
export FLASK_APP=app.py
```
2. Run the Flask application:
```
flask run
```
3. Open your web browser and go to `http://127.0.0.1:5000/` to see the application in action.

# Flask Web App Docker Setup

This guide will help you build and run your Flask web application using Docker.

## Prerequisites

- Docker installed on your machine.

## Building the Docker Image

1. Clone the repository if you haven't already:

```sh
git clone https://github.com/Petro96/Market.git
cd Market
```

2. Build the Docker image:
```sh
docker build -t flask-web-app .
```

## Running the Docker Container

1. Run the Docker container:
```sh
docker run -d -p 5000:5000 --name flask-web-app-container flask-web-app
```

2. Open your web browser and go to `http://localhost:5000` to see the application in action.

## Stopping the Docker Container

1. Stop the running container:
```sh
docker stop flask-web-app-container
```

2. Remove the container:
```sh
docker rm flask-web-app-container
```

# Clone DockerHub image and run your App

This guide will help you pull the Docker image from Docker Hub and run your Flask web application using Docker.

## Prerequisites

- Docker installed on your machine.

## Pulling the Docker Image

1. Pull the Docker image from Docker Hub:
```sh
docker pull yourusername/flask-web-app:latest
```

## Running the Docker Container

1. Run the Docker container:
```sh
docker run -d -p 5000:5000 --name flask-web-app-container yourusername/flask-web-app:latest
```

2. Open your web browser and go to `http://localhost:5000` to see the application in action.

## Stopping the Docker Container

1. Stop the running container:
```sh
docker stop flask-web-app-container
```

2. Remove the container:
```sh
docker rm flask-web-app-container
```