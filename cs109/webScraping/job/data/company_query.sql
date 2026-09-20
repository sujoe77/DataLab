

select * from company where company in (select company
from jobs
where 1=1
and date_trunc('milliseconds', jobs.add_time) > '2026-05-01 00:00:00.000'::timestamp
group by company
having count(*) > 10)
and labels is null;
    --order by count desc;

select * from company where lower(labels) like '%ignore%';

select * from jobs
where lower(title) ~* '.*(kotlin|java|scala).*'
and not lower(city) ~* '.*(sweden|malmö).*'
and not lower(tags) ~* '.*(applied|ignore).*'
order by pub_date desc;


update jobs
set title = substr(jobs.title, 2)
where title LIKE chr(9)||'%';


select * from jobs
where add_time is not null
AND title like '%java%'
order by add_time desc
;

select * from company
where labels like '%ignore%';

select * from company
where company.company in ('Infosys')
--where add_time is not null
order by add_time desc;

select company from company where labels like '%ignore%';

select * from company
where lower(company.company) ~* '.*(chip).*';
--where lower(labels) ~* '.*(internet|it).*
-- ';

ALTER TABLE company
ADD description VARCHAR(255);

select distinct company
from jobs where company not in (select company from company);

INSERT INTO company (company, add_time)
SELECT distinct company, now()
FROM jobs
WHERE company not in (select company from company);