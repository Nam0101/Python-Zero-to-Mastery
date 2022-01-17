import requests
from bs4 import BeautifulSoup
import pprint
re = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(re.text, 'html.parser')
links = soup.select('.titlelink')
votes = soup.select('.score')
subtex = soup.select('.subtext')


def create_custom_hn(links, subtex):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        vote = subtex[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'point': points})
    return sorted(hn, key=lambda x: x['point'], reverse=True)


pprint.pprint(create_custom_hn(links, subtex))
