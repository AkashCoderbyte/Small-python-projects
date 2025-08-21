import requests

query = input("Enter the topic which you like to search : ")

api_key ="5a99d6b7e1cb4522aec93df1be96f599"

url = f"https://newsapi.org/v2/everything?q={query}&from=2025-07-18&sortBy=publishedAt&apiKey={api_key}"
 
response = requests.get(url)
data = response.json()

articles = data['articles']
for article in articles:
    print("Title:", article['title'])
    print("Link:", article['url'])
    print("*******************************")




