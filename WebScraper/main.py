import requests
from bs4 import BeautifulSoup

# Replace 'url' with the actual URL of the page you want to scrape
url = 'http://127.0.0.1:3000/home/idris/Downloads/test.html'
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.text, 'html.parser')

# Find all links on the page
svgs = soup.find_all('svg')

# Print the href attribute of each link
i =0
for svg in svgs:
  i += 1
  with open(f'frame{i}.svg', 'w') as file:
    file.write(str(svg))
    file.close()