# Google-image-downloader-telegram-bot
Parses and downloads images from google.com using color and license (commercial/non-commercial use) filters. The bot will send images in .jpg or .png.
The bot uses the [Aiogram](https://github.com/aiogram/aiogram) framework for handling Telegram interactions and the [iCrawler](https://icrawler.readthedocs.io/en/latest/) library for image scraping.
# Requirements
Requirements are provided in **requirements.txt**

```pip install -r requirements.txt```
# Preview
![image](https://github.com/DuranTonee/Google-image-downloader-telegram-bot/assets/95922080/285e0380-b713-4b77-a66f-6f758359b982)

### Colors are provided in the reply keyboard:
![image](https://github.com/DuranTonee/Google-image-downloader-telegram-bot/assets/95922080/84c2d4af-d06d-4b05-ba6a-2626571dd6d0)

# How to start
* Provide your bot token you recieved from [BotFather](https://telegram.me/BotFather) into **create_bot.py** or using **config.py** (you have to create one)
* Run **main.py**
* Text your bot /start
> [!NOTE]
> The bot utilizes the Google Image Crawler from iCrawler, so the images retrieved may vary based on the availability on Google.
