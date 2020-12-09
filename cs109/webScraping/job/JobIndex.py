from bs4 import BeautifulSoup
import requests
import time
from datetime import datetime
from job import Job

class JobIndexJob(Job):
    KEYWORD_LIST=["Java"]
    EXECLUDE_TITLE = ["frontend", "c#", "udvikler", "android", "analyst", "devops", "security", "sale", "Javascript", "QA",".NET","javascript","microsoft","php"]
    EXECLUDE_COMPANY = ["dfds", "prodata", "Systematic","test"]


    def parse(self, page_content):
        result = []        
        div_title = page_content.find_all("div", "PaidJob")
        
        for i in range(0, len(div_title)):
            link  = div_title[i].contents[2]
            if "href" not in str(link):
                link = div_title[i].contents[3]["href"]            
                title = div_title[i].contents[3].b.text.replace("\n", " ").strip().replace(",", "_")
            else:
                link = div_title[i].contents[2]["href"]
                title = div_title[i].contents[2].b.text.replace("\n", " ").strip().replace(",", "_")
            company = div_title[i].p.a.b.text.replace(",", "_").replace("\n", " ").replace("\r", " ").strip()            
            location = div_title[i].p.text.replace(",", "_").replace("\n", " ").replace("\r", " ").strip()
            if "_" in location:
                location = location[location.index("_") + 1:]
            else:
                location = "_"
            time = datetime.now().strftime("%Y-%m-%d")
            if "month" not in time and super().ex_filter(title, JobIndexJob.EXECLUDE_TITLE) and super().ex_filter(company, JobIndexJob.EXECLUDE_COMPANY):
                text = "{},{},{},{},##{}".format(title, company, location, time, link);
                #print(text)
                result.append(text)
        return result

    def get_url(self, keyword, pageNum):
        return "https://www.jobindex.dk/jobsoegning/it/systemudvikling/storkoebenhavn?q=java&page=" + str(pageNum+1)

