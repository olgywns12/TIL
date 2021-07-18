import requests

'''
telegram 정보
 - TOKEN : "1899377018:AAEiW3rmRqn0MMPtYSm4p4G2EOIiIeVpEzk"
 - URL : f'https://api.telegram.org/bot{TOKEN}'

NAVER 정보
 - 클라이언트 ID : 유저 등록 API 마다 다름
 - 클라이언트 PW : 상동
'''

product_name = ''
count = 0

while(True):
    # 기본 설정
    # NAVER API call
    naver_client_id = ""
    naver_client_pw = ""

    # Telegram API call
    TOKEN = "1899377018:AAEiW3rmRqn0MMPtYSm4p4G2EOIiIeVpEzk"
    tel_url = f'https://api.telegram.org/bot{TOKEN}'

    # Chat & Product 받아오기
    pd_name = product_name
    UPDATES_URL = f'{tel_url}/getUpdates'
    res = requests.get(UPDATES_URL).json()  # request로 해당
    chat_id = res.get('result')[-1]
    chat_id = chat_id.get('message').get('chat').get('id')
    product_name = res.get('result')[-1].get('message').get('text')

    URL = ' https://openapi.naver.com/v1/search/shop.json?query='
    query = product_name  # 나중에는 입력받는 형태로 구성

    headers = {
        'X-Naver-Client-Id': naver_client_id,
        'X-Naver-Client-Secret': naver_client_pw
    }

    product = requests.get(URL+query, headers=headers).json()['items'][0]
    product_name = product['title']
    product_lprice = product['lprice']
    product_link = product['link']

    text = f'| 이름: {product_name} \n \n| 가격: {product_lprice}\\ \n \n| 링크: {product_link}'

    # telegram으로 message_url을 통해서 문자 보내기 'text' 변수에 해당 메세지 입력

    message_url = f'{tel_url}/sendMessage?chat_id={chat_id}&text={text}'
 
    if pd_name==product_name:
        count += 1
    else:
        count = 1

    if count <= 1:
        requests.get(message_url)
