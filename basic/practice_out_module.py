from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())

# pip list
# pip show beautifulsoup4
# pip install --upgrade beautifulsoup4 
# pip unintall beautifulsoup4
