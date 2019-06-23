from bs4 import BeautifulSoup
import requests
import time
import datetime
from job import Job

class ItJobBankJob(Job):
    #KEYWORD_LIST=["Java","Data", "developer"]
    KEYWORD_LIST=["Java"]
    EXECLUDE_TITLE = ["frontend", "c#", "udvikler", "android", "analyst", "devops", "security", "sale", "Javascript", "QA",".NET","javascript","microsoft","php", "Netcompany"]
    EXECLUDE_COMPANY = ["dfds", "prodata", "Systematic","test"]
    PAGE_SIZE = 1

    def parse(self, page_content):
        result = []
        h3_title = page_content.find_all("h3", "title")
        div_info = page_content.find_all("div", "info")
        div_time= page_content.find_all("time")        
        divSize = len(h3_title)
        for i in range(0, divSize):
            print(h3_title[i].a["href"])
            print(h3_title[i].text)
            print(div_info[i].text)
            print(div_time[i]["datetime"])
            print()
            link=h3_title[i].a["href"]
            title=h3_title[i].text
            company=div_info[i].text
            time=div_time[i]["datetime"]
            location="cph"
            if "month" not in time and super().ex_filter(title, ItJobBankJob.EXECLUDE_TITLE) and super().ex_filter(company, ItJobBankJob.EXECLUDE_COMPANY):
                text = "{},{},{},{},##{}".format(title, company, location, time, link);
                print(text)
                result.append(text)
        return result

    def get_url(self, keyword, pageNum):
        return "https://www.it-jobbank.dk/job/software-webudvikling/storkoebenhavn?q="+keyword+"&page=" +str(pageNum)
