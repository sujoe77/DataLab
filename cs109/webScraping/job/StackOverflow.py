from bs4 import BeautifulSoup
import requests
import time
import datetime
from job import Job

class StackOverflowJob(Job):
    KEYWORD_LIST=["Java"]

    def parse(self, page_content):
        result = []
        div = page_content.find_all("div", "-job-summary")
        print("div size:" + str(len(div)))
        divSize = len(div)    
        for i in range(0, divSize):
            link = div[i].div.h2.a["href"]
            title = div[i].div.h2.a.text.replace("\n", "").strip().replace(",", "_")
            #print(title)
            company = div[i].contents[3].span.text#.contents[1].text            
            #company = div[i].children[1]#.contents[1].text
            #print("c1" + company)
            company = company.replace(",", "_").replace("\n", "").replace("\r", "").strip()
            #print(company)
            time = div[i].div.contents[5].text
            #print(time)
            location = div[i].contents[3].contents[3].text.replace("\n", "").replace("\r", "").replace("-", "").strip().replace(",", "_")
            #print(location)
            #if "month" not in time and ex_filter(title, EXECLUDE_TITLE) and ex_filter(company, EXECLUDE_COMPANY):
            text = "{},{},{},{},##{}".format(title, company, location, time, link);
            #print(text)
            result.append(text)
        return result

    def get_url(self, keyword, pageNum):
        return "https://stackoverflow.com/jobs?l=Copenhagen%2C+Denmark&d=20&u=Km&pg=" + str(pageNum+1)
