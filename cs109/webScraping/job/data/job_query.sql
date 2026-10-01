select tags, title, /*city,*/ company, /*city,*/ pub_date, /*add_time,*/ link from jobs j
where 1=1
and lower(title||link) ~* '.*(java|kotlin|scala|spring|jvm).*'
and not city ~* '.*(Sweden|Malm).*'
and not lower(tags)  ~* '.*(expired|applied|ignore).*'
and date_trunc('milliseconds', add_time) > '2026-06-15 00:00:00.000'::timestamp
and pub_date >= '2026-06-15'
order by pub_date desc;

select * from jobs
where 1=1
and lower(title) like '%it lead%'
and date_trunc('milliseconds', add_time) > '2026-09-04 00:00:00.000'::timestamp;

select count(*) from jobs;

select tags, title, /*city,*/ jobs.company, /*labels,*/ pub_date, /*add_time,*/ link from jobs
-- LEFT JOIN company ON jobs.company = company.company
where 1=1
--and j.company = c.company
and not TAGS ~* '.*(applied|ignore).*'
and not city ~* '.*(Sweden|Malm).*'

and not lower(title) ~* '.*(representative|volunteer|construction|kontor|logistik|fraud|projekt|træner|jura|freelance|assistent|operatør|kunde|cabin crew|butik|sælger|coordinator|salgs|senior manager|banker|based in luxembourg|bangkok|start|trader|ios|phd|rådgiver|country manager|support|mechanical|electrical|electronic|legal|business dev|project manager|ingeniør|associate|planner|assistant|designer|controller|embedded|infrastr|mobile|junior|stude|director|research|intern|graduate|trainee|account|hardware|partner|product manager|customer).*'
-- and not lower(title) ~* '.*(junior|maternity|contract|part-time|konsulent|graduate|intern|trainee|volunteer|studie|assistent|assistant|laborant).*'
--and not lower(title) ~* '.*(legal counsel|account manager|accountant|banker|representative|construction|logistik|fraud|træner|trainee|operatør|support).*'
--and not lower(title) ~* '.*(phd|bangkok).*'
--and not lower(title) ~* '.*(full).*'
and not lower(title) ~* '.*(halfspace).*'

-- DevOps
-- and not lower(title||link) ~* '.*(platform|security|network|cloud|scada|automation).*'
--and not lower(title) ~* '.*(network|design|full stack|security).*'


-- Tech
-- and lower(title) ~* '.*(python|golang|rust|c#|\.net|c\+\+|javascript|node|typescript).*'
-- and lower(title||link) ~* '.*(java|kotlin|scala|spring|jvm).*'
--and not lower(title||link) ~* '.*(c#|.net).*'
--and lower(title) ~* '.*(java|python|golang|rust|c#|csharp|script|back).*'
 and not lower(title) ~* '.*(sap |microsoft |ios|dynamics 365|D365).*'
 and not title ~* '.*(APL).*'
 and not lower(title) ~* '.*(quantum).*'
 -- and not lower(title) ~* '.*(embedded).*'
  and not lower(title) ~* '.*(full.?stack|ui |front.end).*'
  -- and not lower(title) ~* '.*(node.js).*'
 and not lower(title) ~* '.*(security|iam).*'
-- and not lower(title) ~* '.*(devops).*'

-- AI
-- and not title ~* '.*(AI|RAG|ML|Machine Learning|Artificial Intelligence|LLM|Agent).*'
--and not lower(title) ~* '.*(artificial intelligence).*'
-- and not (title ~ '.*(AI|ML|LLM|Agent).*' or lower(title) ~* '.*(machine learning).*')
--and not title ~* '.*(AI|ML|Machine Learning|Artificial Intelligence).*'

-- Data
 and not lower(title) ~* '.*(data scien|statistic).*'
-- and not lower(title) ~* '.*(data engineer).*'
--and not lower(title) ~* '.*(analytic).*'
--and not lower(title) ~* '.*(analyst|data engineer|data scien|senior manager|officer).*'
and not lower(title) ~* '.*(data engineer|scientist).*'
--and not lower(title) ~* '.*(scientist|data.*engineer).*'
--and not lower(title) ~* '.*(data|bi ).*'

-- infra
and not lower(title) ~* '.*(infrastr|platform).*'

-- product
and not lower(title) ~* '.*product.*(manager|owner|designer|engineer).*'

-- Other Position
 and not lower(title) ~* '.*(phd|postdoc|researcher|research scientist).*'
and not lower(title) ~* '.*(relationship|account|audit) (manager|executive).*'


