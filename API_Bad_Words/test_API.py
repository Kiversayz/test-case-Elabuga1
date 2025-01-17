import requests
import json
from APIKay import kay

url = "https://api.apilayer.com/bad_words?censor_character=%"

payload = "popit porno huy pidor fuck".encode("utf-8")
headers= {
    "apikey": kay
}

response = requests.request("POST", url, headers=headers, data = payload)

status_code = response.status_code
resultJson = response.text
resultText = response.json()

print(resultJson)

print()

print(resultText['content'])
print(resultText['censored_content'])