import requests
from bs4 import BeautifulSoup
from urllib3.exceptions import InsecureRequestWarning


def write_file(jobSet, fileName):
    print("final set size is: " + str(len(jobSet)))
    with open(fileName, "w", encoding="utf-8") as f:
        f.write("Title,Company,City,pub_date,Link,Tags\n")
        for i in range(0, len(jobSet)):
            f.write(jobSet.pop() + "\n")
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


def get_content_coolshell(url):
    print("get_content_coolshell fetching url: " + url)
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    print("get_content_coolshell before fetching! ")
    page_response = requests.get(url, timeout=180, verify=False)
    print("get_content_coolshell get response: " + str(page_response.status_code))
    if(str(page_response.status_code) != "200"):
        print("get_content_coolshell failed to fetch url: " + url)
        return None
    content = page_response.content.decode('utf-8', errors='ignore')
    content = content.replace("<!DOCTYPE html>", "<!DOCTYPE html><html>")
    content = content + "</html>"
    return BeautifulSoup(content, "html.parser")