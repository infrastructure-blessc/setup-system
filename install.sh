#!/bin/bash

set -e

echo "[+][Install.sh] 🔍 Checking for pip..."
if ! command -v pip &> /dev/null; then
    echo "📦 Installing pip..."
    apt update && apt install -y python3-pip
fi

echo "[+][Install.sh] 📥 Installing dependencies..."
pip install --break-system-packages -r requirements.txt

echo "[+][Install.sh] 🚀 Running main script..."
sudo python3 main.py

echo "[+][Install.sh] 🗑 Removing project directory..."
CURRENT_DIR="$(pwd)"
cd ..
sudo rm -rf "$CURRENT_DIR"

echo "[+][Install.sh] 🔁 Rebooting system now..."
reboot
