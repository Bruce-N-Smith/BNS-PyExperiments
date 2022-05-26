#Thanks to Tomi Tokko @TomiTokko3 for the easy to follow tutorial on web scraping with Python!

#import the requests library functionality and give it a nickname bs to make it easier to use later
import requests
from bs4 import BeautifulSoup as bs

#assign new variable and this is the prompt for the user to enter the user name they want to retrieve
github_user = input('Input GitHub User Name: ')

#next up are some steps for getting web content, here is a concat of the last variable with a base url
url = 'https://github.com/'+github_user

#I think this is a variable that contains a method that sends a GET request to GitHub via the requests library functionality
r = requests.get(url)

#here's another variable I think, and what it does is use the BeautifulSoup functionality to make the request and display the HTTP content of the whole profile page, not just a code
soup = bs(r.content, 'html.parser')

#BeautifulSoup also has functionality to read through the html file for a tag, class, attribute, etc. So you can use a browser Dev tools to narrow down what image you want
profile_image = soup.find('img', {'alt' : 'Avatar'})['src']
print(profile_image)
