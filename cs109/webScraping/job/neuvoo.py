from bs4 import BeautifulSoup
import requests
import time
from datetime import datetime
from job import Job

class NeuvooJob(Job):
    KEYWORD_LIST=["Java"]
    EXECLUDE_TITLE = ["frontend", "c#", "udvikler", "android", "analyst", "devops", "security", "sale", "Javascript", "QA",".NET","javascript","microsoft","php"]
    EXECLUDE_COMPANY = ["dfds", "prodata", "Systematic","test"]


    def parse(self, page_content):
        result = []
  
        div_title = page_content.find_all("div", "card__job-title")
        div_company = page_content.find_all("div", "card__job-empname-label")
        div_location = page_content.find_all("div", "card__job-location")
        
        for i in range(0, len(div_title)):
            link = "https://dk.neuvoo.com"+div_title[i].a["href"]
            title = div_title[i].a.text.replace("\n", " ").strip().replace(",", "_")
            company = div_company[i].text.replace(",", "_").replace("\n", " ").replace("\r", " ").strip()            
            location = div_location[i].span.text.replace(",", "_").replace("\n", " ").replace("\r", " ").strip()
            time = datetime.now().strftime("%Y-%m-%d")
            if "month" not in time and super().ex_filter(title, NeuvooJob.EXECLUDE_TITLE) and super().ex_filter(company, NeuvooJob.EXECLUDE_COMPANY):
                text = "{},{},{},{},##{}".format(title, company, location, time, link);
                #print(text)
                result.append(text)
        return result

    def get_url(self, keyword, pageNum):
        return "https://dk.neuvoo.com/job/?k=java&p=" + str(pageNum+1)

