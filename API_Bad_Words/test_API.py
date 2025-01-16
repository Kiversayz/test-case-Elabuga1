import requests
import json

url = "https://api.apilayer.com/bad_words?censor_character=%"

payload = "popit porno huy pidor fuck".encode("utf-8")
headers= {
    "apikey": "apwq3h9FYmzTozaEzfvZhDm3on11qd4Z"
}

response = requests.request("POST", url, headers=headers, data = payload)

status_code = response.status_code
resultJson = response.text
resultText = response.json()

print(resultJson)

print()

print(resultText['content'])
print(resultText['censored_content'])