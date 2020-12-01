# 웹크롤링 프로젝트
# https://h-glacier.tistory.com/

import datetime
from bs4 import BeautifulSoup
import urllib.request

now = datetime.datetime.now()

print('      오늘의 주요 정보를 요약해 드리겠습니다.\n')

# 오늘의 날씨
print('  ○>> #오늘의 #날씨 #요약 \n')
webpage = urllib.request.urlopen('https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query=%EC%84%9C%EC%9A%B8%EB%82%A0%EC%94%A8')
soup = BeautifulSoup(webpage, 'html.parser')
temps = soup.find('span',"todaytemp")
cast = soup.find('p',"cast_txt")
print('--> 서울 날씨 : ' , temps.get_text() , '℃' , cast.get_text())

webpage = urllib.request.urlopen('https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query=%EB%8C%80%EA%B5%AC+%EB%82%A0%EC%94%A8')
soup = BeautifulSoup(webpage, 'html.parser')
temps = soup.find('span',"todaytemp")
cast = soup.find('p',"cast_txt")
print('--> 대구 날씨 : ' , temps.get_text() , '℃' , cast.get_text())

webpage = urllib.request.urlopen('https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EB%B6%80%EC%82%B0+%EB%82%A0%EC%94%A8&oquery=%EB%8C%80%EA%B5%AC+%EB%82%A0%EC%94%A8&tqi=UrZy%2Bsp0YidssAyki54ssssssKC-251380')
soup = BeautifulSoup(webpage, 'html.parser')
temps = soup.find('span',"todaytemp")
cast = soup.find('p',"cast_txt")
print('--> 부산 날씨 : ' , temps.get_text() , '℃' , cast.get_text())
print('\n')

# 오늘의 코로나 현황
# https://h-glacier.tistory.com/
print('  ○>> #오늘의 #국내 #코로나19 #현황 \n')
webpage = urllib.request.urlopen('http://ncov.mohw.go.kr/')
soup = BeautifulSoup(webpage, 'html.parser')
dayconfirm = soup.find('span',"data1")
allinfo = soup.find('span', 'num')
print(' --> 오늘의 신규 확진자 : ' ,'\n --> 현재까지 확진자 : ', allinfo.get_text(),'\n\n')

# 오늘의 핫토픽
print('  ○>> #오늘의 #핫토픽 #헤드라인 \n')
webpage = urllib.request.urlopen('https://www.naver.com/')
soup = BeautifulSoup(webpage, 'html.parser')
for temps in soup.find_all('a',"issue"):
    print('--> ' , temps.get_text())
print('\n')