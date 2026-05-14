import db


class FetchTask:
    def __init__(self, jobSite, keyWords, pageSize, name, sleep):
        self.jobSite = jobSite
        self.pageSize = pageSize
        self.keyWords = keyWords
        self.name = name
        self.sleep = sleep

    def run(self):
        print("Starting " + self.name)
        jobSet = self.jobSite.get_jobset(self.keyWords, self.pageSize, self.sleep)
        db.insert_job(jobSet, self.name)
        print("Exiting " + self.name)
