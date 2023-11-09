#!/bin/bash

echo "======================================"
echo "Temporary Files Cleanup Script by w01f"
echo "======================================"

if [ "$EUID" -ne 0 ]; then
  echo "Please run as root (sudo) for better results."
  exit
fi

echo -e "\nCurrent System Status:"
df -h

echo -e "\nCleaning /tmp directory..."
find /tmp -type f -atime +1 -exec rm -f {} \;
echo "Cleanup completed for /tmp directory."

echo -e "\nCleaning package manager cache..."
apt-get clean
yum clean all
echo "Package manager cache cleaned."

echo -e "\nUpdated System Status:"
df -h

echo -e "\nRAM Status:"
free -h

echo -e "\nRemaining Free Storage:"
df -h / | awk 'NR==2 {print $4}'

echo -e "\nCleanup process completed successfully."
