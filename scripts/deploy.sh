echo "Starting deployment..."

echo "Pulling latest images..."
docker pull yourname/uptime-backend:latest
docker pull yourname/uptime-frontend:latest

echo "Stopping old containers..."
echo "docker stop backend frontend"

echo "Starting new containers..."
echo "docker run -d -p 8000:8000 yourname/uptime-backend:latest"
echo "docker run -d -p 80:80 yourname/uptime-frontend:latest"

echo "Deployment complete."