from dotenv import load_dotenv
import os
from newsapi import NewsApiClient
from datetime import datetime, timedelta
from textblob import TextBlob
import matplotlib.pyplot as plt
from sys import exit

load_dotenv('news.env')
api_key = os.environ.get('API_API_KEY')

newsapi = NewsApiClient(api_key=api_key)

# Parameters 
print()
key_word = input("Please enter an input: ")
start_date = datetime.now().strftime('%Y-%m-%d')
end_date = (datetime.now() - timedelta(days=14)).strftime('%Y-%m-%d') 

# Retrieve news articles
articles = newsapi.get_everything(q=key_word,
                          from_param=start_date,
                          to=end_date,
                          language='en')
sentiment_sum_per_day = {}
sentiment_count_per_day = {}

for article in articles['articles']:
    sentiment = TextBlob(article['title']).sentiment.polarity
    published_at = datetime.strptime(article['publishedAt'], '%Y-%m-%dT%H:%M:%SZ')
    day = published_at.strftime('%Y-%m-%d')
    sentiment_sum_per_day[day] = sentiment_sum_per_day.get(day, 0) + sentiment
    sentiment_count_per_day[day] = sentiment_count_per_day.get(day, 0) + 1

average_sentiment_per_day = {day: sentiment_sum_per_day[day] / sentiment_count_per_day[day] 
                              for day in sentiment_sum_per_day}

sorted_dates = sorted(average_sentiment_per_day.keys())
average_sentiments = [average_sentiment_per_day[date] for date in sorted_dates]


plt.plot(sorted_dates, average_sentiments)
plt.xlabel('Date')
plt.ylabel('Average Sentiment Polarity')
plt.title(f'Average Sentiment Polarity Over Time for "{key_word}"')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(f'{key_word}_sentiment_graph.png')
plt.show(block=False)  
plt.close()
print("Graph Generated")
