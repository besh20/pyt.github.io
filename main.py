import requests
from bs4 import BeautifulSoup
from telegram import Bot

bot_token = '6969736991:AAEZX4HB2Jv_fMVlt12A7cpRQWdduft2qQc'
chat_idi = '@projectpy'

url = 'https://www.ethiopiaobserver.com/category/media/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the article tags on the page
articles = soup.find_all('article')

# Initialize an empty list to store the article information
article_info = []

# Loop through each article tag and extract the title, link, and image
for article in articles:
    title = article.find('h2').text
    link = article.find('a')['href']
    image = article.find('img')['src']
    article_info.append((title, link, image))

# Send the article information to the Telegram channel
bot = Bot(token=bot_token)
for info in article_info:
    bot.send_message(chat_id=chat_idi, text=f'Title: {info[0]}\nLink: {info[1]}\nImage: {info[2]}')

response = requests.post(f'https://api.telegram.org/bot{bot_token}/sendMessage', data={
    'chat_id': chat_idi,
    'text': 'Hello, Telegram!'
})










