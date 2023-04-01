import docker
import requests
import json
import time

# Create a Docker client instance
client = docker.from_env()

# Get the container ID or name
container_name_or_id = 'container'

# Set up the Discord webhook URL
webhook_url = ''

# Initialize the previous log message variable to an empty string
previous_log_message = ''

while True:
    # Retrieve the logs from the container
    logs = client.containers.get(container_name_or_id).logs()

    # Decode the logs to a string
    logs_str = logs.decode('utf-8')

    # Check if the last log message contains a GET request and
    # if it matches the previous log message
    last_log_message = logs_str.strip().split('\n')[-1]
    if 'GET' in last_log_message and last_log_message != previous_log_message:
        # Update the previous log message to the last log message
        previous_log_message = last_log_message

        # Create a dictionary with the message data
        message = {
            'content': last_log_message
        }

        # Send the message to the Discord webhook
        response = requests.post(webhook_url, data=json.dumps(message), headers={'Content-Type': 'application/json'})

        # Print the response status code to the console
        print(response.status_code)

    # Wait for 5 seconds before checking for new logs
    time.sleep(2)



