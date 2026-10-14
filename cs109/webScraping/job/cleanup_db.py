from datetime import date, timedelta

import psycopg


def get_archive_sql(earliest_day):
    sql = f"""
                insert into jobs_old (title, company, city, pub_date, link, tags, add_time)
                select title, company, city, pub_date, link, tags, add_time
                from jobs
                where 1 = 1
                    and (date_trunc('milliseconds', jobs.add_time) < '{earliest_day} 00:00:00.000'::timestamp
                    or  jobs.pub_date < '{earliest_day}' or jobs.add_time is null)
            """
    return sql


def get_delete_sql(earliest_day):
    # Subtract 31 days from today's date
    sql = f"""
                delete from jobs
                where 1 = 1
                    and (date_trunc('milliseconds', jobs.add_time) < '{earliest_day} 00:00:00.000'::timestamp
                    or  jobs.pub_date < '{earliest_day}' or jobs.add_time is null)
            """
    return sql


def archive_old_jobs(earliest_day, do_commit=False):
    sql = get_archive_sql(earliest_day)

    #print(sql)

    conn = psycopg.connect("dbname=mydb user=postgres password=postgres host=localhost")
    try:
        cur = conn.cursor()
        cur.execute(sql)
        rowcount = cur.rowcount
        if do_commit:
            conn.commit()
        cur.close()
        print(f"archived {rowcount} old jobs successfully, commit: {do_commit}")
        return True
    except psycopg.DatabaseError as error:
        print(error)
        return False
    finally:
        if conn is not None:
            conn.close()


def delete_old_jobs(earliest_day, do_commit=False):
    sql = get_delete_sql(earliest_day)

    #print(sql)

    conn = psycopg.connect("dbname=mydb user=postgres password=postgres host=localhost")
    try:
        cur = conn.cursor()
        cur.execute(sql)
        rows_affected = cur.rowcount
        if do_commit:
            conn.commit()
        cur.close()
        print(f"deleted {rows_affected} old jobs successfully, commit: {do_commit}")
        return True
    except psycopg.DatabaseError as error:
        print(error)
        return False
    finally:
        if conn is not None:
            conn.close()


if __name__ == "__main__":
    days_to_keep = 31
    earliest_day = (date.today() - timedelta(days=days_to_keep)).strftime("%Y-%m-%d")
    print(f"Archiving and deleting jobs older than {earliest_day} (keeping last {days_to_keep} days)")
    if archive_old_jobs(earliest_day, True):
        if not delete_old_jobs(earliest_day, True):
            print("failed to delete old jobs")
    else:
        print("failed to archive old jobs")
