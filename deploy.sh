#!/bin/bash
echo "Starting deployment process..."
docker-compose down
docker-compose pull
docker-compose up -d --build
echo "Deployment complete."