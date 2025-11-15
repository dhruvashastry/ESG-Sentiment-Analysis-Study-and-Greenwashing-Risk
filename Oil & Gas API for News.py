import requests
import pandas as pd

api_key = "e04aaf15842c48348146c9bf76ba6be1"
companies = ["ExxonMobil", "Chevron", "ConocoPhillips", "Occidental Petroleum", 
             "Enbridge", "Indian Oil Corporation", "Saudi Aramco", "Southern Company", 
             "Shell", "Marathon Petroleum"]

news = []

for company in companies:
    url = f"https://newsapi.org/v2/everything?q={company}&language=en&sortBy=publishedAt&pageSize=100&apiKey={api_key}"
    response = requests.get(url).json()
    for article in response.get('articles', []):
        news.append({
            "company": company,
            "title": article['title'],
            "description": article['description'],
            "source": article['source']['name'],
            "url": article['url'],
            "publishedAt": article['publishedAt']
        })

df = pd.DataFrame(news)
df.to_csv("news_headlines.csv", index=False)
print(df.head())
