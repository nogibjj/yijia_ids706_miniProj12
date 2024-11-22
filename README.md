# yijia_ids706_miniProj12

## Overview
This repository demonstrates a simple Python application to calculate the mean of numbers entered by the user. The application is containerized using Docker and managed with a CI/CD pipeline integrated with GitHub Actions to deploy the Docker image to Docker Hub.


## CI/CD Badge
[![Build and Push Docker Image](https://github.com/nogibjj/yijia_ids706_miniProj12/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/yijia_ids706_miniProj12/actions/workflows/cicd.yml)


## Link to Docker Image
Find the Docker image on Docker Hub: [yijia123/mini12](https://hub.docker.com/repository/docker/yijia123/mini12/general).


## File Structure
```bash
├── Dockerfile          # Instructions for containerizing the app
├── requirements.txt    # Python dependencies
├── app.py              # Main Python Flask application
├── Makefile            # Automation for Docker commands
└── README.md           # Project documentation
```


## Setup Instructions
### 1. Install Prerequisites
    Install Docker

### 2. Clone the Repository
```sh
git clone https://github.com/nogibjj/yijia_ids706_miniProj12.git
cd yijia_ids706_miniProj12
``` 

### 3. Build the Docker Image
Use the make command to build the Docker image:
```sh
make build
```

### 4. Run the Docker Container
Run the Flask application in a Docker container:
```sh
make run
```
The application will be accessible at: http://127.0.0.1:8080.

## Application Functionality
This application calculates the mean of a list of numbers provided by the user.

### How It Works:
1. Access the application via a browser at http://127.0.0.1:8080.
2. Enter a comma-separated list of numbers in the form and submit.
3. The application will calculate and display the mean of the provided numbers.

## CI/CD Workflow for Deployment to Docker Hub
### Prerequirement 
Set up the following secrets in your GitHub repository under Settings > Secrets and variables > Actions:
* DOCKER_USERNAME: Your Docker Hub username.
* DOCKER_PASSWORD: Your Docker Hub password or access token.

### CI/CD Workflow
1. Automatically builds the Docker image when changes are pushed to the main branch.
2. Pushes the built Docker image to Docker Hub.
