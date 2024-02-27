#!/bin/bash
echo "artemchik16" | sudo -S systemctl restart gunicorn
echo "artemchik16" | sudo -S systemctl restart postgresql
echo "artemchik16" | sudo -S systemctl restart nginx
