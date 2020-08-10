

import requests
import json

url = "https://contact.plaid.com/jobs"

data = {
  "name": "Brandon Patterson",
  "email": "pattersonbl2@vcu.edu",
  "resume": "https://bit.ly/2PGdhhn",
  "phone": "804-399-4165",
  "twitter": "@bpdev2",
  "location": "baltimore,MD",
  "favorite_candy": "sour patch",
  "superpower": "persistent"

}
data = json.dumps(data)
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
http_post_request = requests.post(url=url, data=data, headers=headers)
server_response = http_post_request.text
print(server_response)
