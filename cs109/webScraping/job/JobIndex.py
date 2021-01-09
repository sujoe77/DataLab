from datetime import datetime

from job import Job


class JobIndexJob(Job):
    KEYWORD_LIST=["Java"]
    EXECLUDE_TITLE = ["frontend", "c#", "udvikler", "android", "analyst", "devops", "security", "sale", "Javascript", "QA",".NET","javascript","microsoft","php"]
    EXECLUDE_COMPANY = ["dfds", "prodata", "Systematic","test"]


    def parse(self, page_content):
        result = []        
        div_title = page_content.find_all("div", "PaidJob")
        
        for i in range(0, len(div_title)):
            tag = self.getTag(div_title, i)
            link, title = self.getLinkTitle(tag)

            company = div_title[i].p.a.b.text.replace(",", "_").replace("\n", " ").replace("\r", " ").strip()
            location = self.getLocation(div_title, i)
            time = datetime.now().strftime("%Y-%m-%d")
            if "month" not in time and super().ex_filter(title, JobIndexJob.EXECLUDE_TITLE) and super().ex_filter(company, JobIndexJob.EXECLUDE_COMPANY):
                text = "{},{},{},{},##{}".format(title, company, location, time, link);
                #print(text)
                result.append(text)
        return result

    def getTag(self, div_title, i):
        # print(div_title[i])
        j = 2
        while "href" not in str(div_title[i].contents[j]):
            print("j is %d" % j)
            j += 1
        tag = div_title[i].contents[j]
        # print("tag is: [%s]" % str(tag))
        return tag

    def getLinkTitle(self, tag):
        if "<p>" in str(tag):
            link = tag.a["href"]
            title = tag.a.b.text.replace("\n", " ").strip().replace(",", "_")
        else:
            link = tag["href"]
            title = tag.b.text.replace("\n", " ").strip().replace(",", "_")
        return link, title

    def getLocation(self, div_title, i):
        location = div_title[i].p.text.replace(",", "_").replace("\n", " ").replace("\r", " ").strip()
        if "_" in location:
            location = location[location.index("_") + 1:].strip()
        else:
            location = "_"
        return location

    def get_url(self, keyword, pageNum):
        return "https://www.jobindex.dk/jobsoegning/it/systemudvikling/storkoebenhavn?q="+keyword+"&page=" + str(pageNum+1)

