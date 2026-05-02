import threading
import FetchTask

class FetchThread(threading.Thread):
    def __init__(self, jobSite, keyWords, pageSize, name, sleep):        
        threading.Thread.__init__(self)        
        self.fetchTask = FetchTask(jobSite, keyWords, pageSize, name, sleep)

    def run(self):        
        self.fetchTask.run()
