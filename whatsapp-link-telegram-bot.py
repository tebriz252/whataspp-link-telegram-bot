from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

BOT_TOKEN = os.getenv("BOT_TOKEN")
# Start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Welcome! Send me a phone number, and I'll generate a WhatsApp link for you.")

# Generate WhatsApp link handler
async def generate_whatsapp_link(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    phone_number = update.message.text.strip()

    # Basic phone number validation
    if phone_number.isdigit() or (phone_number.startswith('+') and phone_number[1:].isdigit()):
        whatsapp_link = f"https://wa.me/{phone_number}"
        await update.message.reply_text(f"Here is your WhatsApp link:\n{whatsapp_link}")
    else:
        await update.message.reply_text("Please send a valid phone number.")

# Main function to start the bot
def main():
    # Replace 'YOUR_BOT_TOKEN' with your actual bot token
    application = Application.builder().token(BOT_TOKEN).build()

    # Command and message handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, generate_whatsapp_link))

    # Run the bot
    application.run_polling()

if __name__ == '__main__':
    main()
