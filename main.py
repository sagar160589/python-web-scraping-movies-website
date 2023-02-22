from bs4 import BeautifulSoup
import requests, html

movie_response = requests.get('https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/')
movie_doc = movie_response.text

soup = BeautifulSoup(movie_doc, 'html.parser')
movie_titles = soup.findAll(name='h3', class_='title')
movie_titles_text = [movie.get_text() for movie in movie_titles]
for movie in reversed(movie_titles_text):
    with open("my_files.txt", mode='a', encoding="utf-8") as data:
        data.write(f"{movie}\n")


