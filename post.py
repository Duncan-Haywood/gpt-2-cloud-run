# Makes a request to test the app.py file when running locally
import requests

req = requests.post('http://0.0.0.0:8080',
                    json={'length': 100, 'temperature': 1.0})
text = req.json()['text']
print(text)

