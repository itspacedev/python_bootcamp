import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

news_params = {
    "apiKey": "**********",
    "q": COMPANY_NAME,
    "searchIn": "title"
}
response = requests.get(url=NEWS_ENDPOINT, params=news_params)
articles = response.json()["articles"]
first_three_articles = articles[:3]

formatted_articles = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in first_three_articles]

print(formatted_articles)



