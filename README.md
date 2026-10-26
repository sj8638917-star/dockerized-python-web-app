

\# Dockerized Python Web Application



\## Project Overview

This project demonstrates how to containerize a Python Flask web application using Docker. The application runs inside a Docker container and is accessible through port 5000.



\## Technologies Used

\- Python 3.12

\- Flask

\- Docker

\- Git and GitHub



\## Project Features

\- Developed a web application using Python Flask.

\- Created a custom Dockerfile.

\- Built a Docker image using Docker CLI.

\- Ran the application inside a Docker container.

\- Mapped container port 5000 to the local machine.

\- Used Git and GitHub for version control.



\## Project Structure

```text

dockerized-python-web-app/

├── app.py

├── requirements.txt

├── Dockerfile

├── .gitignore

└── README.md

```



\## How to Run the Project



\### 1. Build the Docker Image

```bash

docker build -t docker-python-app .

```



\### 2. Run the Container

```bash

docker run -d -p 5000:5000 --name python-web-container docker-python-app

```



\### 3. Open the Application

Visit the following URL in your browser:



http://localhost:5000



\### 4. Stop the Container

```bash

docker stop python-web-container

```



\### 5. Remove the Container

```bash

docker rm python-web-container

```



\## Learning Outcomes

\- Understanding Docker images and containers.

\- Writing a Dockerfile.

\- Containerizing a Python application.

\- Port mapping and container management.

\- Using Git and GitHub for project version control.



\## Author

Sahil Jadhav



