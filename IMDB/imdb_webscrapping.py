#https://bit.ly/2NyxdAG
from bs4 import BeautifulSoup
import requests
import re
import csv

# Url to get the top 250 movies
url = 'http://www.imdb.com/chart/top'
response = requests.get(url) 
soup = BeautifulSoup(response.text, 'lxml')
movies = soup.select('td.titleColumn') # Getting the table data of the table of the html source
links = [a.attrs.get('href') for a in soup.select('td.titleColumn a')] #Extracting the href of the individual movies
images = [a.attrs.get('src') for a in soup.select('td.posterColumn a img')]
crew = [a.attrs.get('title') for a in soup.select('td.titleColumn a')] #Extracting the crew of the individual movies

title = [b.attrs.get('title') for b in soup.select('td.ratingColumn strong')] #Extracting the ratings and vote string
ratings = []
votes = []
for i in title:
    ratings.append(i.split()[0]) #Extracting rating from title string
    votes.append(i.split()[3])   #Extracting votes from title string

imdb = []

# Store each item into dictionary (data), then put those into a list (imdb)
for index in range(0, len(movies)):
    # Seperate movie into: 'place', 'title', 'year'
    movie_string = movies[index].get_text()
    movie = (' '.join(movie_string.split()).replace('.', ''))
    movie_title = movie[len(str(index))+1:-7]       #Getting the movie title
    year = re.search('\((.*?)\)', movie_string).group(1) #Getting the year of movie
    place = movie[:len(str(index))-(len(movie))] #Getting the sequence of movie

    data = {"place": place,
            "movie_title": movie_title,
            "year": year,
            "star_cast": crew[index],
            "rating": ratings[index],
            "vote": votes[index],
            "link": links[index],
            "images":images[index]}
    imdb.append(data)
csv_columns = ['place','movie_title','year','star_cast','rating','vote','link','images']
csv_file = "movie_data.csv"
try:
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in imdb:
            writer.writerow(data)
except IOError:
    print("I/O error")
