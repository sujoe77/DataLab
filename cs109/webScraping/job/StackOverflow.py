from bs4 import BeautifulSoup
import requests
import time
import datetime
from job import Job

class StackOverflowJob(Job):
    KEYWORD_LIST=["Java"]
    EXECLUDE_TITLE = ["frontend", "c#", "udvikler", "android", "analyst", "devops", "security", "sale", "Javascript", "QA",".NET","javascript","microsoft","php"]
    EXECLUDE_COMPANY = ["dfds", "prodata", "Systematic","test"]


    def parse(self, page_content):
        result = []
        #<h2 class="mb4 fc-black-800 fs-body3">
        title_h2 = page_content.find_all("h2", "mb4 fc-black-800 fs-body3")
        #<h3 class="fc-black-700 fs-body1 mb4">
        company_h3=page_content.find_all("h3", "fc-black-700 fs-body1 mb4")
        timeDiv = page_content.find_all("div", "mt4 fs-caption fc-black-500 grid gs4 gsx fw-wrap")
        print("div size:" + str(len(title_h2)))
        #divSize = len(div)
        j=0
        for i in range(0, len(title_h2)):
            #if div[i].div is None or div[i].div.h2 is None or div[i].div.h2.a is None:
            #    continue
            link = "https://stackoverflow.com"+title_h2[i].a["href"]
            title = title_h2[i].a.text.replace("\n", " ").strip().replace(",", "_")
            #print(title)
            company = company_h3[i].span.text.replace("\n", " ").replace("\r", " ").strip()
            #company = div[i].children[1]#.contents[1].text
            #print("c1" + company)
            company = company.replace(",", "_").replace("\n", " ").replace("\r", " ").strip()            
            #print(company)
            time = timeDiv[j].div.text.replace(",", "_").replace("\n", " ").replace("\r", " ").strip()
            j = j+1
            #print("time -> " + time)
            location = company_h3[i].contents[3].text.replace(",", "_").replace("\n", " ").replace("\r", " ").strip()
            #.contents[1].text            #div[i].contents[3].contents[3].text.replace("\n", "").replace("\r", "").replace("-", "").strip().replace(",", "_")
            #print("location -> " + location)
            if "month" not in time and super().ex_filter(title, StackOverflowJob.EXECLUDE_TITLE) and super().ex_filter(company, StackOverflowJob.EXECLUDE_COMPANY):
                text = "{},{},{},{},##{}".format(title, company, location, time, link);
                #print(text)
                result.append(text)
        return result

    def get_url(self, keyword, pageNum):
        return "https://stackoverflow.com/jobs?l=Copenhagen%2C+Denmark&d=20&u=Km&pg=" + str(pageNum+1)
