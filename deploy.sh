#!/bin/bash
set -e

APP_DIR="/home/ec2-user/todo-app"
REPO_URL="https://github.com/Bhavesh8890/simple-python-code.git"

echo "🚀 Starting deployment of To-Do CLI app..."

# Pull or clone the latest code
if [ -d "$APP_DIR" ]; then
  echo "📁 Directory exists. Pulling latest changes..."
  cd "$APP_DIR"
  git pull origin main
else
  echo "📁 Directory doesn't exist. Cloning repository..."
  git clone "$REPO_URL" "$APP_DIR"
  cd "$APP_DIR"
fi

# Set permissions (optional, good practice)
chmod +x deploy.sh

# Optionally run the app
# echo "🎯 Launching the CLI app..."
# python3 todo.py

echo "✅ Deployment successful!"
