import re
from pprint import pprint
import argparse

import requests
from bs4 import BeautifulSoup


parser = argparse.ArgumentParser()
parser.add_argument('my_points', type=int)

args = parser.parse_args()


r = requests.get("https://abit.itmo.ru/bachelor/rating/266/", verify=False)
soup = BeautifulSoup(r.text, 'html.parser')

rows = soup.find(class_="table-page__wrapper").find_all("tr")

positive_above_me = []

for r in rows:
    if r.find("td", string="Да"):
        columns = r.find_all("td")
        full_points = columns[8].text
        if full_points and int(full_points) > args.my_points:
            positive_above_me.append({"name": columns[2].text, "points": columns[8].text })

pprint(positive_above_me)
print(f"Всего подавших согласие с баллом выше {args.my_points}: {len(positive_above_me)}")