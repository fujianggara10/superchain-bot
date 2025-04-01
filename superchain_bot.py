from telegram.ext import Application, CommandHandler, MessageHandler
from telegram.ext.filters import Text, Command
from telegram import BotCommand, ReplyKeyboardMarkup, ReplyKeyboardRemove
import requests
from bs4 import BeautifulSoup

# Bot token
TOKEN = "7717186753:AAHO-fXEGO-9mmPaLIEN83lVG2LG7ow3wqg"  # Your token

# Define the main menu buttons
MENU_KEYBOARD = ReplyKeyboardMarkup([
    ["📩 Subscribe to Updates", "📜 View Active Proposals"],
    ["💬 Optimism Forum Summary", "💬 Lisk Forum Summary"]
], resize_keyboard=True)

# "Back to Menu" button
BACK_TO_MENU = ReplyKeyboardMarkup([["⬅️ Back to Menu"]], resize_keyboard=True)

# Start function with a welcoming message
async def start(update, context):
    welcome_message = (
        "Hey there! I’m Superchain_Bot -Built By Fuji AR!\n"
        "Your go-to assistant for Superchain governance\n"
        "Pick an option below to get started!"
    )
    await update.message.reply_text(welcome_message, reply_markup=MENU_KEYBOARD)

# Handle "Subscribe to Updates" button
async def subscribe(update, context):
    message = (
        "Awesome! You’re subscribed!\n"
        "You’ll now get the latest proposal updates straight to Telegram."
    )
    await update.message.reply_text(message, reply_markup=BACK_TO_MENU)

# Handle "View Active Proposals" button
async def live_proposals(update, context):
    message = (
        "Active Proposal on Optimism!\n\n"
        "Upgrade Proposal #13: OPCM & Incident Response Improvements\n"
        "This proposal aims to enhance incident response procedures and streamline contract management.\n"
        "Voting Ends: March 19, 2025, 18:55:25"
    )
    await update.message.reply_text(message, reply_markup=BACK_TO_MENU)

# Handle "Optimism Forum Summary" button
async def optimism_forum(update, context):
    message = (
        "💼 Weekly Optimism Forum Summary 💼\n\n"
        "This week’s discussions focused on upcoming voting cycles and incident response upgrades:\n"
        "1️⃣ Upgrade Proposal #13 by maurelian\n"
        "📊 82% positive feedback from 11 comments.\n"
        "👍 Strong community support for the upgrades.\n"
        "⚠️ Some concerns about governance clarity.\n\n"
        "🔗 Explore Optimism Forum: https://gov.optimism.io/"
    )
    await update.message.reply_text(message, reply_markup=BACK_TO_MENU)

# Handle "Lisk Forum Summary" button
async def lisk_forum(update, context):
    message = (
        "💬 Weekly Lisk Forum Summary 💬\n\n"
        "⏳ No recent updates from the Lisk forum.\n"
        "We’ll update this section soon! 🔜"
    )
    await update.message.reply_text(message, reply_markup=BACK_TO_MENU)

# Handle button clicks (text messages)
async def handle_message(update, context):
    text = update.message.text
    if text == "📩 Subscribe to Updates":
        await subscribe(update, context)
    elif text == "📜 View Active Proposals":
        await live_proposals(update, context)
    elif text == "💬 Optimism Forum Summary":
        await optimism_forum(update, context)
    elif text == "💬 Lisk Forum Summary":
        await lisk_forum(update, context)
    elif text == "⬅️ Back to Menu":
        await update.message.reply_text(
            "🌟 Back to the main menu! Pick an option below: 🚀",
            reply_markup=MENU_KEYBOARD
        )
    else:
        await update.message.reply_text(
            "Please select an option from the menu below! 😊",
            reply_markup=MENU_KEYBOARD
        )

# Set bot commands
async def set_commands(application):
    commands = [
        BotCommand("start", "Start the bot and view the menu"),
        BotCommand("menu", "Show the main menu")
    ]
    await application.bot.set_my_commands(commands)

# Show menu command
async def menu(update, context):
    await update.message.reply_text(
        "🌟 Back to the main menu! Pick an option below: 🚀",
        reply_markup=MENU_KEYBOARD
    )

# Main function
def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("menu", menu))
    application.add_handler(MessageHandler(Text() & ~Command(), handle_message))
    application.post_init = set_commands
    print("Bot is running...")
    application.run_polling()

if __name__ == "__main__":
    main()