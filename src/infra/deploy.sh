# src/infra/deploy.sh
#!/bin/bash

# Pull the latest changes from the repository
git pull origin main

# Build and start the containers
docker-compose -f src/infra/docker-compose.yml up -d --build

echo "Deployment complete. Application is now running."
