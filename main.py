import telebot
from googletrans import Translator

# Создаем экземпляр класса Translator
translator = Translator()

# Создаем экземпляр бота
with open('key.config', 'r') as file:
    key = file.read().strip()
bot = telebot.TeleBot(key)

# Читаем файл с названиями всех языков
with open('textlangs.txt',  'r', encoding='utf-8') as tlangs:
    tlang = tlangs.read().strip()

# Создаём список валидных кодов языка
langlist = ["af", "sq", "am", "ar", "hy", "az", "eu", "be", "bn", "bs", "bg", "ca", "ceb", "ny", "zh-cn", "zh-tw", "co", "hr", "cs", "da", "nl", "en", "eo", "et", "tl", "fi", "fr", "fy", "gl", "ka", "de", "el", "gu", "ht", "ha", "haw", "iw/he", "hi", "hmn", "hu", "is", "ig", "id", "ga", "it", "ja", "jw", "kn", "kk", "km", "ko", "ku", "ky", "lo", "la", "lv", "lt", "lb", "mk", "mg", "ms", "ml", "mt", "mi", "mr", "mn", "my", "ne", "no", "ps", "fa", "pl", "pt", "pa", "ro", "ru", "sm", "gd", "sr", "st", "sn", "sd", "si", "sk", "sl", "so", "es", "su", "sw", "sv", "tg", "ta", "te", "th", "tr", "uk", "ur", "uz", "vi", "cy", "xh", "yi", "yo", "zu"]

# Обработчик сообщений
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот-переводчик. Отправьте мне текст, и я переведу его на выбранный вами в конце сообщения язык. Чтобы показать список всех языков введите /langs")

@bot.message_handler(commands=['langs'])
def show_langs(message):
    bot.reply_to(message, tlang)

@bot.message_handler(func=lambda message: True)
def translate_text(message):
    # Получаем исходный текст и целевой язык от пользователя
    original_text = message.text
    if message.text.split()[len(message.text.split()) - 1] in langlist:
        target_language = message.text.split()[len(message.text.split()) - 1]
    else:
        target_language = 'en'

    # Переводим текст
    translated_text = translator.translate(original_text, dest=target_language)

    # Отправляем переведенный текст пользователю
    bot.reply_to(message, f"Переведенный текст: {translated_text.text}")

# Запускаем бота
bot.polling()