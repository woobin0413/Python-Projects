import requests
from bs4 import BeautifulSoup

from twilio.rest import Client

<<<<<<< HEAD
account_sid = '' # Found on Twilio Console Dashboard
auth_token = '' # Found on Twilio Console Dashboard

myPhone = '' # Phone number you used to verify your Twilio account
TwilioNumber = '' # Phone number given to you by Twilio
=======
account_sid = '#' # Found on Twilio Console Dashboard
auth_token = '#' # Found on Twilio Console Dashboard

myPhone = '#' # Phone number you used to verify your Twilio account
TwilioNumber = '#' # Phone number given to you by Twilio
>>>>>>> cdb98408951f672c4a9cd582109ddeabd3ecac92

client = Client(account_sid, auth_token)



# HTTP GET Request
# req = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn')
req = requests.get('https://slickdeals.net/deals/')
link = 'https://slickdeals.net/deals/'
html = req.text


soup = BeautifulSoup(html, 'html.parser')

my_titles = soup.select(
    '#mainColumn > div.box.popularDeal > div > div > div.mainDealInfo > div > div.dealTitle > a'
)

# print len(my_titles)
my_rates = soup.select(
    '#mainColumn > div.box.popularDeal > div:nth-child(2) > div > div'
)
# for rate in soup.find_all('div',{'class': 'num'}):
#     print rate

total = ''

for link in soup.find_all("div", {"class": "dealRow"}):
    for rate in link.find_all('div',{'class':'num'}):
        if(int(rate.text))>25:
            item_rate = (rate.text).strip()
            item_name = (link.find_all('div', {'class':'dealTitle'})[0].text).strip()
            item_price = ((link.find_all('div', {'class': 'price'}))[0].text).strip()
            total += '\n' + 'item rate: ' + item_rate + ' ' + '\n' + \
                     'item name: ' + item_name + '\n' \
                     + 'item price: ' + item_price + '\n'
if(total==""):
    total += 'Empty Product'

# (Twilio) sending a msg regarding the most slick deals that have more than 25 likes
#
# client.messages.create(
#   to= myPhone,
#   from_= TwilioNumber,
#   body=  total
# )

print total
