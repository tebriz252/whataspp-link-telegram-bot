import os
from telegram.ext import Updater, CommandHandler, MessageHandler
from telegram import Update, Filters

# Use environment variable for the bot token
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

def start(update, context):
    update.message.reply_text("Welcome! Send me a phone number, and I'll generate a WhatsApp link for you.")

def generate_whatsapp_link(update, context):
    phone_number = update.message.text.strip()
    if phone_number.isdigit() or (phone_number.startswith('+') and phone_number[1:].isdigit()):
        whatsapp_link = f"https://wa.me/{phone_number}"
        update.message.reply_text(f"Here is your WhatsApp link:\n{whatsapp_link}")
    else:
        update.message.reply_text("Please send a valid phone number.")

def main():
    updater = Updater(TELEGRAM_BOT_TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, generate_whatsapp_link))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