and not lower(title) ~* '.*(consult|analyst|specialist|scientist).*'
and not lower(title) ~* '.*(trader|quant).*'
and not  lower(title) ~* '.*(forward deployed).*'
/*

 and not lower(title) ~* '.*(sælger|consult|analyst|specialist|controller|officer|researcher|coordinator|represent|auditor).*'

 and not lower(title) ~* '.*(partner).*'



and not lower(title) ~* '.*(auditor).*'
and not lower(title) ~* '.*(projektleder|hardware|network|security|trader|partner|account|designer|rådgiver|associate|advisor|analyst|analytiker|consul|counsel|owner|strategist|koordinator).*'
and not lower(title)  ~* '.*(mechanical|vvs).*'
*/

-- Consultant

-- Developer

-- Developer, Engineer
-- and lower(title) ~* '.*(develop|engineer|program|udvik).*'
-- AND NOT lower(title) ~* '.*(manager).*'
--and lower(title) ~* '^(?!.*manager).*(engineer|develop|program|udvik).*$'

-- Lead
  /*
and not lower(title) ~* '.*(archi|arkitekt).*'
and not lower(title) ~* '.*(lead|principal|cloud|data center).*(archi|arkitekt).*'
and not (lower(title) ~* '.*(afdelingschef|director|manager|head|lead).*' and not lower(title) ~* '.*(engineer|developer).*')

   */
--and not (lower(title) ~* '.*(archi|arkitekt|lead|manager|head|director|leder|president).*' and not lower(title) ~* '.*(engineer|developer).*')


and not lower(title) ~* '.*(mainframe|devops|platform engineer).*'
and not lower(title) ~* '.*(admini).*'
/*

-- danish
and not lower(title) ~* '.*(æ|ø|å).*'

 */

and lower(jobs.company) in (select lower(company) from company where (lower(labels) ~* '.*(fin|selected|ai).*' or lower(company) ~* '.*(ai |\.ai| ai).*'))
and not lower(jobs.company) in (select lower(company) from company where lower(labels) ~* '.*(retai|ignore|gov).*')
-- and not lower(jobs.company) ~* '.*(salling group|jem & fix|joe & the juice|politi|kommune|forsvarets).*'
-- recent
and not lower(jobs.company) ~* '.*(keyrock|corti|twoday|dalux|flatpay|festina).*'
and not lower(jobs.company) ~* '.*(emagine).*'
-- game
and not lower(jobs.company) ~* '.*(playdead|sybo|triband|unity).*'

--and not lower(company) ~* '.*(bairesdev|systematic).*'
--and not lower(company) ~* '.*(systematic|finalto|festina|banking circle).*'
-- and not lower(company) ~* '.*(ashby|staff|hays|flatpay|human resou|superbrugsen|psykiatrisk|forsvaret|hospital|lidl danmark|netto|365discount|kommune|normal a/s|politi|zara|røde kors|power a/s|red cross).*'
 -- and company not in (select company from company where labels like '%ignore%')
--and not lower(company) in (select lower(company) from company where lower(labels) ~* '.*(retail|health).*')

and date_trunc('milliseconds', jobs.add_time) > '2026-09-01 00:00:00.000'::timestamp
and pub_date >= '2026-09-01'
and jobs.add_time is not null
and (title, jobs.company, pub_date, jobs.add_time) in (select jobs.title, jobs.company, max(jobs.pub_date), max(jobs.add_time) from jobs group by title, company)
--order by company, title, pub_date desc

order by company, pub_date desc
-- order by pub_date desc
;

select tags, title, /*city,*/ company, pub_date, /*add_time,*/ link from jobs j
where 1=1
and not TAGS ~* '.*(applied|ignore).*'
and not city ~* '.*(Sweden|Malm).*'
and lower(title) ~* '.*(archi|arkitekt|lead|manager|head|director|leder|president).*'
and lower(company) in (select lower(company) from company where (lower(labels) ~* '.*(fin|selected|ai).*' or company ~* '.*(.ai).*'))
and date_trunc('milliseconds', add_time) > '2026-08-03 00:00:00.000'::timestamp
and pub_date >= '2026-08-03'
and add_time is not null
and (title, company, pub_date, add_time) in (select jobs.title, jobs.company, max(jobs.pub_date), max(jobs.add_time) from jobs group by title, company)
--order by company, title, pub_date desc
 order by company, pub_date desc
;


insert into company (company, labels, add_time) values ('Lån & Spar Bank', 'Fin', null);
--order by company, j.pub_date desc;

select tags, title, /*city,*/ company, pub_date, add_time, link from jobs
where 1=1
--and lower(company) like '%alm%'
--and lower(company) like '%pleo%'
--and lower(company) not in (select lower(company) from company)
and not lower(city) ~* '.*(sweden|malm).*'
and not lower(tags) ~* '.*(applied|ignore|expired).*'
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