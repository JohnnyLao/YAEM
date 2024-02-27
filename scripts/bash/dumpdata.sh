#!/bin/bash

mkdir other/fixtures

current_date=$(date +"%Y-%m-%d")
fixture_path="fixture_${current_date}.json"
log_path="scripts/bash/logs.txt"

green='\033[0;32m'
reset='\033[0m'

echo -e "${green}Starting dumpdata script...${reset}"
if python manage.py dumpdata > "other/fixtures/${fixture_path}" 2>&1 | tee -a; then
   echo "${current_date} - dumpdata script has been executed successfully" >> "${log_path}"
   echo -e "${green}dumpdata script has been executed successfully.${reset}"
fi
