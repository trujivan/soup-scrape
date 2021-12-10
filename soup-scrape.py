from bs4 import BeautifulSoup
import requests
#Target web page

wikiSearch = "Genghis_Khan"
url = "https://en.wikipedia.org/wiki/" + wikiSearch

#Connection to web page
response = requests.get(url)
print(response.status_code)

# Convert the response HTLM string into a python string
html = response.text

soup = BeautifulSoup(html, 'lxml')

#List to store results
textContent = []

#Get all headers from the latest section of the web site
for i in range(0, 10):
    the_latest = soup.find_all("h3")[i].text
    textContent.append(the_latest)

print(textContent)
#pd.DataFrame(textContent)