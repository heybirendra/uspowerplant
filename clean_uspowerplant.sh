#!/bin/bash

echo "Stopping and removing all containers, networks, and volumes..."

# Stop and remove everything from docker-compose including volumes
docker compose down -v --remove-orphans

# Optional: Force remove images (if needed)
docker image prune -a -f

# Optional: Clean specific named volumes if still hanging around
docker volume rm uspowerplant_pgdata 2>/dev/null

# Optional: Clean unused volumes system-wide
docker volume prune -f

# Optional: Clean unused networks
docker network prune -f

echo "✅ All Docker artifacts for USPowerPlant cleaned up."

sh clean_test.sh
