import requests
import datetime as dt

PIXELA_PROFILE = "https://pixe.la/**********"
PIXELA_URL = "https://pixe.la"
PIXELA_TOKEN = "**********"
PIXELA_USERNAME = "**********"

# 1. Create a user account
# create_user_params = {
#     "token": PIXELA_TOKEN,
#     "username": PIXELA_USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }
# response = requests.post(url=f"{PIXELA_URL}/v1/users", json=create_user_params)
# print(response.text)

# 2. Create a graph
# request_headers = {
#     "X-USER-TOKEN": PIXELA_TOKEN
# }
# create_graph_params = {
#     "id": "coffee-meter",
#     "name": "Coffee Consumption Graph",
#     "unit": "cup",
#     "type": "int",
#     "color": "ajisai"
# }
# response = requests.post(
#     url=f"{PIXELA_URL}/v1/users/{PIXELA_USERNAME}/graphs",
#     json=create_graph_params,
#     headers=request_headers
# )
# print(response.text)

# 3. Posting a pixel to a graph
# today = dt.datetime.now()
# today_yyyyMMdd = today.strftime("%Y%m%d")
#
# pixel_headers = {
#     "X-USER-TOKEN": PIXELA_TOKEN,
# }
# pixel_params = {
#     "date": today_yyyyMMdd,
#     "quantity": "4"
# }
# response = requests.post(
#     url=f"{PIXELA_URL}/v1/users/{PIXELA_USERNAME}/graphs/coffee-meter",
#     json=pixel_params,
#     headers=pixel_headers
# )
# print(response.text)

# 4. Update a pixel
# today = dt.datetime.now()
# today_yyyyMMdd = today.strftime("%Y%m%d")
#
# pixel_headers = {
#     "X-USER-TOKEN": PIXELA_TOKEN,
# }
# pixel_params = {
#     "quantity": "10"
# }
# response = requests.put(
#     url=f"{PIXELA_URL}/v1/users/{PIXELA_USERNAME}/graphs/coffee-meter/{today_yyyyMMdd}",
#     json=pixel_params,
#     headers=pixel_headers
# )
# print(response.text)

# 5. Delete a pixel
today = dt.datetime.now()
today_yyyyMMdd = today.strftime("%Y%m%d")

pixel_headers = {
    "X-USER-TOKEN": PIXELA_TOKEN,
}
response = requests.delete(
    url=f"{PIXELA_URL}/v1/users/{PIXELA_USERNAME}/graphs/coffee-meter/{today_yyyyMMdd}",
    headers=pixel_headers
)
print(response.text)
