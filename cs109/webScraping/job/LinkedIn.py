from job import Job
from datetime import date
import datetime as DT
from util.IOUtil import get_content_linkedIn
import urllib.parse

class LinkedInJob(Job):
    #KEYWORD_LIST=["Java","Data", "developer"]
    #KEYWORD_LIST=["Java"]
    EXECLUDE_TITLE = ["student", "test", "frontend", 
                      #"c#", "udvikler", 
                      "android", 
                      "analyst", 
                      #"devops", "security", 
                      "sale", 
                      #"Javascript", 
                      "QA",
                      #".NET",
                      #"javascript",
                      #"microsoft",
                      "php"
                     ]
    EXECLUDE_COMPANY = ["prodata", "SoftNice"]
    PAGE_SIZE = 5

    def parse(self, page_content):
        result = []
        #li = page_content.find_all("li", "result-card job-result-card result-card--with-hover-state")
        li = page_content.find_all("li")
        divSize = len(li)
        print(divSize)
        for i in range(0, divSize):
            titleList = li[i].find_all("span", "sr-only")
            if len(titleList)==0:
                continue
            link = li[i].a["href"]
            #print(li[i].div)
            titleList = li[i].find_all("span", "sr-only")
            title = titleList[0].text.replace("\n", "").lstrip().rstrip().replace(",", "_")
            #print(title)
            company = li[i].div.h4.text if li[i].div.h4.a is None else li[i].div.h4.a.text    
            company = company.replace(",", "_").replace("\n", "").lstrip().rstrip()
            #print(company)
            timeList=li[i].find_all("time")
            time=timeList[0].text.replace("\n", "").lstrip().rstrip().replace(",", "_")
            time=self.getPubDate(time)
            #print(time.text.replace("\n", "").lstrip().rstrip())            
            locationList = li[i].find_all("span", "job-search-card__location")
            location = locationList[0].text.replace("\n", "").lstrip().rstrip().replace(",", "_")
            #print(location)
            if "month" not in time and super().ex_filter(title, LinkedInJob.EXECLUDE_TITLE) and super().ex_filter(company, LinkedInJob.EXECLUDE_COMPANY):
                text = "{},{},{},{},##{}".format(title, company, location, time, link)
                print(text)
                result.append(text)
        return result

    def get_url(self, keyword, pageNum):
        #url = "https://www.linkedin.com/jobs/search/?keywords="+keyword+"&location=copenhagen%20denmark&start=" + str(pageNum*25)
        url = "https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords={keyword}&location={location}&start={start}"
        url = "https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords={keyword}&start={start}&geoId=102194656"
        url = "https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?distance=40&f_TPR=a1769632530-&f_WT=1%2C3&geoId=102194656&keywords={keyword}&origin=JOB_SEARCH_PAGE_SEARCH_BUTTON&start={start}"
        url = url.format(keyword=urllib.parse.quote(keyword, safe=''), location="copenhagen", start=pageNum*10)        
        return url

    def getPubDate(self, timeStr):
        today = date.today()

        # dd/mm/YY
        #d1 = today.strftime("%Y-%m-%d")
        #print("d1 =", d1)

        time = timeStr.split()
        delta = int(time[0])
        unit = time[1]
        if unit.startswith("day"):
            delta = delta * 24
        elif unit.startswith("week"):
            delta = delta * 24 * 7

        pub_date = today - DT.timedelta(hours=delta)
        return pub_date.strftime("%Y-%m-%d")

    def process_page(self, url):
        print(url)
        page_content = get_content_linkedIn(url)
        #print(page_content)
        return self.parse(page_content)