# import requests

# url = 'https://bluedollar.net/informal-rate/'

# response = requests.get(url)

# print(response.status_code)
# print(response.text)

# if response == 200:
#     data = response.json()
#     dollar_rate = data ['dollar_rate']
#     print(f'Курс доллара:{dollar_rate}')
# else:
#     print('Произошла ошибка при получении данных')


import requests
from bs4 import BeautifulSoup

url = 'https://bluedollar.net/informal-rate/'
response = requests.get(url)


soup = BeautifulSoup(response.content, 'html.parser')
buying_element = soup.find('div', class_="buy buy-sell-blue")
selling_element = soup.find('div', class_="sell buy-sell-blue")

buying_price= buying_element.contents[0]
selling_price= selling_element.contents[0]



# if response.status_code == 200:
#     soup = BeautifulSoup(response.content, 'html.parser')
    
#     buying_element = soup.find('div', class_="buy")
#     selling_element = soup.find('div', class_="sell buy-sell-blue")
    
#     if buying_element:
#         buying_rate = buying_element.text.split()[0]
#         print(f'Курс покупки доллара: {buying_rate}')
#     else:
#         print('Курс покупки доллара не найден')
    
#     if selling_element:
#         selling_rate = selling_element.text.strip()
#         print(f'Курс продажи доллара: {selling_rate}')
#     else:
#         print('Курс продажи доллара не найден')
# else:
#     print('Произошла ошибка при получении данных')



# import requests
# from bs4 import BeautifulSoup

# url = 'https://bluedollar.net/informal-rate/'
# response = requests.get(url)

# if response.status_code == 200:
#     soup = BeautifulSoup(response.content, 'html.parser')
    
#     buying_element = soup.find('div', class_='buy')
#     selling_element = soup.find('div', class_='sell')
    
#     if buying_element:
#         buying_rate = buying_element.text.split()[0].replace(',', '')  # Remove comma from the numeric value
#         print(f'Курс покупки доллара: {buying_rate}')
    
#     if selling_element:
#         selling_rate = selling_element.text.split()[0].replace(',', '')  # Remove comma from the numeric value
#         print(f'Курс продажи доллара: {selling_rate}')
# else:
#     print('Произошла ошибка при получении данных')