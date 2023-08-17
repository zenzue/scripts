#!/bin/bash

# SSH Connection Selector
# Author: w01f

echo "╭─────────────────────────────────────────────────────────╮"
echo "│                    SSH Connection Selector              │"
echo "│                       by w01f                           │"
echo "╰─────────────────────────────────────────────────────────╯"
echo

echo "Select a server to connect:"
echo "1. Connect to Core Server"
echo "2. Connect to Sprint Server"
echo "3. Connect to soon"

read -p "Enter the number of your choice: " choice

case $choice in
    1)
        ssh -i id_rsa user@core.server
        ;;
    2)
        ssh -i id_rsa root@core.server -p 2222
        ;;
    3)
        sshpass -p 'your_password_here' ssh root@core.server
        ;;
    *)
        echo "Invalid choice"
        ;;
esac
