select * from company;

create table jobs (
	title text,
	company text,
	city text,
	pub_date text,
	link text,
	tags text
)

create table resources (
	format text,
	keywords text,
	path text
)

select * from jobs
where 1=1
 and jobs.tags like '%appli%'
order by pub_date desc
;


select
-- * 
 company, count(*)
from jobs
where 1=1
--and link like '%stackover%'
and company not in (select company from company)
--and pub_date not like '202%'
--and company='Danmarks Tekniske Universitet'
and (not  city ~*  '.*(Arden|United States|Skjern|Kolding|Kalundborg|mal|aarhus|Billund|Hørsholm|Esbjerg|sweden|kingdom|roskilde|Odense|Aalborg|Skensved|Struer|Herning|Tønder|ylland|Naestved|Holstebro|Galten|Viborg|Tilst|Vejle).*'  or  title ~*  '.*(remote).*' )
group by company
order by count(*) desc
;

select * from company c
where company like '%HOFOR%';

select jobs.company, count(*), labels
from jobs left join company on jobs.company = company.company
where jobs.company not in (select company from company)
and (not  city ~*  '.*(Arden|United States|Skjern|Kolding|Kalundborg|mal|aarhus|Billund|Hørsholm|Esbjerg|sweden|kingdom|roskilde|Odense|Aalborg|Skensved|Struer|Herning|Tønder|ylland|Naestved|Holstebro|Galten|Viborg|Tilst|Vejle).*'  or  title ~*  '.*(remote).*' )
group by jobs.company, labels
order by company desc;

select * from company c;

select *
 from jobs left  join company
 on  jobs.company = company.company
where 1=1
-- and jobs.company like '%itach%'
 and  not title  ~*  '.*(controller|Web Developer|Quality|Analytiker|planner|director|Restaurant|jutland|danish|Mechanical|quanlification|Scrum master|hardware|projekt|gis|dev ops|contract|support|ingeniør|quality assurance|mule|data center|devops|365|electrical|berlin|cloud engineer|surveyor|trainee|coordinator|student|data center|arbejde|søger|udvik|arkitekt|vizual|så|konsulent|000|angular|assistant|graduate|network|designer|operation|shipping|construction|audio|sre|owner|test|policy|front|defence|intern|sap|nodejs|studie| erp |admin|embed|junior|ios|c-d|manager|print|på|kotlin|phd|ui).*'
 and not jobs.company ~*  '.*(Gavdi|greenlee|Fiftytwo|game|food|tamigo|visma|unicef|rina|Akademikernes|ministeriet|dsv|church|DCA|Municipality|ncc|TrackMan|Politikens|banking circle|pfa|Maquet|Endomondo|DIS A/S|Faunaphotonics|unity|Ramböll|Elastic|post office|Radiometer|game|Bjarke|mulesoft|deltek|Enghouse|Schneider|atp|Famly|Nordsense|Harnham|olufsen|ministry|styrels|talent|Peakon|IQVIA|Opvækst|ARKITEKTT|Nykredit|adobe|4C|universi|kommune|academic|unops|netsuite|mercell|GAN Integrity|glaze|avance|aerosp|Total|issuu|karnov|3Shape|SOUNDBOKS|globesearch|erhvervsa|lego|Too Good To Go|Netcompany|danish|sap|epsn|dsb|appen|Duunitori|blockchain|dtu|energ|school).*'
 and (not  city ~*  '.*(Arden|United States|Skjern|Kolding|Kalundborg|mal|aarhus|Billund|Hørsholm|Esbjerg|sweden|kingdom|roskilde|Odense|Aalborg|Skensved|Struer|Herning|Tønder|ylland|Naestved|Holstebro|Galten|Viborg|Tilst|Vejle).*'  or  title ~*  '.*(remote).*' )
and (not city  ~  '.*_ [A-Z]{2}'  or  title ~*  '.*(remote).*')--USA
-- and not labels ~*  '.*(hr).*'
-- and pub_date like '2022%'
--and (TO_DATE(pub_date,'YYYY-MM-DD') > now() - interval '21 days')
--and pub_date not like '20%'
--and labels like '%Fin%'
--and jobs.company like '%orde%'
order by pub_date desc;

select --*
tags, title, jobs.company, company.labels,  city, pub_date, link
-- substring(lower(title), '.*(dev ops|contract|support|ingeniør|quality assurance|mule|data center|devops|365|electrical|berlin|full|cloud engineer|surveyor|trainee|coordinator|student|data center|arbejde|søger|udvik|arkitekt|vizual|så|konsulent|000|angular|assistant|graduate|network|designer|operation|shipping|construction|audio|sre|owner|test|policy|front|defence|intern|sap|nodejs|studie| erp |admin|embed|junior|ios|c-d|manager|print|på|kotlin|phd|ui).*') kw, 
 --distinct company
 from jobs left  join company
 on  jobs.company = company.company
