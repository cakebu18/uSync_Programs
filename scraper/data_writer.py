#### uSync LLC
#### Matthew O'Connor, Co-Founder

# Imports
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from web_scraper import get_tournament_info, get_date
import requests
import re
import csv
import os
import shutil

# use while loop to check the date using the getDate function created in web_scraper

# Test data
# test_data = [{'date': 'September 12, 2022', 'time': '10:20 PM', 'title': '2v2 1ND MW SND', 'entry': '$4', 'team_size': '2', 'platforms': ['xbox', 'playstation', 'battle.net'], 'game': 'Call of Duty Modern Warfare 2'}, {'date': 'September 12, 2022', 'time': '9:20 PM', 'title': '3v3 1ND CW SND', 'entry': '$4', 'team_size': '3', 'platforms': ['xbox', 'playstation', 'battle.net'], 'game': 'Call of Duty Modern Warfare 2'}]

URL = "https://esportsagent.gg/tournament"
driver = webdriver.Chrome(ChromeDriverManager().install())

# all_info = get_tournament_info(driver, URL)
# print(all_info)

def current_tournaments(driver, URL):
    all_tourneys = []
    tourney = get_tournament_info(driver, URL)
    while (tourney["date"] == get_date()):
        all_tourneys.append(tourney)
        print(all_tourneys)

print(current_tournaments(driver, URL))

# Write all data to CSV file
# Input: data to write, optional path but will default to tournaments_data.csv
# Returns: None
def write_all(data, path = "tournaments_data.csv"):

    # Header for CSV file
    header = ['Date', 'Time', 'Title', 'Entry', 'Team Size', 'Platforms', 'Game']
    field_names = ["date", "time", "title", "entry", "size", "platforms", "game"]

    # Case: 'tournaments data' file does not exist
    # if not(os.path.isfile(path)):
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        dict_writer = csv.DictWriter(f, fieldnames=field_names)
        dict_writer.writerows(data)

        print("Done. New file Created")
        return None
    # Case: 'tournaments data' exists
    # else:
    #     with open(path, 'r') as fr:
    #         read_data = []
    #         reader = csv.reader(fr)

    #         for line in reader:
    #             if line[4] != 'Size':
    #                 line[4] = eval(line[4])
    #             read_data.append(line)

    #         # removing unneeded header info
    #         read _ data = read_data[1:len(read_data)]

    # OVERALL_WRITE = 0
    # WRITE_FLAG = 0
    # new_data = []
    # for d in data:
    #     d_vals = list(d.values())
    #     for rd in read_data:
    #         if rd == d_vals:
    #             WRITE_FLAG = 0
    #             break
    #         else:
    #             WRITE_FLAG = 1
    #     if WRITE_FLAG:
    #         new_data.append(d_vals)
    #         OVERALL_WRITE = 1
    #         WRITE_FLAG = 0
    # all_data = new_data
    # if OVERALL_WRITE:
    #     with open(path, 'w', newline = '') as fw:
    #         writer = csv.writer(fw)
    #         writer.writerow(header)
    #         for ad in all_data:
    #             writer.writerow(ad)
    #         print("Done. New data written.")
    #         return None
    # else:
    #     print("Done. No new data written.")
    # return None

# print(write_all(all_info, "tournaments_data.csv"))
            

            


