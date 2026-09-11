import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import staypresent

logging.basicConfig(level=logging.INFO)
TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Type /help to see commands.")

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("/start - Welcome\n/help - This help\n/about - Info")

async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Simple utility bot. No data collected.")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(CommandHandler("about", about))
    app.run_polling()

if __name__ == "__main__":
    # Start HTTP server for Railway health checks, then run bot
    staypresent.web.json({"status": "running"})
    staypresent.run("main.py", port=int(os.getenv("PORT", 8080)))
