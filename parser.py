## parser.py
import requests
from bs4 import BeautifulSoup
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'JuniorCreate.settings')
import django
django.setup()
## BlogData를 import해옵니다
from bookstore.models import Book

# 사용.
def get_all():
    # 주소 및 뷰티풀 수프 설정.
    url = "http://www.yes24.com/24/Category/Display/001001003024?ParamSortTp=05"
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    # 크롤링해서 베이스 주소 설정.
    data = {}
    find_img = soup.find_all("span", {"class": "imgBdr"})
    find_auth = soup.find_all("span", {"class": "goods_auth"})
    find_pub = soup.find_all("span", {"class": "goods_pub"})
    find_date = soup.find_all("span", {"class": "goods_date"})

    # 반환할 데이터 셋 설정.
    img_set = dict()
    auth_set = dict()
    pub_date_set = dict()

    for i in range(len(find_img)):
        # # 책 이름
        # print(find_img[i].find('a').find('img').get('alt'))
        # # 이미지 주소
        # print(find_img[i].find('a').find('img').get('src'))
        # # 작가 이름
        # print(find_auth[i].find('a').text)
        # # 작가 이름 주소
        # print(find_auth[i].find('a').get('href'))
        # # 출판사
        # print(find_pub[i].text)
        # # 출판일
        # print(find_date[i].text)

        # 책 이름, 이미지 주소
        img_set[find_img[i].find('a').find('img').get('alt')] = list()
        img_set[find_img[i].find('a').find('img').get('alt')].append(find_img[i].find('a').find('img').get('src'))
        # 작가 이름, 주소
        img_set[find_img[i].find('a').find('img').get('alt')].append(find_auth[i].find('a').text)
        img_set[find_img[i].find('a').find('img').get('alt')].append(find_auth[i].find('a').get('href'))
        # 출판사, 출판일
        img_set[find_img[i].find('a').find('img').get('alt')].append(find_pub[i].text)
        img_set[find_img[i].find('a').find('img').get('alt')].append(find_date[i].text)

    return img_set

if __name__ == "__main__":
    img= get_all()
    #print(img.items())
    
    for title, others in img.items():
        print(title, others)
        Book(title=title, link=others[0], author_name=others[1], author_link=others[2], pub_name=others[3], pub_date=others[4]).save()
        
