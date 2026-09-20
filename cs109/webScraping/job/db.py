import psycopg

from constants import IGNORE_SAME_POSITION_FOR_DAYS

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
QUERY_SQL = "select count(link) from jobs where link=%s or (title = %s and company = %s and (to_date(%s, 'YYYY-MM-DD') - to_date(pub_date, 'YYYY-MM-DD') < %s))"


def insert_job(jobSet, taskName):
    # """insert a new vendor into the vendors table"""
    # query_sql = "select count(link) from jobs where link=%s or (title = %s and company = %s) "
    # to_date(%s, 'YYYY-MM-DD') - to_date(pub_date, 'YYYY-MM-DD') < 30
    conn = psycopg.connect(
        # host="localhost", database="mydb", user="postgres", password="postgres"
        "dbname=mydb user=postgres password=postgres host=localhost"
    )
    ret = []
    try:
        cur = conn.cursor()
        print(taskName + " job set size is: " + str(len(jobSet)))
        for job in jobSet:
            if find_duplicates(cur, job.split(",")) == 0:
                insert_position(cur, job)
                ret.append(job)
        conn.commit()
        cur.close()
        print(
            taskName + " total insert: ",
            len(ret),
        )
        return ret
    except psycopg.DatabaseError as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def insert_position(cur, jobStr):
    values = jobStr.split(",")
    print(
        "\tdo insert ",
        values[0],
        values[1],
        values[2],
        values[3],
        values[4],
    )
    cur.execute(INSERT_SQL, (values[0], values[1], values[2], values[3], values[4], ""))


def find_duplicates(cur, values):
    cur.execute(
        QUERY_SQL,
        (values[4], values[0], values[1], values[3], IGNORE_SAME_POSITION_FOR_DAYS),
    )
    records = cur.fetchall()
    rowcount = 0
    for row in records:
        rowcount = row[0]
        # print("find duplicate ", str(rowcount), )
    return rowcount
