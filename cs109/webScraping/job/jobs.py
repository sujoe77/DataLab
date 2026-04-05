import time
from util.IOUtil import get_content

MAX_RETRY = 3

class Job:
    def __init__(self):
        return

    def ex_filter(self, title, exList):
        for keyword in exList:
            if keyword.lower() in title.lower():
                # print("------------>" + keyword + " found in " + title)
                return False
        return True

    def process_page(self, url):
        print(url)
        page_content = get_content(url)
        # print(page_content)
        return self.parse(page_content)

    def get_jobset(self, keywordList, pageSize, sleep, start=0):
        jobSet = set([])
        keySet = set([])
        for keyword in keywordList:
            for i in range(start, start + pageSize):
                url = self.get_url(keyword, i)
                result = self.process_page(url)
                result = self.retryUrl(MAX_RETRY, result, sleep, url)
                if len(result) == 0:
                    break
                self.toJobSet(jobSet, keySet, result, url)
                time.sleep(sleep)
        return jobSet

    def retryUrl(self, MAX_RETRY, result, sleep, url):
        retry = 0
        while len(result) == 0 and retry < MAX_RETRY:
            time.sleep(sleep)
            result = self.process_page(url)
            print("retry -> " + url)
            retry += 1
        return result

    def toJobSet(self, jobSet, keySet, result, url):
        sizeBefore = len(jobSet)
        for ii in range(0, len(result)):
            # print(result[ii].split("##")[0])
            if result[ii].split("##")[0] not in keySet:
                keySet.add(result[ii].split("##")[0])
                jobSet.add(result[ii].replace("##", ""))
        print(
            "result size {}, set size before {}, after {}, page: {}".format(
                sizeBefore, len(result), len(jobSet), url
            )
        )
