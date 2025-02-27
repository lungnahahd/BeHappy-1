from urllib.parse import urlencode, unquote, quote_plus
import urllib
import urllib.request
import requests
from bs4 import BeautifulSoup
import xml.etree.ElementTree

from requests.sessions import Request


serviceKey="aEwwPiJLOfQLF991Fvvcv6piLOUwnO7uH7qiX6DXVazK8EDb6Yw39Hsq7xA+F4ux1KvKgLNVTx3CP7/IvdpOtQ=="
service = unquote(serviceKey, 'UTF-8')


def checkNum(num): # 숫자 여부를 판단하는 함수
    try:
        tmp = float(num)
        return True
    except ValueError:
        return False

def showBin():
    data = []
    where =[]
    kind = []

 
    url = "https://api.odcloud.kr/api/15087773/v1/uddi:6bcb9ebf-d368-4ac8-9382-a9e82437f74d"
    returnType = "XML"
    page = "1"
    perPage = "280"

    queryParams = '?' + urlencode({ quote_plus('serviceKey') : service, quote_plus('page') : page, quote_plus('perPage') : perPage, quote_plus('returnType') : returnType})
    res = requests.get(url + queryParams)

    
    xml = res.text
    soup = BeautifulSoup(xml,'html.parser')
    for tag in soup.find_all('col', attrs={'name':'위도'}):
        check = str(tag.next)
        if checkNum(check):
            data.append(tag.next)
    for tag in soup.find_all('col', attrs={'name':'경도'}):
        check = str(tag.next)
        if checkNum(check):
            where.append(tag.next)
    for tag in soup.find_all('col', attrs={'name':'수거쓰레기종류'}):
        kind.append(tag.next)

    result =[]
    result.append(data)
    result.append(where)
    result.append(kind)
    # print(result) # result 에 대한 내용을 출력
    return result

