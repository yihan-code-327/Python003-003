from bs4 import BeautifulSoup as BS
import requests 
import pandas as pd 
import time

'''
安装并使用 requests、bs4 库，
爬取猫眼电影（）的前 10 个电影名称、电影类型和上映时间，
并以 UTF-8 字符集保存到 csv 格式的文件中。
'''

def get_bs(url_ext):
    url = f"https://maoyan.com{url_ext}"
    #user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
    #user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3"
    user_agent ='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15'
    header = {'user-agent':user_agent}
    response = requests.get(url, headers = header)
    if response.status_code !=200:
        exit()
    bs_info = BS(response.text, 'html5lib')
    return bs_info

def get_top_urls():
    bs_info = get_bs('/board')
    movie_urls = []
    for tags in bs_info.find_all('p', attrs = {'class':'name'}):
        for atag in tags.find_all('a',):
            movie_url = atag.get('href')
            movie_urls.append(movie_url)
    return movie_urls

def get_movie_details(url_ext):
    bs_info = get_bs(url_ext)
    for tags in bs_info.find_all('div', attrs = {'class':'movie-brief-container'}):
        try:
            c_name = tags.find('h1', attrs ={'class':'name'}).get_text()
        except:
            c_name = None
        try:
            e_name = tags.find('div', attrs = {'class':'ename ellipsis'}).get_text()
        except:
            e_name = None
        try:
            movie_types = (',').join( [atag.get_text() for atag in tags.find_all('a',)])
        except:
            movie_types = None 
        try:
            on_date = tags.select("ul li" )[2].get_text()
        except:
            on_date = None
        #print(c_name, e_name, movie_types, on_date)
    return [c_name, e_name, movie_types, on_date]

movie_urls= get_top_urls()
results = []
for url_ext in movie_urls:
    results.append(get_movie_details(url_ext))
    time.sleep(2)

pd.DataFrame(results, columns = ['c_name', 'e_name', 'movie_types', 'on_date'])\
    .reset_index(drop = True)\
    .to_csv('./maoyan_movie.csv', encoding= 'utf-8')