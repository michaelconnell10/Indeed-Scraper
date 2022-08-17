import requests
from bs4 import BeautifulSoup
import pandas as pd

def extract(page):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}
    url = f'https://www.indeed.com/jobs?q=data%20analyst&l=Texas&start={page}', 'https://www.indeed.com/jobs?q=data%20analyst&l=Georgia&start={page}'
    r = requests.get(url, headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    
    return soup

def transform(soup):
    divs = soup.find_all('div', class_ = 'jobCard_mainContent')
    
    for item in divs:
        title = item.find('a').text.strip()
        company = item.find('div', class_ = 'company_location').text.strip()
        summary = item.find('div', class_ = 'jobCardShelfContainer').text.strip().replace('\n', '')
        
        job = {
            'title': title,
            'company': company,
            'summary': summary
        }
        joblist.append(job)
    return
        
joblist = []


#### BECAUSE PAGES IN WEBSITE GO UP BY 10, HAVING TO DO 10 STEP FOR EVERY PAGE
for i in range(0,100,10):
    c = extract(0)
    transform(c)

df = pd.DataFrame(joblist)

df.to_csv('jobs.csv')