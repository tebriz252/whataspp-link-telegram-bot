import os
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

# Fetch the bot token from the environment variable
BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("No BOT_TOKEN environment variable set!")

# Initialize the bot application
application = Application.builder().token(BOT_TOKEN).build()

# Handlers
async def start(update, context):
    await update.message.reply_text("Welcome! Send me a phone number, and I'll generate a WhatsApp link for you.")

async def generate_whatsapp_link(update, context):
    phone_number = update.message.text.strip()

    # Normalize the phone number
    phone_number = phone_number.replace(" ", "")  # Remove spaces
    phone_number = phone_number.replace("+", "")  # Remove +
    if phone_number.startswith("00"):            # Replace 00 with 994
        phone_number = "994" + phone_number[2:]
    elif phone_number.startswith("0"):           # Replace 0 with 994
        phone_number = "994" + phone_number[1:]

    # Validate the normalized phone number
    if phone_number.isdigit():
        whatsapp_link = f"https://wa.me/{phone_number}"
        await update.message.reply_text(f"Here is your WhatsApp link:\n{whatsapp_link}")
    else:
        await update.message.reply_text("Please send a valid phone number.")

# Main function to add handlers and run the bot
def main():
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, generate_whatsapp_link))

    application.run_polling()

if __name__ == "__main__":
    main()
