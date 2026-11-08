import time

from coolshell import *

ts = "20251202192447"
url="https://web.archive.org/web/"+ ts+ "/https://coolshell.cn/"

cs = coolshell([], [])

results = []
offset = 58
step = 20

url_tags: dict = {}

def read_categories(file_path):
    categories = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            fields = line.split(",")
            category_count = fields[0] + "," + fields[2]
            if line:
                categories.append(category_count)
    return categories

def generate_full_list(url_tags, lines):
    for line in lines:
        line = line.strip()
        if not line:
            continue
        fields = line.split(",")
        if len(fields) < 4:
            print(f"Skipping malformed line: {line}")
            continue
        url = fields[3].strip()
        page = get_page(url)
        if page in url_tags:
            category_name = url_tags[page]
            new_line = f"{line},{category_name}\n"
            results.append(new_line)
        else:
            print(f"URL not found in tags: {url}")

    final_file_path = "data/coolshell/final_list.txt"
    with open(final_file_path, "w", encoding="utf-8") as f:
        f.writelines(results)

    return results

def get_page(url):
    last_slash = url.rfind('/')
    page = url[last_slash:]
    return page

if __name__ == '__main__':
    category_count = read_categories("data/coolshell/categories_tmp.txt")
    for category in category_count:
        category_name, count = category.split(",")
        count = int(count)
        print(f"Processing category: {category_name}, Count: {count}")
        step = count / 10
        for s in range(int(step+1)):
            #page_url = f"https://web.archive.org/web/20251202202415/https://coolshell.cn/category/proglanguage/webdev/page/2"
            page = f"page/{s+1}"
            if s == 0:
                page = ""
            page_url = f"https://web.archive.org/web/20251202202415/https://coolshell.cn/category/{category_name}/{page}"
            print(f"Fetching URL: {page_url}")
            articles = cs.process_page(page_url)
            for article in articles:
                url = article.split(",")[-1].strip()
                page = get_page(url)
                if page not in url_tags:
                    url_tags[page] = category_name
                else:
                    url_tags[page] += f"|{category_name}"
            time.sleep(3)  # Be polite and avoid hammering the server

        print(f"Finished processing category: {category_name}. Total articles found: {len(articles)}")

        if len(url_tags) > 0:
            with open("data/coolshell/url_tags.txt", "w", encoding="utf-8") as f:
                for url, tags in url_tags.items():
                    f.write(f"{url},{tags}\n")
            print(f"URL tags written to data/coolshell/url_tags.txt")

    print("all done!")

    f = open("data/coolshell/sorted_all.txt", "r")
    lines = f.readlines()
    f.close()

    generate_full_list(url_tags, lines)