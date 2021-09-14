from bs4 import BeautifulSoup
import pandas as pd
import requests

def extract(page):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'}
    url = f'https://www.indeed.com/jobs?q=python%20developer&l=Minnesota&start={page}'
    r = requests.get(url, headers)
    soup = BeautifulSoup(r.content, 'lxml')
    return soup


def transform(soup):
    divs = soup.find_all('div', class_='slider_container')
    for item in divs:
        job_title = item.find('h2').find(class_=None).text
        company = item.find('span', class_='companyName').text
        try:
            salary = item.find('span', class_='salary-snippet').text
        except:
            salary = ''
        summary = item.find('div', class_='job-snippet').text.strip().replace('\n',' ')

        job = {
            'title': job_title,
            'company': company,
            'salary': salary,
            'summary': summary
        }
        joblist.append(job)
    return

joblist=[]
for page in range(0, 40, 10):
    print(f'Getting data on page: {page//10}')
    c = extract(page)
    transform(c)
print(len(joblist))


job_listings_csv = pd.DataFrame(joblist)
job_listings_csv.to_csv('jobs.csv')

job_listings_excel = pd.DataFrame(joblist)
job_listings_excel.to_excel('jobs.xlsx')