import time

import psycopg2
from IOUtil import get_content

MAX_RETRY = 3


class Job:

    def __init__(self):
        return

    def ex_filter(self, title, exList):
        for keyword in exList:
            if(keyword.lower() in title.lower()):
                #print("------------>" + keyword + " found in " + title)
                return False
        return True

    def process_page(self, url):
        page_content = get_content(url)
        #print(page_content)
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
        return jobSet

    def retryUrl(self, MAX_RETRY, result, sleep, url):
        retry = 0
        while (len(result) == 0 and retry < MAX_RETRY):
            time.sleep(sleep)
            result = self.process_page(url)
            print("retry -> " + url)
            retry += 1
        return result

    def toJobSet(self, jobSet, keySet, result, url):
        sizeBefore = len(jobSet)
        for ii in range(0, len(result)):
            # print(result[ii].split("##")[0])
            if (result[ii].split("##")[0] not in keySet):
                keySet.add(result[ii].split("##")[0])
                jobSet.add(result[ii].replace("##", ""))
        print("result size {}, set size before {}, after {}, page: {}".format(sizeBefore, len(result), len(jobSet), url))


def insert_job(jobSet):
    """ insert a new vendor into the vendors table """
    sql = """INSERT INTO jobs(title, company, city, pub_date, link, tags)
             VALUES(%s, %s, %s, %s, %s, %s);"""
    query_sql = "select count(link) from jobs where link=%s or (title = %s and company = %s) "
    conn = psycopg2.connect(
        host="localhost",
        database="mydb",
        user="postgres",
        password="postgres")
    vendor_id = None
    totalInsert = 0
    try:
        cur = conn.cursor()
        for job in jobSet:
            values = job.split(",")
            cur.execute(query_sql, (values[4],values[0], values[1],))
            records = cur.fetchall()
            rowcount = 0
            for row in records:
                rowcount = row[0]
                #print("find duplicate ", str(rowcount), )
            if rowcount == 0:
                print("do insert " , values[0],values[1],values[2],values[3],values[4],)
                cur.execute(sql, (values[0],values[1],values[2],values[3],values[4], ''))
                totalInsert += 1
        conn.commit()
        cur.close()
        print("total insert: ", totalInsert, )
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()