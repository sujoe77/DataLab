import datetime as DT
import urllib.parse
from datetime import datetime
from zoneinfo import ZoneInfo

from jobs import Job
from util.IOUtil import get_content_coolshell


class coolshell(Job):
    def __init__(self, exclude_title, exclude_company):
        self.exclude_title = exclude_title
        self.exclude_company = exclude_company

    def parse(self, page_content):
        print("start to parse!")
        result = []
        # li = page_content.find_all("li", "result-card job-result-card result-card--with-hover-state")
        entry_headers = page_content.find_all("header", "entry-header")
        divSize = len(entry_headers)
        print("divSize: " + str(divSize))
        # print(divSize)
        for i in range(0, divSize):
            #print("Processing entry " + entry_headers[i].span("screen-reader-text"))
            title = entry_headers[i].span.text
            #print("title: " + title)
            #if len(titleList) == 0:
            #    continue
            link = entry_headers[i].a["href"].replace("https://web.archive.org/web/20251202192107/", "")
            #print("link: " + link)
            # print(li[i].div)
            #title = self.get_title(entry_headers, i)
            read = self.get_read(entry_headers, i)
            read_str = "".join(read).strip().replace(",", "").replace(" 人阅读", "")
            #print("read: " + read_str)
            pubdate = self.get_time(entry_headers, i)
            #print("pubdate: " + pubdate)
            #location = self.get_location(entry_headers, i)
            #if (
            #    "month" not in time
            #    and super().ex_filter(title, self.exclude_title)
            #    and super().ex_filter(company, self.exclude_company)
            #):
                # if "month" not in time:
            text = f"{title},{pubdate},{read_str},{link}\n"
            print("\t" + text)
            result.append(text)
        return result

    def get_read(self, entry_headers, i):
        return entry_headers[i].div.h5.find_all(string=True, recursive=False)
        #time = timeList[0].text.replace("\n", "").lstrip().rstrip().replace(",", "_")
        #time = self.getPubDate(time)
        # print(time.text.replace("\n", "").lstrip().rstrip())
        #return time

    def get_location(self, li, i):
        locationList = li[i].find_all("span", "job-search-card__location")
        location = (
            locationList[0].text.replace("\n", "").lstrip().rstrip().replace(",", "_")
        )
        # print(location)
        return location

    def get_title(self, li, i):
        titleList = li[i].find_all("span", "sr-only")
        title = titleList[0].text.replace("\n", "").lstrip().rstrip().replace(",", "_")
        # print(title)
        return title

    def get_time(self, entry_headers, i):
        return entry_headers[i].div.h5.a.time.text.strip().replace("年","-").replace("月","-").replace("日","")

    def get_url(self, keyword, pageNum):
        # url = "https://www.linkedin.com/jobs/search/?keywords="+keyword+"&location=copenhagen%20denmark&start=" + str(pageNum*25)
        url = "https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords={keyword}&location={location}&start={start}"
        url = "https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords={keyword}&start={start}&geoId=102194656"
        url = "https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?distance=40&f_TPR=a1769632530-&f_WT=1%2C3&geoId=102194656&keywords={keyword}&origin=JOB_SEARCH_PAGE_SEARCH_BUTTON&start={start}"
        url = url.format(
            keyword=urllib.parse.quote(keyword, safe=""),
            location="copenhagen",
            start=pageNum * 10,
        )
        return url

    def getPubDate(self, timeStr):
        today = datetime.now(ZoneInfo("Europe/Copenhagen")).date()

        # dd/mm/YY
        # d1 = today.strftime("%Y-%m-%d")
        # print("d1 =", d1)

        time = timeStr.split()
        delta = int(time[0])
        unit = time[1]
        if unit.startswith("day"):
            delta = delta * 24
        elif unit.startswith("week"):
            delta = delta * 24 * 7

        pub_date = today - DT.timedelta(hours=delta)
        return pub_date.strftime("%Y-%m-%d")

    def process_page(self, url):
        print("\nfeatching url: " + url)
        page_content = get_content_coolshell(url)
        return self.process_page_content(page_content)

    def process_page_content(self, page_content):
            #print(page_content)
            return self.parse(page_content)

    def get_next_url(self, url, page_content):
        #https://web.archive.org/web/20251202192428/https://coolshell.cn/category/technews/page/2
        firstPage = url.endswith("/")
        nextPage = 2
        if not firstPage:
            nextPage = int(url.split("/")[-1]) + 1

        end_with = url[url.rfind("category"):]
        if "page/" in end_with:
            end_with = end_with[:end_with.rfind("page/")]
        page_links = page_content.find_all("div", "wp-pagenavi")[0].find_all("a")
        print(page_content)
        for i in range(len(page_links)):
            href = page_links[i]["href"]
            if href.endswith(end_with + "page/"+ str(nextPage)):
                return href