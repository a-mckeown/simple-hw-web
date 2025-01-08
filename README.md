# Simple Web Application Deployment with Docker and GitHub Actions

## Overview
This project demonstrates how to deploy a simple web "Hello World" application using Docker and GitHub Actions.

## Prerequisites
- Docker
- GitHub account

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/surfbum99/simple-hw-web
   cd simple-hw-web

2. Build and run the Docker container locally:
   ```bash
    docker build -t simple_web_app .
    docker run -d -p 5000:5000 simple_web_app
   
3.  Or download the image from GHCR
   ```bash
    docker run -d -p 5000:5000 --name simple_web_app_container ghcr.io/surfbum99/simple_web_app:latest
   ```
## Access the application at http://localhost:5000

   Make sure there isn't anything already running on your local machine on TCP port 5000 as this is a common port for testing on.
   It is also commonly used for Apple's Airplay receiver.
   ```bash
   sudo lsof -i :5000
   ```

4. Monitoring

   There is a basic monitor.sh script avaliable to check if the container is running.
