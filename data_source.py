import requests
import os
import time

def get_page(i):
    url = r'https://shr32taah3.execute-api.us-east-1.amazonaws.com/Prod/applications/browse?pageSize=12&pageNumber=%d&searchText=&category=&runtime=&verified=&sortFields='
    page = requests.get(url%i)
    return eval(page.text.replace("true", "True").replace("false", "False"))

data = get_page(3)
for i in range(1, 4):
    data = get_page(i)
    for item in data["applications"]:
        print(item["deploymentCount"], end="\t")
        print(item["name"])
        print(item["homePageUrl"])
        print()
        # os.popen("git clone " + item["homePageUrl"])
        # time.sleep(3)
