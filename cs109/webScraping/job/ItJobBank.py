from bs4 import BeautifulSoup
import requests
import time
import datetime
from datetime import datetime
from job import Job

class ItJobBankJob(Job):
    #KEYWORD_LIST=["Java","Data", "developer"]
    KEYWORD_LIST=["Java"]
    EXECLUDE_TITLE = ["frontend", "c#", "udvikler", "android", "analyst", "devops", "security", "sale", "Javascript", "QA",".NET","javascript","microsoft","php", "Netcompany"]
    EXECLUDE_COMPANY = ["dfds", "prodata", "Systematic","test"]
    PAGE_SIZE = 1

    def parse(self, page_content):
        result = []
        h3_title = page_content.find_all("h3", "job-title")
        div_info = page_content.find_all("div", "job-info")
        div_company = page_content.find_all("div", "job-company")
        div_time= page_content.find_all("time")
        #span_location = page_content.find_all("span", "job-location")
        divSize = len(h3_title)
        for i in range(0, divSize):
            #print(div_company[i].text)
            #print(h3_title[i].a.text)
            location= 'cph'
            if div_info[i].div.span is not None:
                location = div_info[i].div.span.text.replace(',',' ')
            #print(location)
            #print(h3_title[i].a["href"])            
            #print(div_time[i]["datetime"])
            #print()
            link=h3_title[i].a["href"]
            title=h3_title[i].a.text
            company=div_company[i].text
            now = datetime.now() # current date and time
            time = now.strftime("%Y-%m-%d")            
            #if "month" not in time and super().ex_filter(title, ItJobBankJob.EXECLUDE_TITLE) and super().ex_filter(company, ItJobBankJob.EXECLUDE_COMPANY):
            if super().ex_filter(title, ItJobBankJob.EXECLUDE_TITLE) and super().ex_filter(company, ItJobBankJob.EXECLUDE_COMPANY):
                text = "{},{},{},{},##{}".format(title, company, location, time, link);
                print(text)
                result.append(text)
        return result

    def get_url(self, keyword, pageNum):
        return "https://www.it-jobbank.dk/job/software-webudvikling/storkoebenhavn?q="+keyword+"&page=" +str(pageNum)
