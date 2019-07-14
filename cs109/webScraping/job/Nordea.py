from bs4 import BeautifulSoup
import requests
import time
import datetime
from job import Job

class NordeaJob(Job):
    #KEYWORD_LIST=["Java","Data", "developer"]
    KEYWORD_LIST=["Java"]
    EXECLUDE_TITLE = ["frontend", "c#", "udvikler", "android", "analyst", "devops", "security", "sale", "Javascript", "QA",".NET","javascript","microsoft","php", "Netcompany"]
    EXECLUDE_COMPANY = ["dfds", "prodata", "Systematic","test"]
    PAGE_SIZE = 1

    def parse(self, page_content):
        result = []
        tr_jobitem = page_content.find_all("tr", "job-item")
        div_info = page_content.find_all("div", "info")
        div_time= page_content.find_all("time")
        divSize = len(tr_jobitem)
        print(divSize)
        for i in range(0, divSize):
            #print(tr_jobitem[i].td.a["href"])
            title=tr_jobitem[i].td.a.text
            link="https://www.nordea.com/"+tr_jobitem[i].td.a["href"]
            #print(tr_jobitem[i].contents[3].text)
            time=tr_jobitem[i].contents[3].text
            company="Noredea"
            location="Copenhagen"
            if "month" not in time and super().ex_filter(title, NordeaJob.EXECLUDE_TITLE) and super().ex_filter(company, NordeaJob.EXECLUDE_COMPANY):
                text = "{},{},{},{},##{}".format(title, company, location, time, link);
                #print(text)
                result.append(text)
        return result

    def get_url(self, keyword, pageNum):
        return "https://www.nordea.com/en/careers/vacant-positions/?cty=19419&geo=19424&area=19488&jobid=&p=" +str(pageNum+1)
