import requests, json

url = "https://analisi.transparenciacatalunya.cat/resource/gn9e-3qhr.json"

text = requests.get(url)

print(text) # <Response [200]>
print(text.json()) # list of dictionaries