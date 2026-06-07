select tags, title, /*city,*/ company, pub_date, add_time, link from jobs j
where 1=1
and not TAGS ~* '.*(applied|ignore).*'
and not city ~* '.*(Sweden|Malm).*'

--and not lower(title) ~* '.*(hauffør|construction|kontor|logistik|fraud|projekt|træner|jura|freelance|assistent|operatør|kunde|cabin crew|butik|sælger|coordinator|salgs|senior manager|banker|based in luxembourg|bangkok|start|trader|ios|phd|rådgiver|country manager|support|mechanical|electrical|electronic|legal|business dev|project manager|ingeniør|associate|planner|assistant|designer|controller|embedded|infrastr|mobile|junior|stude|director|research|intern|graduate|trainee|account|hardware|partner|product manager|customer).*'
--and not lower(title) ~* '.*(contract|part-time|studiejob|konsulent|graduate).*'
--and not lower(title) ~* '.*(speaking|søger).*'

--and not lower(title) ~* '^(?!.*manager).*(engineer|develop|program|udvik).*$'
--and not lower(title) ~* '.*(advisor|analyst|analytiker|specialist|officer|consul|scientist|owner|strategist|koordinator|speculative).*'
--and not lower(title) ~* '.*(archi|lead|manager|head|director|leder|president).*' and not lower(title) ~* '.*engineer'

-- and lower(title) ~* '.*(develop|engineer|program|udvik).*'
-- AND NOT lower(title) ~* '.*(manager).*'

--and not lower(title) ~* '.*(consult|specialist).*'

-- and lower(title) ~* '.*(java|kotlin|scala).*'
-- and lower(title) ~* '.*(python|golang|rust|c#|\.net|c\+\+|javascript|node|typescript).*'
--and not lower(title) ~* '.*(scientist|data.*engineer).*'
--and not lower(title) ~* '.*(data|bi ).*'

--and not lower(title) ~* '.*(sap |microsoft ).*'

--and not lower(title) ~* '.*(security|iam).*'
--and not lower(title) ~* '.*(devops|platform engineer).*'
--and not lower(title) ~* '.*(full|ui |front.*end).*'

--and not title ~* '.*(AI|ML|Machine Learning|Artificial Intelligence).*'
--and lower(title) ~* '.*(java|python|golang|rust|c#|csharp|script|back).*'

--and not lower(title) ~* '.*(analyst|data engineer|data scien|senior manager|officer).*'

and lower(company) in (select lower(company) from company where lower(labels) ~* '.*(fin|selected).*')
-- and not lower(company) ~* '.*(systematic).*'
and not lower(company) ~* '.*(ashby|staff|hays|flatpay|human resou|superbrugsen|psykiatrisk|forsvaret|hospital|lidl danmark|netto|365discount|kommune|normal a/s|politi|zara|røde kors|power a/s|red cross).*'
and company not in (select company from company where labels like '%ignore%')
--and not lower(company) in (select lower(company) from company where lower(labels) ~* '.*(retail|health).*')

and date_trunc('milliseconds', add_time) > '2026-05-10 00:00:00.000'::timestamp
and pub_date > '2026-05-10'
and add_time is not null
and (title, company, pub_date, add_time) in (select jobs.title, jobs.company, max(jobs.pub_date), max(jobs.add_time) from jobs group by title, company)
--order by company, title, pub_date desc
-- order by company, pub_date desc
order by pub_date desc
;

insert into company (company, labels, add_time) values ('Lån & Spar Bank', 'Fin', null);
--order by company, j.pub_date desc;

select tags, title, /*city,*/ company, pub_date, add_time, link from jobs
where 1=1
--and lower(company) like '%alm%'
--and lower(company) like '%pleo%'
--and lower(company) not in (select lower(company) from company)
and not lower(city) ~* '.*(sweden|malm).*'
and not lower(tags) ~* '.*(applied|ignore).*'
--and lower(tags) ~* '.*(applied).*'
and lower(title) like '%java%'
and add_time is not null
order by company, add_time desc        ;

select count(*) from jobs;

--select distinct labels from company
--order by labels;

select * from company
where 1=1
--and labels is null
--and lower(company) like '%rsted%'
--and lower(labels) like '%fin%'

--and lower(company) like '%saab%'
order by company;