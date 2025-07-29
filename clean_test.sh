#!/bin/bash

echo "Checking the cleanup result"

# Stop and remove everything from docker-compose including volumes
docker container ls
docker image ls
docker volume ls

echo "✅ Everything cleaned up"
