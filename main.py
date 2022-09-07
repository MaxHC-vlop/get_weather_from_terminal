import requests


# url = 'https://wttr.in/London'
# url = 'https://wttr.in/Череповец'
url = 'https://wttr.in/svo'
response = requests.get(url)
response.raise_for_status()
print(response.text)