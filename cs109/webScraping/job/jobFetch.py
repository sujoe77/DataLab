from bs4 import BeautifulSoup
import requests
import time
import datetime
import os
import sys
from FetchThread import FetchThread

sys.path.append("/media/zhou/DATA/zhousu/git/github_new/DataLab/cs109/webScraping/job")
from StackOverflow import StackOverflowJob

from LinkedIn import LinkedInJob
from ItJobBank import ItJobBankJob
from Nordea import NordeaJob
from neuvoo import NeuvooJob
from JobIndex import JobIndexJob
from job import Job

import psycopg2

import threading


EXECLUDE_TITLE = ["frontend", "c#", "udvikler", "android", "analyst", "devops", "security", "sale","microsoft"]
EXECLUDE_COMPANY = ["dfds", "prodata", "Systematic","test"]
#KEYWORD_LIST=["Java","Data", "developer"]
KEYWORD_LIST=["Java", "Backend", "data", "architect"]
STACKOVERFLOW_KEYWORD_LIST=["Backend"]
SLEEP=6
PAGE_SIZE = 5

print("KEYWORD_LIST size: " + str(KEYWORD_LIST))
print("EXECLUDE_COMPANY size: " + str(EXECLUDE_COMPANY))
print("SLEEP: " + str(SLEEP))
print("PAGE_SIZE: " + str(PAGE_SIZE))

jobs=[Job(), ]

jobSet = set([])

list1 = [LinkedInJob(), JobIndexJob(), NeuvooJob(), ItJobBankJob(), StackOverflowJob()]
list2 = [LinkedInJob(),  JobIndexJob(), NeuvooJob(), ItJobBankJob()]
list3 = [ StackOverflowJob()]
list4 = [ JobIndexJob()]

def fetch_job(jobSet, keyWords, size):
    jobSet = jobSet.union(jobSite.get_jobset(keyWords, size, SLEEP))

for jobSite in list2:
    thread1 = FetchThread(jobSite, KEYWORD_LIST, 5)
    thread1.start()

for jobSite in list3:
    thread1 = FetchThread(jobSite, STACKOVERFLOW_KEYWORD_LIST, 5)
    thread1.start()

#j.write_file(jobSet, './data/all_jobs'+datetime.datetime.now().strftime("%Y%m%d%H%M%S")+'.csv')
#print(jobSet)