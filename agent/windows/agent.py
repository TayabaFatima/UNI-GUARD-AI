import requests

def send_to_server(link):
    url = "http://127.0.0.1:5001/scan"
    response = requests.post(url, json={"link": link})
    print(response.json())

if __name__ == "__main__":
    link = input("Enter link: ")
    send_to_server(link)
