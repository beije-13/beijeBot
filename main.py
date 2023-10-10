from typing import Text
import telebot
from telebot import types
from googletrans import Translator

with open('token.bot', 'r') as file:
    BOT_TOKEN = file.read()


translator = Translator()
bot = telebot.TeleBot(BOT_TOKEN)


@bot.inline_handler(lambda query: len(query.query) > 0)
def query_text(inline_query):
    translation = types.InlineQueryResultArticle(
        '1',
        'Translation',
        types.InputTextMessageContent(f'{translator.translate(inline_query.query, dest="ru").text}'),
        description=f'{translator.translate(inline_query.query, dest="ru").text}'
    )
    bot.answer_inline_query(inline_query.id, [translation])


@bot.message_handler(commands=['start'])
def start_command(message):
    bot.reply_to(message, f"Hi, {message.from_user.first_name}! My name is beije.\nI was created for translating text from any language to russian!")
    bot.send_message(message.from_user.id, 'Type /help to get how2use info :)')


@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(message.from_user.id, 'I\'m inline bot. For translating text you need: \n-@ me in any chat you need\n-Write any text\n-Press the pop-up result to send translation to this chat.')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    bot.send_message(message.from_user.id, 'Type /help to get a quick guide :)')


bot.polling(none_stop=True)