where 1=1
--and title ~*  '.*(?i)Developer(?-i).*'
--and title ~*  '.*(java).*' 
and (not  city ~*  '.*(Aarhus|Arden|United States|Skjern|Kolding|Kalundborg|mal|aarhus|Billund|Hørsholm|Esbjerg|sweden|kingdom|roskilde|Odense|Aalborg|Skensved|Struer|Herning|Tønder|ylland|Naestved|Holstebro|Galten|Viborg|Tilst|Vejle).*'  or  title ~*  '.*(remote).*' )
and (not city  ~  '.*_ [A-Z]{2}'  or  title ~*  '.*(remote).*') --USA
and not tags ~*  '.*(ignore|appli).*'
and  not title  ~*  '.*(node.js|mobile developer|mainframe|ux|Wordpress|automation|controller|Web Developer|Quality|Analytiker|planner|director|Restaurant|jutland|danish|Mechanical|quanlification|Scrum master|hardware|projekt|gis|dev ops|contract|support|ingeniør|quality assurance|mule|data center|devops|365|electrical|berlin|cloud engineer|surveyor|trainee|coordinator|student|data center|arbejde|søger|udvik|arkitekt|vizual|så|konsulent|000|angular|assistant|graduate|network|designer|operation|shipping|construction|audio|sre|owner|test|policy|front|defence|intern|sap|nodejs|studie| erp |admin|embed|junior|ios|c-d|manager|print|på|phd|ui).*'
and not title ~*  '.*(learning|scien|consul).*' 
and  title ~*  '.*(java|engine|devel|archi|progra).*' 
--and not title ~*  '.*(ai|machine|python|data en|scientist|full|dataops).*' -- developer 23 
-- and  title ~*  '.*(archit).*'  and not jobs.company  ~*  '.*(Microsoft|Oracle|amazon|Salesforce).*' and not title ~*  '.*(data|analytic).*' -- architect 17
 --and  title ~*  '.*(analytic|data|ai|machine|python).*'  -- and  not  title ~*  '.*(head|chief|architect|senior|lead).*' -- and  not title ~*  '.*(scientist).*'-- data 22
-- and jobs.company = 'Penni.io'
and not jobs.company ~*  '.*(accenture).*' -- temp exclude
and not jobs.company ~*  '.*(Gavdi|greenlee|Fiftytwo|game|food|tamigo|visma|unicef|rina|Akademikernes|ministeriet|dsv|church|DCA|Municipality|ncc|TrackMan|Politikens|banking circle|pfa|Maquet|Endomondo|DIS A/S|Faunaphotonics|unity|Ramböll|Elastic|post office|Radiometer|game|Bjarke|mulesoft|deltek|Enghouse|Schneider|atp|Famly|Nordsense|Harnham|olufsen|ministry|styrels|talent|Peakon|IQVIA|Opvækst|ARKITEKTT|Nykredit|adobe|4C|universi|kommune|academic|unops|netsuite|mercell|GAN Integrity|glaze|avance|aerosp|Total|issuu|karnov|3Shape|SOUNDBOKS|globesearch|erhvervsa|lego|Too Good To Go|Netcompany|danish|sap|epsn|dsb|appen|Duunitori|blockchain|dtu|energ|school).*'
and not jobs.company  ~*  '.*(hunt|job|Recruitio|bloom|Recruit|Nigel Frank|Capgemini|EPICO Search|consul|Casefair|EUROPEAN SEARCH COMPANY).*' -- head hunt
and (
jobs.company ~*  '.*(Keylane|alm|invest|pay|sdc|novo|uber|blackrock|Nordea|bank|Microsoft|google|amazon|Morningstar|invest|facebook|nets|NN|novo|ibm|intel|GitHub|Maersk|BEC|Tradeshift|Nasdaq|oracle|tryg|Simcorp|forsik|cisco|trade).*'   
--	and not jobs.company ~*  '.*(Lundbeck|penni.io).*' --top companies
	or  ( labels ~*  '.*(IT|Fin|software|AI|internet|VR|good|VC|nternet).*'  and  not labels ~*  '.*(Retail|Audit).*')
-- or title is not null
)-- good company
--  and jobs.company not in (select company from company)
and (not company.labels ~*  '.*(hr).*'  or labels is null)
and TO_DATE(pub_date,'YYYY-MM-DD') > now() - interval '21 days'
order by  labels, company, pub_date desc
;  

-- Data, Full Stack, Cloud, Architect

--  company, industry, company size, role, level

update jobs 
set tags = 'ignore-title'
where 1=1
--and title  like ('%Test%' )
and company like ('%Klint Marketing%')
--and city like '%Odense%'
--and tags = 'ignore-location'
;

ALTER TABLE jobs  ADD CONSTRAINT uni_link  UNIQUE (link);


