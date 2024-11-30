from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Welcome! Send me a phone number, and I'll generate a WhatsApp link for you.")

def generate_whatsapp_link(update: Update, context: CallbackContext) -> None:
    # Extract the phone number from the message
    phone_number = update.message.text.strip()

    # Validate the phone number format (basic validation for example purposes)
    if phone_number.isdigit() or (phone_number.startswith('+') and phone_number[1:].isdigit()):
        whatsapp_link = f"https://wa.me/{phone_number}"
        update.message.reply_text(f"Here is your WhatsApp link:\n{whatsapp_link}")
    else:
        update.message.reply_text("Please send a valid phone number.")

def main() -> None:
    # Replace 'YOUR_BOT_TOKEN' with your bot's API token
    updater = Updater("7659328626:AAEKml-f5wjKbrWbNOyj23USqxkQ58VSTRk")

    # Add handlers
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, generate_whatsapp_link))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
