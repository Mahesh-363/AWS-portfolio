#!/bin/bash

# ----------------- Server Setup Script -----------------
echo "Starting Linux Server Management Script..."

# 1. Update system
echo "Updating system packages..."
sudo apt update -y && sudo apt upgrade -y

# 2. Install common packages
echo "Installing git, vim, htop..."
sudo apt install -y git vim htop curl wget

# 3. Create a test user
USER_NAME="testuser"
if id "$USER_NAME" &>/dev/null; then
    echo "User $USER_NAME already exists."
else
    sudo adduser --disabled-password --gecos "" $USER_NAME
    echo "User $USER_NAME created."
fi

# 4. Check running services
echo "Checking services..."
sudo systemctl status ssh || echo "SSH service not found."

# 5. Monitor CPU and Memory usage
echo "Top 5 processes by CPU usage:"
ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%cpu | head -n 6

echo "Top 5 processes by Memory usage:"
ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%mem | head -n 6

echo "Linux Server Management Script Completed."

