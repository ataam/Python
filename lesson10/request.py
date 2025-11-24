import requests

#windows_active = '.\venv\Scripts\activate'
site = "https://jsonplaceholder.typicode.com/posts"

try:
    responce_get = requests.get(site, timeout = 0.1 )
    responce_get.raise_for_status()
    print(responce_get.status_code)
    headerText = ''
    for header, value in responce_get.headers.items():
        headerText += f"\nHeader: {header}\nValue: {value}\n_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-"

except requests.exceptions.Timeout:
    print("errorTimeout")

except requests.exceptions.RequestException as reqEx:
    print(f"Помилкf {reqEx}")

open('page.txt', 'w', encoding='utf-8').write(headerText)
print("file created")









#print('_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-')



#body = {
 #   "userId" : 41,
#    "header": "test"
#}

#header = {'Judy':"123121"}

#responce_post = requests.post(site, data=body, headers=header)

#print('_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-')
#print(responce_post.status_code)
#print(responce_post.reason)
#print(responce_post.text)
#print('_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-')

