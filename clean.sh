#!/bin/bash
# Author: w01f
GREEN="\e[32m"
YELLOW="\e[33m"
RED="\e[31m"
CYAN="\e[36m"
RESET="\e[0m"

clean_directory() {
    dir_to_clean="$1"
    echo -e "${CYAN}Cleaning $dir_to_clean...${RESET}"
    cleaned_size=$(sudo find "$dir_to_clean" -type f -atime +7 -print -exec rm -f {} + | du -ch | grep total$ | cut -f1)
    echo -e "${GREEN}Cleaned files size:${RESET} $cleaned_size"
}

system_status() {
    echo -e "\n${CYAN}System Status:${RESET}"
    echo -e "-----------------"
    echo -e "${YELLOW}Remaining free storage:${RESET}"
    df -h / | awk 'NR==2{printf "Total: %s Used: %s Free: %s\n", $2, $3, $4}'
    echo -e "${CYAN}RAM Status:${RESET}"
    free -h
}

echo -e "${RED}============================================${RESET}"
echo -e "${RED}| Linux Temporary and Cache Cleaning Script |${RESET}"
echo -e "${RED}==================w01f======================${RESET}"

echo -e "${CYAN}Cleaning Linux Temporary and Cache Directories${RESET}"

clean_directory "/tmp"

clean_directory "/var/cache"

system_status
