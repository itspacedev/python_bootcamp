from bs4 import BeautifulSoup
import requests

TOP_MOVIES_URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Get html from Top Movies website
response = requests.get(url=TOP_MOVIES_URL)
contents = response.text

# Parse html
soup = BeautifulSoup(contents, "html.parser")

movies = []
# Get all movies blocks tags
movies_tags = soup.select("section.gallery__content-item")
for movie_tag in movies_tags:
    title_tag = movie_tag.select_one(selector=".article-title-description__text h3.title")
    title_text = title_tag.getText().split()  # Format of the text is as follows "100) Stand By Me"

    # Get movie position in the rating
    movie_position = title_text[0].replace(")", "").replace(":", "")
    movie_position = int(movie_position)
    # Get movie title
    movie_title = " ".join(title_text[1:])

    movies.append({
        "title": movie_title,
        "position": movie_position
    })

# Sort movies by the movie position in ASC order
movies = sorted(movies, key=lambda m: m['position'])

print("----- Top 100 Movies to watch -----")
for movie_idx, movie in enumerate(movies):
    print(f"{movie_idx+1}. {movie['title']}")
