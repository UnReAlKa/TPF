from aiogram import types,executor,Dispatcher,Bot
from bs4 import BeautifulSoup
import requests
from selenium import webdriver

bot = Bot(token=("6509681127:AAGEofK_W9_YxnMvfsgVeloPIh3img45IgM"))
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def begin(message: types.Message):
    await bot.send_message(message.chat.id, "Привет")

@dp.message_handler(content_types=['text'])
async def begin(message: types.Message):
    url = "https://ru.wikipedia.org/w/index.php?go=Перейти&search=" + message.text
    request = requests.get(url)
    soup = BeautifulSoup(request.text, "html.parser")

    links = soup.find_all("div", class_="mw-search-result-heading")

    if len(links) > 0:
        url = "https://ru.wikipedia.org" + links[0].find("a")["href"]

    option = webdriver.ChromeOptions()
    option.add_argument('headless')

    driver = webdriver.Chrome()
    driver.get(url)

    driver.execute_script("window.scrollTo(0,200)")
    driver.save_screenshot("img.png")
    driver.close()

    photo = open("img.png", 'rb')
    await bot.send_photo(message.chat.id , photo=photo, caption='Сылка на статью: <a href="{url}">тык</a>',parse_mode="HTML")

executor.start_polling(dp)