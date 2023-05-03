import requests, json

url = "https://analisi.transparenciacatalunya.cat/resource/gn9e-3qhr.json"

file = requests.get(url)

print(file) # code
print(file.json()) # text