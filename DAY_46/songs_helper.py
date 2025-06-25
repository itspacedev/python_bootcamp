import requests
from bs4 import BeautifulSoup

BILLBOARD_URL = "https://www.billboard.com/charts/hot-100"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"


def top_songs_by_date(date_in_the_past: str):
    """
    Returns Top 100 songs for a specified date (YYYY-MM-DD)
    """
    # Get html with Top 100 songs for a specific date
    response = requests.get(
        url=f"{BILLBOARD_URL}/{date_in_the_past}",
        headers={
            "User-Agent": USER_AGENT
        }
    )
    contents = response.text

    # Parse html
    soup = BeautifulSoup(contents, "html.parser")
    songs = []
    songs_tags = soup.select(selector="div.chart-results-list div.o-chart-results-list-row-container")
    for song_tag in songs_tags:
        title = song_tag.select_one(selector="li.lrv-u-width-100p li.o-chart-results-list__item h3.c-title").getText().strip()
        artist = song_tag.select_one(selector="li.lrv-u-width-100p li.o-chart-results-list__item span.c-label").getText().strip()
        songs.append({
            "artist": artist,
            "title": title
        })

    return songs
