import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first.settings')
import django
django.setup() #manage.py를 통해 장고 실행이 아니므로 장고 셋업

from webtoon.models import Episode

from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup #원하는 문자열을 찾을 때


def main():
    url_set = { ep.url for ep in Episode.objects.all() } #딕셔너리?

    episode_list = []

    for page in range(1, 10000):
        params = {
            'titleId': 667870,
            'page': page,
        }
        page_url = 'http://comic.naver.com/webtoon/list.nhn'
        html = requests.get(page_url, params=params).text
        soup = BeautifulSoup(html, 'html.parser')
        for a_tag in soup.select('.viewList .title a'):
            title = a_tag.text
            link = urljoin(page_url, a_tag['href'])

            if link in url_set: #페이지가 5로 넘어가도 1번째 페이지로 넘어가므로 동일 url 반복
                print('End!')
                return episode_list

            url_set.add(link)

            print(title, link)
            episode_list.append(Episode(title=title, url=link))


if __name__ == '__main__':  #import한 경우는 실행 X
    from django.db import connection

    episode_list = main()
    Episode.objects.bulk_create(episode_list) #리스트로 한번에 쿼리문 날려서 객체 생성

    for idx, query in enumerate(connection.queries, 0):
        print(idx, query)

'''if __name__ == '__main__':
    print 'This program is being run by itself'
else:
    print 'I am being imported from another module

$ python using_name.py
This program is being run by itself

$ python
>>> import using_name
I am being imported from another module

파이썬은 import 과정에서 그 파일을 실행한다. 만약 import는 하되, 실행하고싶지 않으면
if __name__ == '__main__': 뒤에 설정. 이 뒤에 오는 것은 import하지 않은 경우만 실행됨.
import하면 __name__은 그 파일명이므로.
직접 그 파일을 실행하면 __name__ is __main__'''