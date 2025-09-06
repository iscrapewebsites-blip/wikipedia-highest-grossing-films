import requests

url = 'https://en.wikipedia.org/wiki/List_of_highest-grossing_films'
headers = {'User-Agent':'Mozilla/5.0'}

response = requests.get(url, headers=headers)

with open('data.html', 'w', encoding='utf-8') as  f:
     f.write(response.text)



