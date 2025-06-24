from bs4 import BeautifulSoup
import requests

Y_COMBINATOR_URL = "https://news.ycombinator.com/news"

# Get html code of a live website
response = requests.get(url=Y_COMBINATOR_URL)
contents = response.text

# Parse html code
soup = BeautifulSoup(contents, "html.parser")

news = []

# Get all news links and store them in a list
news_tags = soup.select(selector="tr.submission .title .titleline > a")
for news_tag in news_tags:
    news.append({
        "link": news_tag.get('href'),
        "title": news_tag.getText(),
        "score": 0
    })

# Get all html tags containing news details
details_tags = soup.select(selector="td.subtext")
for details_idx, details_tag in enumerate(details_tags):
    # Get score tag within the details tag
    score_tag = details_tag.select_one(selector=".subline span.score")
    score_value = 0
    # For some news, score does not exist and there is no score tag, so we need to check if tag exists
    if score_tag is not None:
        score_value = int(score_tag.getText().split()[0])
    news[details_idx]["score"] = score_value

# Sort a list of dictionaries (news) by an elm value (score) in DESC order
news = sorted(news, key=lambda sort_elm: sort_elm['score'], reverse=True)

for elm_idx, elm in enumerate(news):
    print(f"{elm_idx+1}. {elm['title']} (Score: {elm['score']})")

