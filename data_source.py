import requests

def get_page(i):
    url = r'https://shr32taah3.execute-api.us-east-1.amazonaws.com/Prod/applications/browse?pageSize=12&pageNumber=%d&searchText=&category=&runtime=&verified=&sortFields='
    page = requests.get(url%i)
    return eval(page.text.replace("true", "True"))

data = get_page(1)
for item in data["applications"]:
    print(item["deploymentCount"], end="\t")
    print(item["name"])
    print(item["homePageUrl"])
