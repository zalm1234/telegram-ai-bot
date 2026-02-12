import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# وەرگرتنی توکن لە Variables
TOKEN = os.getenv("8289517227:AAGpASlCO7khYMySSZ1vl3CmN4MqQEiMRX8")

# ئەگەر توکن نەبوو، بەرنامە وەستێت (بۆ ئەوەی کڕاشی شاردراو نەبێت)
if not TOKEN:
    raise ValueError("BOT_TOKEN is not set in Railway Variables")

# وەڵامی /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot is running 🚀")

# وەڵامی هەر نامەیەک (echo)
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(update.message.text)

# دروستکردنی بۆت
app = ApplicationBuilder().token(TOKEN).build()

# زیادکردنی هەندلەرەکان
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

print("Bot started successfully...")

# دەستپێکردن
app.run_polling()