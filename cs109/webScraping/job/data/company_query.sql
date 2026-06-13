select substr(jobs.title, 2)
from jobs
where title LIKE chr(9)||'%';

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
where company.company in ('Hooked - Seafood Kitchen')
--where add_time is not null
order by add_time desc;

select company from company where labels like '%ignore%';

select * from company
where lower(company.company) ~* '.*(ostnord).*';
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