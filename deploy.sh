#!/bin/bash
set -e

APP_DIR="/home/ec2-user/todo-app"

echo "🚀 Starting deployment of To-Do CLI app..."

# Ensure the app directory exists
mkdir -p $APP_DIR
cd $APP_DIR

# Optional: Run Python app (only if needed)
# python3 todo.py

echo "✅ Deployment completed!"
