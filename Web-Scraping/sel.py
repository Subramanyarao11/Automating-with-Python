from selenium import webdriver

browser = webdriver.Firefox()
browser.get('https://automatetheboringstuff.com/')
emailSub = browser.find_element(".main > main:nth-child(1) > div:nth-child(1) > ul:nth-child(19) > li:nth-child(13) > a:nth-child(1)")
print(emailSub)
