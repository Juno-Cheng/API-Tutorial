from todoist_api_python.api import TodoistAPI
import argparse
import math
import requests#Used for HTTP request
import os
import dotenv
import time

token = ""

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json",
}

response = requests.get("https://api.todoist.com/rest/v2/projects", headers=headers)

if response.status_code == 200:
    projects = response.json()
    for project in projects:
        print(f"Name: {project['name']}")
        print(f"ID: {project['id']}")
else:
    print(f"Error fetching projects: {response.text}")