import pandas as pd
from bs4 import BeautifulSoup
import requests
from time import sleep
import datetime

def clean_string(column):
    return column.apply(lambda x: x.replace("\n",'',2)).apply(lambda x: x.replace('  ',''))

def scrape_reviews(PATH, n_pages, sleep_time = 0.3):


    names = []
    ratings = []
    headers = []
    reviews = []
    dates = []
    locations = []

    for p in range(n_pages):

        sleep(sleep_time)

        #http = requests.get(f'{PATH}{p}&stars=1&stars=5')
        path1 = f'{PATH}{p+1}&stars=1'
        print(path1)
        http = requests.get(path1)
        bsoup = BeautifulSoup(http.text, 'html.parser')
        
        review_containers = bsoup.find_all('div', class_ = 'review-content__body')
        user_containers = bsoup.find_all('div', class_ = 'consumer-information__name')
        rating_container = bsoup.find_all('div',class_ = "review-content-header")
        date_container = bsoup.find_all('div',class_ = "review-content-header__dates")
        profile_link_containers = bsoup.find_all('aside', class_ = 'review__consumer-information' )
        
        print(len(review_containers))

        for x in range(len(review_containers)):

            review_c = review_containers[x]
            headers.append(review_c.h2.a.text)
            reviews.append(review_c.p.text)
            reviewer = user_containers[x]
            names.append(reviewer.text)
            rating = rating_container[x]
            ratings.append(rating.div.attrs['class'][1][12])
            date = date_container[x].script.text
            dates.append(datetime.datetime.strptime(date[19:29], '%Y-%m-%d').date())


            prof = profile_link_containers[x]
            link = 'https://www.trustpilot.com'+ prof.a['href']
            c_profile = requests.get(f'{link}')
            csoup = BeautifulSoup(c_profile.text, 'html.parser')
            cust_container = csoup.find('div', class_ = 'user-summary-location')
            locations.append(cust_container.text)
            
    rev_df = pd.DataFrame(list(zip(names, headers, reviews, ratings, dates, locations)),
                  columns = ['Name','Header','Review','Rating', 'Date', 'Location'])
    
    rev_df.Review = clean_string(rev_df.Review)
    rev_df.Name = clean_string(rev_df.Name)
    rev_df.Location = clean_string(rev_df.Location)
    rev_df.Location = rev_df.Location.apply(lambda x: x.split(',',1)[-1])
    rev_df.Rating = rev_df.Rating.astype('int')
    rev_df.Date = pd.to_datetime(rev_df.Date)
    
    return rev_df