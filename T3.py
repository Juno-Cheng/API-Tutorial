from todoist_api_python.api import TodoistAPI
import argparse
import math
import requests#Used for HTTP request
import os
import dotenv
import time
#=================================================
url_bearer = "https://api.todoist.com/rest/v2/projects"
url_tasks = "https://api.todoist.com/rest/v2/tasks"
bearer = "Bearer "

dotenv.load_dotenv()
id = os.getenv("API_BEARER_KEY_TODOIST")
headerBearer = bearer + id
headerContent = "application/json"
#=================================================

#Add functions
def check_projects():
    #Variables
    url = url_bearer
    header = {'Authorization': headerBearer}
    #Get response
    response = requests.get(url, headers=header)
    if response.status_code != 200:
        print("Something went wrong...\n")
        exit()

    for project in response.json():
        print(f"Project: {project['name']} | ID: {project['id']}\n")

def check_tasks(id): #https://developer.todoist.com/rest/v1/?shell#get-active-tasks
    url = url_tasks
    header = {'Authorization':headerBearer, 'project_id':id}
    
    #Get response
    response = requests.get(url, headers=header)
    if response.status_code != 200:
        print("Something went wrong...\n")
        exit()

    for tasks in response.json():
         if tasks['project_id'] == id:
            print(f"Task: {tasks['content']} | ID: {tasks['id']}\n")

def add_tasks(project_id, task_name):
    url = url_tasks
    header = {'Authorization':headerBearer}
    data = {'content': task_name, 'project_id': project_id}
    response = requests.post(url, headers=header, json= data)#Since json automatically turns content type, we don't need to specify it in header
    if response.status_code != 200:
        print("Uh Oh\n")
        exit()
    print(f"Added Task ({task_name}) to Project {project_id}\n")

def del_tasks(taskid):
    url = url_tasks
    header = {'Authorization':headerBearer}
    url = url + f"/{taskid}"
    print(url)
    response = requests.delete(url, headers=header)
    print(response.status_code)
    if response.status_code != 204:
        print("Uh Oh\n")
        exit()
    print(f"Deleted Task\n")
#=================================================

while True:
#Print Options:
    print("Welcome to Your ToDoList App - Uses an API to store data - Choose a Number\n")
    print("1. Check All Projects\n")
    print("2. Check Tasks in Projects - Input ID\n")
    print("3. Add a Task to Current Project\n")
    print("4. Delete a Task\n")
    print("5. Exit\n")
    command = input().strip()

    if (command == "1"):
        print("============================")
        check_projects()

    elif (command == "2"):
        print("============================")
        print("Enter Project ID\n")
        check_projects()
        print("====")
        id = input()
        print("====")
        check_tasks(id)
        
    elif (command == "3"):
        print("============================")
        print("Enter Project ID\n")
        check_projects()
        print("====")
        id = input()
        print("====")
        print("Enter task name\n")
        name = input()
        add_tasks(id,name)


    elif (command == "4"):
        print("====")
        id = input()
        print("====")
        del_tasks(id)

    elif (command == "5"):
        exit()

    time.sleep(1)
    print("============================")
    print("Enter 6 to see Option Again:")
    while True:
        command = input().strip()
        if command == "6":
            break


    
