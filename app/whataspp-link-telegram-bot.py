from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext, filters
from telegram import Update

# Start command handler
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Welcome! Send me a phone number, and I'll generate a WhatsApp link for you.")

# Generate WhatsApp link handler
def generate_whatsapp_link(update: Update, context: CallbackContext) -> None:
    phone_number = update.message.text.strip()

    # Basic phone number validation
    if phone_number.isdigit() or (phone_number.startswith('+') and phone_number[1:].isdigit()):
        whatsapp_link = f"https://wa.me/{phone_number}"
        update.message.reply_text(f"Here is your WhatsApp link:\n{whatsapp_link}")
    else:
        update.message.reply_text("Please send a valid phone number.")

# Main function to start the bot
def main():
    # Replace 'YOUR_BOT_TOKEN' with your actual bot token
    updater = Updater("YOUR_BOT_TOKEN")

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, generate_whatsapp_link))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
