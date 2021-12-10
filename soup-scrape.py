from bs4 import BeautifulSoup
import requests
import pandas as pd
#Target web page
url = "https://projects.fivethirtyeight.com/trump-approval-ratings/"

#Connection to web page
response = requests.get(url)
print(response.status_code)

# Convert the response HTLM string into a python string
html = response.text

soup = BeautifulSoup(response.content, 'lxml')

#List to store results
textContent = []

#Get all headers from the latest section of the web site
for i in range(0, 4):
    the_latest = soup.find_all("h3")[i].text
    textContent.append(the_latest)

print(textContent)
pd.DataFrame(textContent)