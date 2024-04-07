# **Вступление**
___
### Тelegram-bot, который спрашивает у пользователя вопрос, после чего на него отвечает в виде фотки из википедии





## Требования к установке
```python
pip install aiogram
pip install selenium
pip install requests
pip install bs4
```
___
## **Добавление библиотек**
```python
from aiogram import types,executor,Dispatcher,Bot
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
``` 
*Импортируем свой токен в проэкт: ```bot = Bot("Your_Token") ```* 

*Запуск бота командой старт*

```python
@dp.message_handler(commands=['start'])
async def begin(message: types.Message):
    await bot.send_message(message.chat.id, "Привет")
```

*Ищем ответ на вопрос на сайте*
```python
@dp.message_handler(content_types=['text'])
async def begin(message: types.Message):
    url = "https://ru.wikipedia.org/w/index.php?go=Перейти&search=" + message.text
    request = requests.get(url)
    soup = BeautifulSoup(request.text, "html.parser")

    links = soup.find_all("div", class_="mw-search-result-heading")

    if len(links) > 0:
        url = "https://ru.wikipedia.org" + links[0].find("a")["href"]
```
## Развертывание
```python
python3 bot.py
```

# **Конфигурация**
Add [Bot_Father](https://t.me/botfather)
___

## Поддержка
[Telegram](https://web.telegram.org/a/#5153165332)
___




