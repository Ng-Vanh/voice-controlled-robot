#!/usr/bin/env bash
set -e

echo "=== Đang thêm Cyberbotics APT Repository và cài đặt Webots ==="

# 1. Thêm keyring
sudo mkdir -p /etc/apt/keyrings
wget -qO- https://cyberbotics.com/Cyberbotics.asc | sudo gpg --dearmor --yes -o /etc/apt/keyrings/Cyberbotics.gpg

# 2. Thêm APT source list
echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/Cyberbotics.gpg] https://cyberbotics.com/debian binary-amd64/" | sudo tee /etc/apt/sources.list.d/Cyberbotics.list

# 3. Cập nhật và cài đặt webots
sudo apt update
sudo apt install -y webots

echo "=== Cài đặt Webots hoàn tất! Bạn có thể khởi động bằng lệnh 'webots' ==="
