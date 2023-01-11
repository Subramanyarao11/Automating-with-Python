import bs4 , requests
res = requests.get('https://dev.to/novu/creating-a-website-aggregator-with-chatgpt-react-and-nodejs-4dij')
res.raise_for_status()

# Create a BeautifulSoup object
soup = bs4.BeautifulSoup(res.text, 'html.parser')
elems = soup.select('div.crayons-card--secondary:nth-child(1) > div:nth-child(1) > a:nth-child(1) > span:nth-child(2)')
print(elems[0].text.strip())
