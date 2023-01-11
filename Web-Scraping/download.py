import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
# print(res.status_code)
# print(res.text[:250])

# Raises an error if downloading fails
res.raise_for_status()


romeoJulietPlay = open('romeoJuliet.txt', 'wb')
# Write the content of the response object to the file
for chunk in res.iter_content(100000):
    romeoJulietPlay.write(chunk)
romeoJulietPlay.close()
