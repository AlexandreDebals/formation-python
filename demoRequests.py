import requests as req

response = req.get("https://pypi.org/project/requests/")

# print(type(response)) # object de la classe Response
body = str(response.content)

with open("response.html", "w") as f:
  f.write(body)
  
print("Page téléchargée")