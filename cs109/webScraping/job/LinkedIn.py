from bs4 import BeautifulSoup
import requests
import time
import datetime
from job import Job

class LinkedInJob(Job):
    #KEYWORD_LIST=["Java","Data", "developer"]
    KEYWORD_LIST=["Java"]
    EXECLUDE_TITLE = ["frontend", "c#", "udvikler", "android", "analyst", "devops", "security", "sale", "Javascript", "QA",".NET","javascript","microsoft","php"]
    EXECLUDE_COMPANY = ["dfds", "prodata", "Systematic","test"]
    PAGE_SIZE = 3

    def parse(self, page_content):
        result = []
        li = page_content.find_all("li", "result-card job-result-card result-card--with-hover-state")
        divSize = len(li)    
        for i in range(0, divSize):
            link = li[i].a["href"]
            title = li[i].div.h3.text.replace(",","_")
            company = li[i].div.h4.text if li[i].div.h4.a is None else li[i].div.h4.a.text    
            company = company.replace(",", "_")
            time = li[i].div.div.time.text
            location = li[i].div.div.span.text.replace(",", "_")
            #print(title)
            if "month" not in time and super().ex_filter(title, LinkedInJob.EXECLUDE_TITLE) and super().ex_filter(company, LinkedInJob.EXECLUDE_COMPANY):
                text = "{},{},{},{},##{}".format(title, company, location, time, link);
                #print(text)
                result.append(text)
        return result

    def get_url(self, keyword, pageNum):
        return "https://www.linkedin.com/jobs/search/?keywords="+keyword+"&location=copenhagen%20denmark&start=" + str(pageNum*25)
