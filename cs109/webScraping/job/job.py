from bs4 import BeautifulSoup
import requests
import time
import datetime

class Job:

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

    def process_page(self, url):
        page_content = self.get_content(url)    
        #print(page_content)
        return self.parse(page_content)


    def get_jobset(self, keywordList, pageSize, sleep):
        jobSet = set([])
        keySet = set([])
        for keyword in keywordList: 
            for i in range(0, pageSize): 
                url = self.get_url(keyword, i)
                print(url)
                result = self.process_page(url)
                time.sleep(sleep)
                retry=0
                MAX_RETRY=3
                while(len(result) == 0 and retry<MAX_RETRY):
                    result = self.process_page(url)
                    time.sleep(sleep)
                    print("retry!")
                    retry+=1
                sizeBefore = len(jobSet)
                for ii in range(0, len(result)):
                    #print(result[ii].split("##")[0])
                    if(result[ii].split("##")[0] not in keySet):
                        keySet.add(result[ii].split("##")[0])
                        jobSet.add(result[ii].replace("##",""))
                print("result size {}, set size before {}, after {}".format(sizeBefore, len(result), len(jobSet)))
        return jobSet
