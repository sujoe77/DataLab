select count(*) from jobs_old;

select count(*) from jobs ;
select * from jobs order by add_time ;

select
from jobs
where 1 = 1
  and (date_trunc('milliseconds', jobs.add_time) < '2026-09-01 00:00:00.000'::timestamp
    or jobs.pub_date < '2026-09-01'
    or jobs.add_time is null)
;

select count(*) from jobs;

select * from jobs order by add_time;

SELECT * INTO TABLE jobs_old
FROM jobs
where 1 = 1
  and (date_trunc('milliseconds', jobs.add_time) < '2026-09-01 00:00:00.000'::timestamp
    or date_trunc('milliseconds', jobs.pub_date) < '2026-09-01'
    or jobs.add_time is null)
  and jobs.add_time is null;

insert into jobs_old (title, company, city, pub_date, link, tags, add_time)
select title, company, city, pub_date, link, tags, add_time
    from jobs
where 1 = 1
  and (date_trunc('milliseconds', jobs.add_time) < '2026-09-01 00:00:00.000'::timestamp
    or  jobs.pub_date < '2026-09-01' or jobs.add_time is null);


delete from jobs_old where 1=1;