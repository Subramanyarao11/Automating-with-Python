import bs4 , requests

def getAmazonPrice(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('span.a-price:nth-child(2) > span:nth-child(2) > span:nth-child(2)')
    return elems[0].text.strip()

price = getAmazonPrice('https://www.amazon.in/2022-Apple-MacBook-Laptop-chip/dp/B0B3B5BWCT/ref=sr_1_1_sspa?crid=3HN5EJZGTTIL7&keywords=macbook+pro&qid=1673463741&sprefix=mac%2Caps%2C312&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1')
print('The price is ' + price)
