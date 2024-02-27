#!/bin/bash

green='\033[0;32m'
red='\033[0;31m'
reset='\033[0m'

current_date=$(date +"%Y-%m-%d")
fixture_path="fixtures_${current_date}.json"

echo -e "${green}Starting loaddata script...${reset}"

echo -e "${red}Deleting ContentType objects...${reset}"
echo "from django.contrib.contenttypes.models import ContentType; ContentType.objects.all().delete()" | python manage.py shell
echo -e "${red}ContentType has been deleted...${reset}"

if python manage.py loaddata "other/fixtures/${fixture_path}" 2>&1 | tee -a; then
   echo -e "${green}loaddata script has been executed successfully.${reset}"
fi
