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
3.  Else to simply download the image from GHCR
   ```bash
    docker run -d -p 5000:5000 --name simple_web_app_container ghcr.io/surfbum99/simple_web_app:latest

4. 
    Access the application at http://localhost:5000.

