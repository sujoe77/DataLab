import threading
from job import insert_job


class FetchThread (threading.Thread):
    
    def __init__(self, jobSite, keyWords, pageSize, name):
        threading.Thread.__init__(self)
        self.jobSite = jobSite
        self.pageSize = pageSize
        self.keyWords = keyWords
        self.name = name

    def run(self):
        print("Starting " + self.name)
        jobSet = self.jobSite.get_jobset(self.keyWords, self.pageSize, 5)
        insert_job(jobSet)
        print("Exiting " + self.name)

