# cs361
A. To receive data from my microservice, a POST request can be sent to the endpoint '/validate_email'. 
If you are doing this in Python, you can use the requests library, and below is an example:

import requests

url = "http://127.0.0.1:5000/validate_email"
payload = {'email': 'test@example.com'}
response = requests.post(url, json=payload)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Error:", response.text)

B. The microservice returns a JSON response containing data 
indicating whether the email address is valid or not. The above code would send a request, 
receive the response, and print it. 

C. Image in discussion post (not sure how to add images on the readme file). 

