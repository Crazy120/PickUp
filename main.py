import random
from os import environ
from pyrogram import Client, filters
from pyrogram.errors import UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup

bot = Client(
            "PickUp",
            api_id = int(environ["API_ID"]),
            api_hash = environ["API_HASH"],
            bot_token = "5376007165:AAF4EDHXyoteW7PxH3SmvvsBu0oCWfzv0rg"
)

force = "TeamDumperOps"
force_message = "<b>You Must Subscribe Our Channel To Use This Bot</b>"
force_but = [[InlineKeyboardButton("CHANNEL", url="https://t.me/teamdumperops")]]

button = [[InlineKeyboardButton("ADD ME TO YOUR GROUP", url="https://t.me/Pickupquotesbot?startgroup=true")],
        [InlineKeyboardButton("SUPPORT", url="https://t.me/dumpersuppport")]]

button2 = [[InlineKeyboardButton("CLICK TO COPY", url="https://t.me/teamdumperops")]]
start_but = [[("GET PICKUP QUOTE")], [("ABOUT")]]
storage = "oxcqpm"

@bot.on_message(filters.command("start") & filters.private)
async def start(bot, msg):
    if force:
        try:
            user = await bot.get_chat_member(force, msg.from_user.id)
            if user.status:
                reply = InlineKeyboardMarkup(button)
                text1 = "<b>Hello, Welcome To Pickup Quotes Bot\n\nWanna Impress Your Crush ❤\n\nGet Pickup Quotes For Ur Crush ❤\n\n</b>"
                reply_markup1 = ReplyKeyboardMarkup(start_but, one_time_keyboard=False, resize_keyboard=True)
                await msg.reply_text(text=text1, reply_markup=reply)
                await msg.reply_text(text="<b>Use Button To Get Quotes</b>", reply_markup=reply_markup1)
        except UserNotParticipant:
            text = force_message
            reply_markup = InlineKeyboardMarkup(force_but)
            await msg.reply_text(text=text, reply_markup=reply_markup)

@bot.on_message(filters.command("start") & filters.group)
async def start(bot, msg):
    await msg.reply_text("<b>Use /pickupline To Get Quote</b>")

@bot.on_message(filters.command("pickupline") & filters.group)
async def start2(bot, msg):
    rndm = random.randint(1, 362)
    replymark = InlineKeyboardMarkup(button2)
    randum = await bot.get_messages(storage, message_ids=rndm)
    await msg.reply(text="<b>" + randum.text + "</b>")

@bot.on_message(filters.command("pickupline") & filters.private)
async def start3(bot, msg):
    rndm = random.randint(0, 362)
    replymark = InlineKeyboardMarkup(button2)
    randum = await bot.get_messages(storage, message_ids=rndm)
    await msg.reply(text="<b>" + randum.text + "</b>")

@bot.on_message(filters.regex("GET PICKUP QUOTE") & filters.private)
async def getz(bot, msg):
    try:
        user = await bot.get_chat_member(force, msg.from_user.id)
        if user.status:
            rndm = random.randint(0, 362)
            randum = await bot.get_messages(storage, message_ids=rndm)
            replymark = InlineKeyboardMarkup(button2)
            await msg.reply(text="<b>" + randum.text + "</b>")
    except UserNotParticipant:
        text = force_message
        reply_markup = InlineKeyboardMarkup(force_but)
        await msg.reply_text(text=text, reply_markup=reply_markup)

@bot.on_message(filters.regex("ABOUT") & filters.private)
async def gotcha(bot, msg):
    xxx = await bot.get_messages(storage, 363)
    await msg.reply(text="<b>" + xxx.text + "</b>")

@bot.on_message(filters.command("ping") & filters.group)
async def ping(bot, msg):
    await msg.reply_text("<b>PONG!!\nIAM ALIVE BABE</b>")

print("Bot Is Alive")
bot.run()
