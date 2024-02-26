#!/bin/bash

cd .. && cd ..

green='\033[0;32m'
red='\033[0;31m'
reset='\033[0m'

echo -e "${green}Available fixtures:${reset}"
ls other/fixtures

echo "-------"
echo "Enter the name of the fixture you want to load:"
read fixture_name

if [ -z "$fixture_name" ]; then
    echo "Usage: $0 <fixture_file_path>"
    exit 1
fi

echo -e "${green}Starting loaddata script...${reset}"

echo -e "${red}Deleting ContentType objects...${reset}"
echo "from django.contrib.contenttypes.models import ContentType; ContentType.objects.all().delete()" | python manage.py shell
echo -e "${red}ContentType has been deleted...${reset}"

if python manage.py loaddata "other/fixtures/$fixture_name" 2>&1 | tee -a; then
   echo -e "${green}loaddata script has been executed successfully.${reset}"
fi
