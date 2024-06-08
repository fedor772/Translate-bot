import telebot
from googletrans import Translator

# Создаем экземпляр класса Translator
translator = Translator()

# Создаем экземпляр бота
bot = telebot.TeleBot("7495754943:AAGecHUMf1uU6k2nyh2Y0CoXzDp6tvXmWf8")

# Обработчик сообщений
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот-переводчик. Отправьте мне текст, и я переведу его на выбранный вами язык.")

@bot.message_handler(func=lambda message: True)
def translate_text(message):
    # Получаем исходный текст и целевой язык от пользователя
    original_text = message.text
    target_language = message.text.split()[1] if len(message.text.split()) > 1 else 'en'

    # Переводим текст
    translated_text = translator.translate(original_text, dest=target_language)

    # Отправляем переведенный текст пользователю
    bot.reply_to(message, f"Переведенный текст: {translated_text.text}")

# Запускаем бота
bot.polling()