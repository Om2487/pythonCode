import requests
response=requests.get('/Library/GetBook.php'),params={'ID':''}
print(response.text)