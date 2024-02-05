#!/bin/bash
echo "artemchik16" | sudo -S systemctl restart gunicorn
python manage.py dumpdata > data.json
