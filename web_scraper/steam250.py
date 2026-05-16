import requests
import pandas as pd
from bs4 import BeautifulSoup as bs
from tqdm import tqdm
import time
import random

class steam250:
    def __init__(self):
        pass

    def insert_data(soup, array):
        for i in soup.find_all("a", class_="store"):
            try:
                array.append(int(i["href"].split("/")[4]))
            except:
                continue

    def insert_data_algo(soup, array):
        for i in soup.find("tbody").find_all("span", class_="title"):
            array.append(int(i.find("a")['href'].split("/")[4]))


    def data_to_csv(path, array):
        df = pd.DataFrame(array, columns=["id"])
        df.to_csv(path, index=False)

    def fill_in(soup, array, div_num):
        for i in soup.find_all("div")[div_num]:
            try:
                array.append(f"https://steam250.com{i['href']}")
            except:
                continue

    def get_data(soup, soup_algo):

        for i in soup.find_all("section", class_="top10"):
            main_page.append(f"https://steam250.com/{i.find("a")['href']}")

        for i in soup.find_all("a", class_="tag"):
            tags.append(f"https://steam250.com{i['href']}")

        for i in soup_algo.find("ul").find_all("a"):
            algorithms.append(f"https://algorithms.steam250.com/{i['href']}")

        steam250.fill_in(soup, rankings, 12)
        steam250.fill_in(soup, rankings, 14)
        steam250.fill_in(soup, rankings, 15)
        steam250.fill_in(soup, rankings, 16)
        
        steam250.fill_in(soup, deals, 22)
        steam250.fill_in(soup, deals, 24)
        steam250.fill_in(soup, deals, 25)
        
        steam250.fill_in(soup, dates, 27)
        steam250.fill_in(soup, dates, 29)

        rankings.append("https://steam250.com/reviews")
        rankings.append("https://steam250.com/hidden_novels")

        full_list = main_page + rankings + tags + deals + dates + algorithms
        set_list = list(set(full_list))

        set_list = [i for i in set_list if "https://club.steam250.com" not in i]

        return set_list


if __name__=="__main__":
    all_ids = []
    main_page = []
    rankings = []
    tags = []
    deals = []
    dates = []
    algorithms = []
    csv = 'steam_ids.csv'

    base_url = requests.get("https://steam250.com/").content
    base_soup = bs(base_url, 'html.parser')

    url_algo = requests.get("https://algorithms.steam250.com/").content
    soup_algo = bs(url_algo, 'html.parser')
#only scrapes these 4 pages
    data = [
        "https://steam250.com/top250",
        "https://steam250.com/new",
        "https://steam250.com/hidden_gems",
        "https://steam250.com/year/2026"
    ]
    for i in tqdm(data):
        url = requests.get(i).content
        soup = bs(url, 'html.parser')

        if "algorithms.steam250" in i:
            steam250.insert_data_algo(soup, all_ids)
        else:
            steam250.insert_data(soup, all_ids)

        time.sleep(random.randint(0, 3))

    every_id = list(set(all_ids))
    every_id.sort()
    steam250.data_to_csv(csv, every_id)