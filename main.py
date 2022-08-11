import requests
from bs4 import BeautifulSoup

my_url = "https://sponsor.hackernoon.com/billboard"

response = requests.get(url=my_url)
data = response.text

soup = BeautifulSoup(data, "html.parser")
my_title = soup.find(name="h1")
my_paragraph = soup.find(name="p")
my_content = soup.find(name="div")
print(my_title.getText())
print(my_paragraph.getText())
print(my_content.getText())