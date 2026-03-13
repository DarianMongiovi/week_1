#!/bin/bash

# Navigate to the project folder
cd /home/darmongiovi/Desktop/cmcc_calendar_fetcher

# Activate the virtual environment
source venv/bin/activate

# Execute the Python script and log the output
echo "--- Run Started: $(date) ---" >> cron_log.txt
python3 postgre_populate.py >> cron_log.txt 2>&1
echo "--- Run Finished: $(date) ---" >> cron_log.txt

# Exit the virtual environment
deactivate
