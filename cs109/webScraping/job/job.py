from bs4 import BeautifulSoup
import requests
import time
import datetime

class Job:
    EXECLUDE_TITLE = ["frontend", "c#", "udvikler", "android", "analyst", "devops", "security", "sale"]
    EXECLUDE_COMPANY = ["dfds", "prodata", "Systematic","test"]
    KEYWORD_LIST=["Java","Data", "developer"]
    SLEEP=6
    PAGE_SIZE = 1
    
    def __init__(self):
        return

    def ex_filter(self, title, exList):
        for keyword in exList:
            if(keyword.lower() in title.lower()):
                #print("------------>" + keyword + " found in " + title)
                return False
        return True

    def get_content(self, url):
        page_response = requests.get(url, timeout=5)
        return BeautifulSoup(page_response.content, "html.parser")
        
    def write_file(self, jobSet, fileName):
        print("final set size is: " + str(len(jobSet)))
        with open(fileName, 'w', encoding='utf-8') as f:
            f.write("Title,Company,Location,Time,Link\n")
            for i in range(0, len(jobSet)):
                f.write(jobSet.pop()+"\n")
        f.close()
        
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
            #if "month" not in time and ex_filter(title, EXECLUDE_TITLE) and ex_filter(company, EXECLUDE_COMPANY):
            text = "{},{},{},{},##{}".format(title, company, location, time, link);
            #print(text)
            result.append(text)
        return result

    def get_url(self, keyword, pageNum):
        return "https://www.linkedin.com/jobs/search/?keywords="+keyword+"&location=copenhagen%20denmark&start=" + str(pageNum*25)

    def get_jobset(self, keywordList, pageSize):
        jobSet = set([])
        keySet = set([])
        for keyword in keywordList:        
            for i in range(0, pageSize):            
                url = self.get_url(keyword, i)
                print(url)
                result = process_page(url)
                time.sleep(Job.SLEEP)
                while(len(result) == 0):
                    result = process_page(url)
                    time.sleep(Job.SLEEP)
                    print("retry!")
                sizeBefore = len(jobSet)
                for ii in range(0, len(result)):
                    #print(result[ii].split("##")[0])
                    if(result[ii].split("##")[0] not in keySet):
                        keySet.add(result[ii].split("##")[0])
                        jobSet.add(result[ii].replace("##",""))
                print("result size {}, set size before {}, after {}".format(sizeBefore, len(result), len(jobSet)))
        return jobSet


    def process_page(self, url):
        page_content = self.get_content(url)    
        #print(page_content)
        return self.parse(page_content)
        

    def get_jobset(self, keywordList, pageSize):
        jobSet = set([])
        keySet = set([])
        for keyword in keywordList:        
            for i in range(0, pageSize):            
                url = self.get_url(keyword, i)
                print(url)
                result = self.process_page(url)
                time.sleep(Job.SLEEP)
                while(len(result) == 0):
                    result = self.process_page(url)
                    time.sleep(Job.SLEEP)
                    print("retry!")
                sizeBefore = len(jobSet)
                for ii in range(0, len(result)):
                    #print(result[ii].split("##")[0])
                    if(result[ii].split("##")[0] not in keySet):
                        keySet.add(result[ii].split("##")[0])
                        jobSet.add(result[ii].replace("##",""))
                print("result size {}, set size before {}, after {}".format(sizeBefore, len(result), len(jobSet)))
        return jobSet