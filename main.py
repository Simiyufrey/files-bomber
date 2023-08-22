import requests
import sim

url="https://api.portal.kibu.ac.ke/api/login/user"

try:
    req=requests.get(url)
except Exception as e:
    print(e)