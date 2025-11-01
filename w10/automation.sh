#!/bin/bash
echo "Building Docker image..."
docker build -t mynginx:latest .

echo "Creating kind cluster..."
kind create cluster --name mycluster

echo "Deploying app..."
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml

echo "Cluster info:"
kubectl get pods
kubectl get svc

echo "Access app at localhost:8080 using port-forward"
kubectl port-forward service/myapp-service 8080:80
chmod +x automation.sh
./automation.sh
