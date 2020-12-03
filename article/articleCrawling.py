from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import quote
import re

TARGET_URL_BEFORE_PAGE_NUM = "http://news.donga.com/search?p="
TARGET_URL_BEFORE_KEYWORD = '&query='
TARGET_URL_REST = '&check_news=1&more=1&sorting=1&search_date=1&v1=&v2=&range=1'

def get_link_from_news_title(page_num, URL,articleIndex):
    count=1
    for i in range(page_num):
        # 페이지당 15개의 게시물
        current_page_num = 1 + i * 15
        # URL 처음 = 오는 위치 반환 (URL에 몇페이지 인지 추가하기 위해)
        position = URL.index('=')
        # 페이지가 있는 URL 재구성
        URL_with_page_num = URL[: position + 1] + str(current_page_num) \
                            + URL[position + 1:]
        # 재구성한 URL을 request로 호출
        source_code_from_URL = urllib.request.urlopen(URL_with_page_num)
        # BeautifulSoup로 변환, 기사 분석 후 추출하기 위해
        soup = BeautifulSoup(source_code_from_URL, 'html.parser', from_encoding='utf-8')

        # 본문 기사가 담긴 URL을 찾기위해
        for title in soup.find_all('p', 'tit'):
            title_link = title.select('a')
            #이거 따로 띄워주기
            article_URL = title_link[0]['href']
            if count==articleIndex:
                get_text(article_URL)
            count+=1

def get_text(URL):
    source_code_from_url = urllib.request.urlopen(URL)
    # urlllib로 기사 페이지를 요청받습니다.
    soup = BeautifulSoup(source_code_from_url, 'html.parser', from_encoding='utf-8')
    # BeautifulSoup로 페이지를 분석하기위해 soup변수로 할당 받습니다.
    content_of_article = soup.select('div.article_txt')
    # 기사의 본문내용을 추출
    for item in content_of_article:
        string_item = str(item.find_all(text=True))
        clean_text(string_item,URL)
    # 기사 텍스트가 있다면 파일에 쓴다

def clean_text(text,URL):
    cleaned_text = re.sub('[a-zA-Z]', '', text)
    cleaned_text = re.sub('[\{\}\[\]\/?.,;:|\)*~`!^\-_+<>@\#$%&\\\=\(\'\"]','', cleaned_text)
    cleaned_text = re.sub('["\t"]','', cleaned_text)
    cleaned_text = re.sub('다 ', '다.\n', cleaned_text)
    cleaned_text = re.sub(' [0-9] ', '', cleaned_text)
    cleaned_text = re.sub('   ', '', cleaned_text)
    cleaned_text = re.sub('15952770652440', '', cleaned_text)
    cleaned_text = re.sub('1249652111', '', cleaned_text)
    #cleaned_text = re.sub('[0-9]','',cleaned_text)
    result=[URL,cleaned_text]
    print(result)
    return result

def articleCrawling(articleIndex=1,keyword="IT 밴처기업"):
    # 검색하고 하는 단어 keyword = "IT 밴처기업"
    page_num = 1  # 가져올 페이지 숫자
    target_URL = TARGET_URL_BEFORE_PAGE_NUM + TARGET_URL_BEFORE_KEYWORD \
                 + quote(keyword) + TARGET_URL_REST
    get_link_from_news_title(page_num, target_URL,articleIndex)

if __name__ == '__main__':
    articleCrawling()