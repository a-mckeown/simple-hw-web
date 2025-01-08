# Simple Web Application Deployment with Docker and GitHub Actions

## Overview
This project demonstrates how to deploy a simple web application using Docker and GitHub Actions.

## Prerequisites
- Docker
- GitHub account

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd <repo-name>

    Build and run the Docker container locally:

    docker build -t simple_web_app .
    docker run -d -p 5000:5000 simple_web_app

    Else to simply download from GHCR

    docker run -d -p 5000:5000 --name simple_web_app_container ghcr.io/surfbum99/simple_web_app:latest

    

    Access the application at http://localhost:5000.

