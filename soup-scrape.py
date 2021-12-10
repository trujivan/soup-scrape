from bs4 import BeautifulSoup
import requests
import sys


countryUrl = "https://history.state.gov/countries/all"

countryResponse = requests.get(countryUrl)

if countryResponse.status_code != 200:
    sys.exit()

countrySoup = BeautifulSoup(countryResponse.text, 'lxml')
soup = BeautifulSoup(countryResponse.text, 'lxml')

textContent = []

for i in range(0, 200):
    country = countrySoup.find_all("li")[i].text
    url = "https://en.wikipedia.org/wiki/" + country
    response = requests.get(url)
    
    soup = BeautifulSoup(response.text, 'lxml')
    for i in range(0, 10):
        the_latest = soup.find_all("h3")[i].text
        print(the_latest)



