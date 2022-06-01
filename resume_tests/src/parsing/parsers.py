import requests
import codecs
from bs4 import BeautifulSoup as BS

__all__ = ('work_2', 'work_3', 'work_4')



def work_2(url, city=None, language=None):
    jobs = []
    errors = []
    if url:
        resp = requests.get(url)
        if resp.status_code == 200:
            soup = BS(resp.content, 'html.parser')
            main_div = soup.find('div', id='pjax-job-list')
            if main_div:
                div_lst = main_div.find_all('div', attrs={'class': 'job-link'})
                for div in div_lst:
                    title = div.find('h2')
                    href = title.a['href']
                    content = div.p.text
                    experience = 'No name'
                    exp = div.find('div', attrs={'class': 'exper'})
                    if exp:
                        experience = exp.span.b.text
                    company = 'No name'
                    com = div.find('div', attrs={'class': 'add-top-xs'})
                    if com:
                        company = com.span.b.text
                    jobs.append({'url': href, 'title': title.text,
                                 'company': company, 'experience': experience, 'description': content,
                                 'city_id': city, 'language_id': language})
            else:
                errors.append({'url': url, 'title': "Div does not exists"})

        else:
            errors.append({'url': url, 'title': "Page do not response"})

    return jobs, errors


def work_3(url, city=None, language=None):
    jobs = []
    errors = []
    if url:
        resp = requests.get(url)
        if resp.status_code == 200:
            soup = BS(resp.content, 'html.parser')
            main_div = soup.find('div', id='pjax-job-list')
            if main_div:
                div_lst = main_div.find_all('div', attrs={'class': 'job-link'})
                for div in div_lst:
                    title = div.find('h2')
                    href = title.a['href']
                    content = div.p.text
                    experience = 'No name'
                    exp = div.find('div', attrs={'class': 'exper'})
                    if exp:
                        experience = exp.span.b.text
                    company = 'No name'
                    com = div.find('div', attrs={'class': 'add-top-xs'})
                    if com:
                        company = com.span.b.text
                    jobs.append({'url': href, 'title': title.text,
                                 'company': company, 'experience': experience, 'description': content,
                                 'city_id': city, 'language_id': language})
            else:
                errors.append({'url': url, 'title': "Div does not exists"})

        else:
            errors.append({'url': url, 'title': "Page do not response"})

    return jobs, errors


def work_4(url, city=None, language=None):
    jobs = []
    errors = []
    if url:
        resp = requests.get(url)
        if resp.status_code == 200:
            soup = BS(resp.content, 'html.parser')
            main_div = soup.find('div', id='pjax-job-list')
            if main_div:
                div_lst = main_div.find_all('div', attrs={'class': 'job-link'})
                for div in div_lst:
                    title = div.find('h2')
                    href = title.a['href']
                    content = div.p.text
                    experience = 'No name'
                    exp = div.find('div', attrs={'class': 'exper'})
                    if exp:
                        experience = exp.span.b.text
                    company = 'No name'
                    com = div.find('div', attrs={'class': 'add-top-xs'})
                    if com:
                        company = com.span.b.text
                    jobs.append({'url': href, 'title': title.text,
                                 'company': company, 'experience': experience, 'description': content,
                                 'city_id': city, 'language_id': language})
            else:
                errors.append({'url': url, 'title': "Div does not exists"})

        else:
            errors.append({'url': url, 'title': "Page do not response"})

    return jobs, errors



