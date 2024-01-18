from bs4 import BeautifulSoup
import requests

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
empire_web_page = response.text

soup = BeautifulSoup(empire_web_page, "html.parser")

movies = soup.find_all(name="h3", class_="title")
movies.reverse()

with open("movies.txt", mode="w") as data:
    for movie in movies:
        text = movie.getText()
        data.write(f"{text}\n")



