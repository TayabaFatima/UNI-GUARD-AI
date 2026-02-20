import requests

link = input("Enter link: ")
device_name = "Windows-PC"

data = {"device": device_name, "link": link}
response = requests.post("http://YOUR_SERVER_IP:3000/api/data", json=data)
print(response.json())
