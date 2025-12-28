# Telegram Bot: Reverse Image Search (Yandex + Google + Bing)
# ----------------------------------------------------------
# This bot takes a photo from the user and finds related images/videos
# using Yandex, Google Lens, and Bing Visual Search.

from telegram import Update, InputFile
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import requests
import os

# ⚠️ Replace this after reset
BOT_TOKEN = "TOKEN_PLACEHOLDER"

# --- Reverse search helper links ---
YANDEX_URL = "https://yandex.com/images/search?rpt=imageview&url={image_url}"
GOOGLE_URL = "https://www.google.com/searchbyimage?image_url={image_url}"
BING_URL = "https://www.bing.com/visualsearch?imgurl={image_url}"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Welcome to SnapTrace Bot!\nSend me an image, and I’ll find where it came from — maybe even the video!")

async def handle_image(update: Update, context: ContextTypes.DEFAULT_TYPE):
    photo = update.message.photo[-1]
    file = await context.bot.get_file(photo.file_id)
    image_url = file.file_path

    await update.message.reply_text("🔍 Searching for your image across the web... please wait.")

    # Generate search links
    yandex_link = YANDEX_URL.format(image_url=image_url)
    google_link = GOOGLE_URL.format(image_url=image_url)
    bing_link = BING_URL.format(image_url=image_url)

    response_text = (
        f"🧠 **Reverse Image Results:**\n\n"
        f"🔹 [Yandex Search]({yandex_link})\n"
        f"🔹 [Google Lens]({google_link})\n"
        f"🔹 [Bing Visual Search]({bing_link})\n\n"
        f"Try each link — if your image is from a video, one of them will reveal it!"
    )

    await update.message.reply_markdown(response_text)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Send me a photo, and I’ll find its source/video online. That’s all you need to do!")

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.PHOTO, handle_image))

    print("🤖 SnapTrace Bot is running...")
    app.run_polling()
ftgv
