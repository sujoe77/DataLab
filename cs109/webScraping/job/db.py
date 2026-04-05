import threading
import psycopg

insert_job_sql = """
    DO $$
    BEGIN
        IF NOT EXISTS (
            select count(link) from jobs where link=%s or (title = %s and company = %s and (to_date(%s, 'YYYY-MM-DD') - to_date(pub_date, 'YYYY-MM-DD') < 30));
        ) THEN
            INSERT INTO jobs(title, company, city, pub_date, link, tags, add_time)
            VALUES(%s, %s, %s, %s, %s, %s, current_timestamp);
        ELSE
            RAISE NOTICE 'found duplicate positions!';
        END IF;
    END $$;
"""

INSERT_SQL = """INSERT INTO jobs(title, company, city, pub_date, link, tags, add_time)
             VALUES(%s, %s, %s, %s, %s, %s, current_timestamp);"""
QUERY_SQL = "select count(link) from jobs where link=%s or (title = %s and company = %s and (to_date(%s, 'YYYY-MM-DD') - to_date(pub_date, 'YYYY-MM-DD') < 30))"


def insert_job(jobSet):
    # """insert a new vendor into the vendors table"""
    # query_sql = "select count(link) from jobs where link=%s or (title = %s and company = %s) "
    # to_date(%s, 'YYYY-MM-DD') - to_date(pub_date, 'YYYY-MM-DD') < 30
    conn = psycopg.connect(
        # host="localhost", database="mydb", user="postgres", password="postgres"
        "dbname=mydb user=postgres password=postgres host=localhost"
    )
    totalInsert = 0
    try:
        cur = conn.cursor()
        print("job set size is: " + str(len(jobSet)))
        for job in jobSet:
            totalInsert += insert_position(INSERT_SQL, QUERY_SQL, cur, job)
        conn.commit()
        cur.close()
        print(
            threading.current_thread().name + " total insert: ",
            totalInsert,
        )
    except (Exception, psycopg.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def insert_position(cur, jobStr):
    values = jobStr.split(",")
    cur.execute(QUERY_SQL, (values[4], values[0], values[1], values[3]))
    records = cur.fetchall()
    rowcount = 0
    for row in records:
        rowcount = row[0]
        # print("find duplicate ", str(rowcount), )
    if rowcount == 0:
        print(
            "do insert ",
            values[0],
            values[1],
            values[2],
            values[3],
            values[4],
        )
        cur.execute(
            INSERT_SQL, (values[0], values[1], values[2], values[3], values[4], "")
        )
        return 1
    return 0
