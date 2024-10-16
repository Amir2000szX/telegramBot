import threading
import schedule
import sqlite3
import time
from telegram import Update
from telegram.ext import ApplicationBuilder , ContextTypes , CommandHandler , CallbackQueryHandler


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("hello mf welcome to mf bot")
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("why the fuck you need help about this bot it doesnt have anything")
async  def blup(update:Update , context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_message.chat_id
    type = int(context.args[0])
    with open("F:/TEl/AUD1.m4a",'rb') as voice:
        await context.bot.sendAudio(chat_id,voice)


Token = '7564736910:AAGHjeCYS9bvx54a3MQFuJmW8YeMxpTdfiU'
app = ApplicationBuilder().token(Token).build()
start_handler = CommandHandler('start', start)
help_handler = CommandHandler("help" , help)
blup_handler = CommandHandler("bloop",blup)
app.add_handler(CallbackQueryHandler())
app.add_handler(start_handler)
app.add_handler(help_handler)
app.add_handler(blup_handler)
app.run_polling()