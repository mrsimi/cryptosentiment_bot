import os 
import telebot
from dotenv import load_dotenv
load_dotenv()
from reddit_crawler import get_data
from sentiment_analyzer import get_sentiments


def run_telegram_bot():
    bot = telebot.TeleBot(os.environ.get('TELEGRAM_TOKEN'))

    @bot.message_handler(commands=['start', 'help'])
    def send_welcome(message):
        bot.reply_to(message, "This telegram bot gives you the currency sentiment \n of a cryptocurrency based on data from reddit")
        bot.send_message(message.chat.id, "Reply with a cryptocurrency name")

    @bot.message_handler(func=lambda message: True)
    def echo_all(message):

        try: 
            bot.send_message(message.chat.id, 'Please be patient. We are trying to generate a sentiment report...')
            crawled_data = get_data(message.text)
            report, text_report = get_sentiments(crawled_data, 'reddit')
            bot.reply_to(message, text_report)
        except Exception as e:
            bot.reply_to(message, 'There was an error. \n Kindly wait a little before you retry and make sure it is a valid cryptocurrency')
	    
    bot.infinity_polling()