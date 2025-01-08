#!/bin/bash

CONTAINER_NAME="simple_web_app_container"

if docker ps | grep -q $CONTAINER_NAME; then
  echo "Container $CONTAINER_NAME is running."
else
  echo "Container $CONTAINER_NAME is not running."
fi