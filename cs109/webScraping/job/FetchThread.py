import threading
import psycopg2

class FetchThread (threading.Thread):
    
    def __init__(self, jobSite, keyWords, pageSize):
        threading.Thread.__init__(self)
        self.jobSite = jobSite
        self.pageSize = pageSize
        self.keyWords = keyWords

    def run(self):
        print("Starting ")
        jobSet = self.jobSite.get_jobset(self.keyWords, self.pageSize, 5)
        insert_job(jobSet)
        print("Exiting ")
        
        
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