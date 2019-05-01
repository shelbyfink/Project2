import requests, re, bs4
from dateutil import parser
import wordninja

# Get url from the user
url = input('Enter the online article url here: ')

resp = requests.get(url)
html_text = resp.text
soup = bs4.BeautifulSoup(html_text, features="html.parser")

# Find the author's name

tag = soup.find_all("a", class_="author-name")
author_name = tag[0].getText()

# Separate the author's last name from their first name

author_name = author_name.split()
first_name, last_name = author_name[0], author_name[1]
first_initial = first_name[0][0]

# Find the date published

tag = soup.find("span", class_="author-timestamp")
date_pub = tag["content"]
date_pub = date_pub[:10]
date_pub = parser.parse(date_pub)
date_pub = date_pub.year

# Get the article title

title_tag = soup.find_all("h1")
title = title_tag[0].getText()

# Get the website name/title from the url

regex = re.compile(r'www.\w*')
page_title = regex.findall(url)
page_title = page_title[0].strip('www').strip('.')
page_title = wordninja.split(page_title)
page_title = page_title[0].capitalize() + ' ' + page_title[1].capitalize()

# Make the citation

print(f'{last_name}, {first_initial}. ({date_pub}). {title}. {page_title}. Retrieved from {url}')