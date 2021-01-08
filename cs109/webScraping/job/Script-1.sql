create table jobs (
	title text,
	company text,
	city text,
	pub_date text,
	link text,
	tags text
)

select * from jobs
where 1=1
and city not like '%weden%'
and tags not like '%ignore%'
and tags not like '%ds%'
order by company desc;

select * from jobs
where pub_date not like '202%'
;


select tags, title, company, pub_date, link
from jobs
where company like '%BEC%'
;

select tags, title, company, city, pub_date, link 
from jobs 
where 1=1
--and title ~*  '.*(?i)Developer(?-i).*'
--and title ~*  '.*(java).*'
and not city ~*  '.*(mal|aarhus|Billund|Hørsholm|Esbjerg|sweden|kingdom|roskilde|Odense|Aalborg|Skensved).*'
and not company ~*  '.*(Bjarke|mulesoft|deltek|Enghouse|Schneider|atp|Famly|Nordsense|Harnham|olufsen|ministry|styrels|talent|Peakon|IQVIA|Opvækst|ARKITEKTT|Nykredit|adobe|4C|universi|kommune|academic|unops|zendesk|netsuite|mercell|GAN Integrity|glaze|avance|aerosp|Total|issuu|karnov|Shape|SOUNDBOKS|globesearch|erhvervsa|lego|Too Good To Go|Netcompany|danish|sap|epsn|dsb|appen|Duunitori|blockchain|dtu|energ|school).*'
and not title ~*  '.*(full|cloud engineer|Surveyor|trainee|coordinator|student|data center|arbejde|søger|Udvik|Arkitekt|vizual|så|konsulent|000|angular|assistant|master|graduate|network|designer|operation|shipping|construction|audio|sre|live|mobile|owner|test|policy|front|defence|intern|sap|nodejs|studie|erp|admin|app|embed|junior|ios|C-D|manager|print|på|kotlin|phd|office|ui).*'
and not tags ~*  '.*(ignore|appli).*'
--and not title ~*  '.*(learning|scien|consul|full).*' and not company ~*  '.*(accenture|bec).*' -- temp exclude
and  title ~*  '.*(engine|devel).*' and not title ~*  '.*(data).*' -- developer 23
--and  title ~*  '.*(archit).*'  -- architect 17
--and  title ~*  '.*(data|ai|machine).*' -- data 22
order by company;

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


