import requests
import datetime
import os

pixela_endpoint = "https://pixe.la/v1/users"
token = os.environ.get('TOKEN')
username = os.environ.get('USERNAME')

user_params = {
    "token": token,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{username}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": token
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# post a pixel

pixel_creation_endpoint = f"{graph_endpoint}/graph1"

today_date = str(datetime.date.today())
usable_date = today_date.replace("-", "")

posting_pixel_params = {
    "date": usable_date,
    "quantity": "19"
}

# post_response = requests.post(url=pixel_creation_endpoint, json=posting_pixel_params, headers=headers)
# print(post_response.text)

# update a pixel

put_pixela_endpoint = f"{pixel_creation_endpoint}/{usable_date}"

pixel_updating_params = {
    "quantity": "35"
}

put_response = requests.put(url=put_pixela_endpoint, json=pixel_updating_params, headers=headers)
print(put_response.text)
