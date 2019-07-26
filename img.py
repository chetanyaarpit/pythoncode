import re
import requests
from bs4 import BeautifulSoup
#import glob
#import matplotlib

site = 'https://imagebank.asrs.org/Content/imagebank'
response = requests.get(site)

new = ""
# traverse in the string  
for x in response: 
    new += x


soup = BeautifulSoup(response.text, 'html.parser')
img_tags = soup.find_all('img')

urls = [img['src'] for img in img_tags]

for url in urls:
    filename = re.search(r'/([\w_-]+[.](jpg|gif|png))$', url)
    with open(filename.group(1), 'wb') as f:
        if 'http' not in url:
            url = '{}{}'.format(site, url)
        response = requests.get(url)
        f.write(response.content)
