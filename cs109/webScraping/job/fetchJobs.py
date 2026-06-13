from constants import EXECLUDE_TITLE, EXECLUDE_COMPANY, KEYWORD_DIC_ALL
from LinkedIn import LinkedInJob
from FetchTask import FetchTask
from util.JobFetcher import fetchJobs

def fetch_jobs():
    job_sites = [LinkedInJob(EXECLUDE_TITLE, EXECLUDE_COMPANY)]

    for jobSite in job_sites:
        tasks = [
            FetchTask(jobSite, [keyWord], size, "task_" + keyWord, 5)
            for keyWord, size in KEYWORD_DIC_ALL.items()
        ]
        fetchJobs(tasks)

fetch_jobs()