import os
from dotenv import load_dotenv, find_dotenv
import requests
import datetime


dotenv_path = find_dotenv()
load_dotenv(dotenv_path)


NEWS_API_KEY = os.getenv("NEWS_API_KEY")
NEWS_SOURCES = 'bbc-news, reuters, associated-press, al-jazeera-english, the-guardian-uk, bloomberg, cnn, abc-news, independent, the-wall-street-journal, business-insider, wired, the-next-web, the-verge, bbc-sport, bleacher-report, time, cbc-news, the-washington-post'



url = "https://newsapi.org/v2/top-headlines/"

params = {
    'apiKey': NEWS_API_KEY,
    'language':'en',
    'sortBy' : 'publishedAt',
    'sources' : NEWS_SOURCES,
    'pageSzie' : 10,

}

response = requests.get(url, params = params)

data = response.json()
articles = data['articles']

articles.sort(key = lambda x: x['publishedAt'], reverse = True) # sort to get newest news first

top_10 = articles[:10] #get the top 10 articles

for article in top_10:
    print(article['title'])
    print(article['publishedAt'])
    print(article['url'])
    print()


def build_email(articles):
    date = datetime.datetime.now()
    formatted_date = date.strftime("%x")

    subject = "Newsletter " +formatted_date
    header = "<h1>TOP NEWS</h1>"

    print(subject)

build_email(articles)


