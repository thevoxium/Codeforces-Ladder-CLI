from importlib.resources import path
from urllib import response
import requests
import json
import click
import pandas as pd
from bs4 import BeautifulSoup


def get_sub_list(handle):
    
    url = "https://codeforces.com/api/user.status?handle="+handle
    response = requests.get(url)
    data = response.json()

    a = []

    for x in data["result"]:
        if (x["verdict"] == "OK"):
            a.append(x["problem"]["name"])

    return a

@click.command()
@click.option('--div', default = "A", help = "Division of Problem that you want to extract")
@click.option('--ir', default = 800, help = "Initial Rating of Problems")
@click.option('--fr', default = 8000, help = "Final Rating of Problems")
@click.option('--num', default = 15, help = "Number of Problems of Each Rating")
@click.option('--handle', prompt = "Enter Your Username")
def generate_sheet(div, ir, fr, num, handle):
    URL = "https://codeforces.com/api/problemset.problems"

    response = requests.get(URL)
    data = response.json()

    a = get_sub_list(handle)

    problems = {
        "prob_name": [],
        "prob_link": [],
        "prob_rating": []
    }

    num_ = {}

    for i in range(ir, fr+1):
        if (i%100 == 0):
            num_[i] = 0

    for x in data["result"]["problems"]:
        if (len(x) >= 6):
            if (x["index"] == div and "rating" in x and x["name"] not in a):
                if (x["rating"] >= ir and x["rating"]<=fr):

                    num_[x["rating"]]+=1

                    if (num_[x["rating"]] > num):
                        continue

                    link = "https://codeforces.com/contest/"+str(x["contestId"])+"/problem/"+div
                    problems["prob_name"].append(x["name"])
                    problems["prob_link"].append(link)
                    problems["prob_rating"].append(x["rating"])
                    
    df = pd.DataFrame(problems)

    df = df.sort_values('prob_rating')

    df.to_excel("list.xlsx", index = False)

    print("Sheet is generated")


if __name__ == '__main__':
    generate_sheet()