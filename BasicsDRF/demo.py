#accessing the api using requests in another file or app

import requests
URL="http://127.0.0.1:8000/stulist/"
response=requests.get(URL)
data=response.json()
print(data)
