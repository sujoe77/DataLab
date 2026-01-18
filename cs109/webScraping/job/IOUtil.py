import requests
from bs4 import BeautifulSoup
from requests.packages.urllib3.exceptions import InsecureRequestWarning

def write_file(jobSet, fileName):
    print("final set size is: " + str(len(jobSet)))
    with open(fileName, 'w', encoding='utf-8') as f:
        f.write("Title,Company,City,pub_date,Link,Tags\n")
        for i in range(0, len(jobSet)):
            f.write(jobSet.pop()+"\n")
    f.close()

def get_content(url):
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    page_response = requests.get(url, timeout=180, verify=False)
    return BeautifulSoup(page_response.content, "html.parser")

def get_content_linkedIn(url):
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    page_response = requests.get(url, timeout=180, verify=False)
    content = page_response.content.decode("utf-8")
    content = content.replace("<!DOCTYPE html>", "<!DOCTYPE html><html>")
    content = content + "</html>"
    return BeautifulSoup(content, "html.parser")