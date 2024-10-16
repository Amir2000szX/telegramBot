import threading
import schedule
import sqlite3
import time
from telegram import Update , InlineKeyboardButton , InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder , ContextTypes , CommandHandler , CallbackQueryHandler


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [

        [InlineKeyboardButton("blup",callback_data="1"),
        InlineKeyboardButton("bleep",callback_data="2")],
        [InlineKeyboardButton("bala",callback_data="3")]
    ]
    reply = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("choose the sound: " , reply_markup=reply)
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("why the fuck you need help about this bot it doesnt have anything")
async  def button(update:Update , context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_message.chat_id
    query = update.callback_query
    await query.answer()
    if query.data =="1":
        with open("TEl/AUD1.m4a",'rb') as voice:
            await context.bot.sendAudio(chat_id,voice)
    if query.data =="2":
        with open("TEl/AUD2.m4a",'rb') as voice:
            await context.bot.sendAudio(chat_id,voice)
    if query.data == "3":
        with open("TEL/AUD3.m4a",'rb') as voice:
            await context.bot.sendAudio(chat_id,voice)


Token = '7564736910:AAGHjeCYS9bvx54a3MQFuJmW8YeMxpTdfiU'
app = ApplicationBuilder().token(Token).build()
start_handler = CommandHandler('start', start)
help_handler = CommandHandler("help" , help)
app.add_handler(CallbackQueryHandler(button))
app.add_handler(start_handler)
app.add_handler(help_handler)
app.run_polling()