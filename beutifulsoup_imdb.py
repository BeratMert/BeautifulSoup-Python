from bs4 import BeautifulSoup
import requests

url = "https://www.imdb.com/chart/top/"

informations = open("movies.csv", "w")
informations.write("movieNumber, movieName, date, rating\n")

r = requests.get(url)
soup = BeautifulSoup(r.content, "lxml")
rows = soup.find_all("tr")

print("*"*20)
print("* Top Rated Movies *")
print("*"*20)

for row in rows:
    titles = row.find_all("td", {"class":"titleColumn"})

    for title in titles:
        name = title.a.text
        movieNumber = title.next.strip()
        date = title.span.text
        rating = row.strong.text
        
        print(f"{movieNumber}{name} {date}\nIMDB Rating; {rating}")
        informations.write(movieNumber + "," + name + "," + date + "," + rating + "\n")

    print("-"*50)

informations.close()