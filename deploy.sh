#!/bin/bash
set -e

APP_DIR="/home/ec2-user/todo-app"
REPO_URL="https://github.com/<your-username>/simple-python-code.git"

echo "🚀 Deploying To-Do App..."

# Clone repo or pull latest
if [ -d "$APP_DIR" ]; then
  cd $APP_DIR
  git pull origin main
else
  git clone $REPO_URL $APP_DIR
  cd $APP_DIR
fi

# Optional: run your CLI app
# python3 todo.py

echo "✅ Deployment completed!"
