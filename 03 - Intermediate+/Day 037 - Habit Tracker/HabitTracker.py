# 100 Days of Code: Python
# May 27, 2022
# Keep track of habits with Pixela
# Practicing using POST

'''
My Pixela dashboard link
https://pixe.la/@gdbecker

First graph I made
https://pixe.la/v1/users/gdbecker/graphs/graph1.html
'''

# Import modules
import requests
from datetime import datetime
from decouple import config

USERNAME = config("USERNAME")
TOKEN = config("TOKEN")
GRAPH_ID = config("GRAPH_ID")

# Step 1: make user profile -> username/token
pixela_endpoint = "https://pixe.la/v1/users"
user_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# Create user step! all done
# response = requests.post(url=pixela_endpoint, json=user_parameters)
# print(response.text)

# Step 2: make a graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "ReadingGraph",
    "unit": "minutes",
    "type": "int",
    "color": "sora"
}
headers = {
    "X-USER-TOKEN": TOKEN
}
response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

# Step 3: post a pixel to the graph
# Get today's date info
today = datetime.now()

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "60"
}
response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)

# Step 4: edit a pixel
date_to_edit = today.strftime("%Y%m%d")
edit_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date_to_edit}"
edit_config = {
    "quantity": "100"
}
response = requests.put(url=edit_endpoint, json=edit_config, headers=headers)
print(response.text)

# Heads up
print("Go to https://pixe.la/v1/users/gdbecker/graphs/graph1.html to see the result!")