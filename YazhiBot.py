from os import environ
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from pyrogram.errors import UserNotParticipant

bot = Client(
            "BOT",
            api_id = int(environ["API_ID"]),
            api_hash = environ["API_HASH"],
            bot_token = "5120333138:AAGCO_JjUIRrjq7CQRAa7ei4JKjeHtwGzX0"
)

send = "qmpzwvc"

caption = "<b>Uninstall old app\n\nInstall new\n\nMore stable app ❤\n\nShare feedback 👍</b>"

force_channel = "yazhi_org"

start_message = "<b>Hello, Welcome To Our Mods Bot</b>"

force_message = "<b>You Must Subscribe Our Channel To Use This Bot</b>"

force_msg_but = [[InlineKeyboardButton("CHANNEL", url="https://t.me/yazhi_ORG")]]

start_msg_but = [[("MODS")], [("ABOUT")], [("REQUEST/FEEDBACK")]]

mods_msg_butt = [[("NETFLIX"), ("HOTSTAR")], [("PRIME VIDEO"), ("VOOT")], [("ZEE5"), ("ULLU")], [("SONY LIV"), ("RESSO")], [("ALT BALAJI"), ("IPL MOD")], [("BACK")]]

@bot.on_message(filters.command("start") & filters.private)
async def start(bot, msg):
    if force_channel:
        try:
            user = await bot.get_chat_member(force_channel, msg.from_user.id)
            if user.status:
                text1 = "<b>Hello, Welcome To Yazhi's Mods Bot\n\n1. You Can Get Mods Here ❤\n\n2. You Will Get Our New Updates ❤\n\n</b>"
                reply_markup1= ReplyKeyboardMarkup(start_msg_but, one_time_keyboard=True, resize_keyboard=True)
                await msg.reply_text(text=text1, reply_markup=reply_markup1)
                await msg.reply_text(text="<b>Use The Buttons To Control Me</b>")

        except UserNotParticipant:
            ReplyKeyboardRemove(True)
            text = force_message
            reply_markup = InlineKeyboardMarkup(force_msg_but)
            await msg.reply_text(text=text, reply_markup=reply_markup)

@bot.on_message(filters.regex("ABOUT") & filters.private)
async def abt(bot, msg):
    try:
        user = await bot.get_chat_member(force_channel, msg.from_user.id)
        if user.status:
            await msg.reply(text="<b>ABOUT\n\nYAZHI TELEGRAM BOT TO GET MODS AND NEW UPDATES OF @Yazhi_Org\n\nBOT BY : @YAZHI_ORG\n\nDEVLOPER : @Walker_Web</b>")
    except UserNotParticipant:
        ReplyKeyboardRemove(True)
        text = force_message
        reply_markup = InlineKeyboardMarkup(force_msg_but)
        await msg.reply_text(text=text, reply_markup=reply_markup)

@bot.on_message(filters.regex("REQUEST/FEEDBACK"))
async def bak(bot, msg):
    await msg.reply(text="<b>CONTACT : @DEMONOIZDZ</b>")

@bot.on_message(filters.document & filters.private)
async def file(bot, msg):
    if msg.from_user.id in [1058482162, 1153912202]:
        await msg.reply(msg.document.file_id)

@bot.on_message(filters.regex("MODS"))
async def mods(bot, msg):
    try:
        user = await bot.get_chat_member(force_channel, msg.from_user.id)
        if user.status:
            reply_markup = ReplyKeyboardMarkup(mods_msg_butt, one_time_keyboard=True, resize_keyboard=True)
            ReplyKeyboardRemove(True)
            await msg.reply_text(text="<b>CHOSE ANY MOD</b>", reply_markup=reply_markup)

    except UserNotParticipant:
        ReplyKeyboardRemove(True)
        text = force_message
        reply_markup = InlineKeyboardMarkup(force_msg_but)
        await msg.reply_text(text=text, reply_markup=reply_markup)

@bot.on_message(filters.regex("NETFLIX"))
async def nef(bot, msg):
    try:
        user = await bot.get_chat_member(force_channel, msg.from_user.id)
        if user.status:
            netflix = await bot.get_messages(send, 3)
            if netflix.text == "none":
                await msg.reply(text="<b>Mod Is Not Updated Yet, Please Wait Until We Update</b>")
            else:
                await bot.send_document(msg.chat.id, netflix.text, caption=caption)

    except UserNotParticipant:
        ReplyKeyboardRemove(True)
        text = force_message
        reply_markup = InlineKeyboardMarkup(force_msg_but)
        await msg.reply_text(text=text, reply_markup=reply_markup)

@bot.on_message(filters.regex("HOTSTAR"))
async def hot(bot, msg):
    try:
        user = await bot.get_chat_member(force_channel, msg.from_user.id)
        if user.status:
            hotstar = await bot.get_messages(send, 5)
            if hotstar.text == "none":
                await msg.reply(text="<b>Mod Is Not Updated Yet, Please Wait Until We Update</b>")
            else:
                await bot.send_document(msg.chat.id, hotstar.text, caption=caption)

    except UserNotParticipant:
        ReplyKeyboardRemove(True)
        text = force_message
        reply_markup = InlineKeyboardMarkup(force_msg_but)
        await msg.reply_text(text=text, reply_markup=reply_markup)

@bot.on_message(filters.regex("PRIME VIDEO"))
async def prm(bot, msg):
    try:
        user = await bot.get_chat_member(force_channel, msg.from_user.id)
        if user.status:
            prime = await bot.get_messages(send, 7)
            if prime.text == "none":
                await msg.reply(text="<b>Mod Is Not Updated Yet, Please Wait Until We Update</b>")
            else:
                await bot.send_document(msg.chat.id, prime.text, caption=caption)
    except UserNotParticipant:
        ReplyKeyboardRemove(True)
        text = force_message
        reply_markup = InlineKeyboardMarkup(force_msg_but)
        await msg.reply_text(text=text, reply_markup=reply_markup)

@bot.on_message(filters.regex("VOOT"))
async def vot(bot, msg):
    try:
        user = await bot.get_chat_member(force_channel, msg.from_user.id)
        if user.status:
            voot = await bot.get_messages(send, 9)
            if voot.text == "none":
                await msg.reply(text="<b>Mod Is Not Updated Yet, Please Wait Until We Update</b>")
            else:
                await bot.send_document(msg.chat.id, voot.text, caption=caption)
    except UserNotParticipant:
        ReplyKeyboardRemove(True)
        text = force_message
        reply_markup = InlineKeyboardMarkup(force_msg_but)
        await msg.reply_text(text=text, reply_markup=reply_markup)

@bot.on_message(filters.regex("ZEE5"))
async def zee(bot, msg):
    try:
        user = await bot.get_chat_member(force_channel, msg.from_user.id)
        if user.status:
            zee5 = await bot.get_messages(send, 11)
            if zee5.text == "none":
                await msg.reply(text="<b>Mod Is Not Updated Yet, Please Wait Until We Update</b>")
            else:
                await bot.send_document(msg.chat.id, zee5.text, caption=caption)
    except UserNotParticipant:
        ReplyKeyboardRemove(True)
        text = force_message
        reply_markup = InlineKeyboardMarkup(force_msg_but)
        await msg.reply_text(text=text, reply_markup=reply_markup)

@bot.on_message(filters.regex("ULLU"))
async def ulu(bot, msg):
    try:
        user = await bot.get_chat_member(force_channel, msg.from_user.id)
        if user.status:
            ullu = await bot.get_messages(send, 13)
            if ullu.text == "none":
                await msg.reply(text="<b>Mod Is Not Updated Yet, Please Wait Until We Update</b>")
            else:
                await bot.send_document(msg.chat.id, ullu.text, caption=caption)
    except UserNotParticipant:
        ReplyKeyboardRemove(True)
        text = force_message
        reply_markup = InlineKeyboardMarkup(force_msg_but)
        await msg.reply_text(text=text, reply_markup=reply_markup)

@bot.on_message(filters.regex("SONY LIV"))
async def sony(bot, msg):
    try:
        user = await bot.get_chat_member(force_channel, msg.from_user.id)
        if user.status:
            sonyliv = await bot.get_messages(send, 15)
            if sonyliv.text == "none":
                await msg.reply(text="<b>Mod Is Not Updated Yet, Please Wait Until We Update</b>")
            else:
                await bot.send_document(msg.chat.id, sonyliv.text, caption=caption)
    except UserNotParticipant:
        ReplyKeyboardRemove(True)
        text = force_message
        reply_markup = InlineKeyboardMarkup(force_msg_but)
        await msg.reply_text(text=text, reply_markup=reply_markup)

@bot.on_message(filters.regex("ALT BALAJI"))
async def alt(bot, msg):
    try:
        user = await bot.get_chat_member(force_channel, msg.from_user.id)
        if user.status:
            altbala = await bot.get_messages(send, 17)
            if altbala.text == "none":
                await msg.reply(text="<b>Mod Is Not Updated Yet, Please Wait Until We Update</b>")
            else:
                await bot.send_document(msg.chat.id, altbala.text, caption=caption)
    except UserNotParticipant:
        ReplyKeyboardRemove(True)
        text = force_message
        reply_markup = InlineKeyboardMarkup(force_msg_but)
        await msg.reply_text(text=text, reply_markup=reply_markup)

@bot.on_message(filters.regex("RESSO"))
async def rese(bot, msg):
    try:
        user = await bot.get_chat_member(force_channel, msg.from_user.id)
        if user.status:
            resso = await bot.get_messages(send, 19)
            if resso.text == "none":
                await msg.reply(text="<b>Mod Is Not Updated Yet, Please Wait Until We Update</b>")
            else:
                await bot.send_document(msg.chat.id, resso.text, caption=caption)
    except UserNotParticipant:
        ReplyKeyboardRemove(True)
        text = force_message
        reply_markup = InlineKeyboardMarkup(force_msg_but)
        await msg.reply_text(text=text, reply_markup=reply_markup)

@bot.on_message(filters.regex("IPL MOD"))
async def ipl(bot, msg):
    try:
        user = await bot.get_chat_member(force_channel, msg.from_user.id)
        if user.status:
            ipl_mod = await bot.get_messages(send, 21)
            if ipl_mod.text == "none":
                await msg.reply(text="<b>Mod Is Not Updated Yet, Please Wait Until We Update</b>")
            else:
                await bot.send_document(msg.chat.id, ipl_mod.text, caption=caption)
    except UserNotParticipant:
        ReplyKeyboardRemove(True)
        text = force_message
        reply_markup = InlineKeyboardMarkup(force_msg_but)
        await msg.reply_text(text=text, reply_markup=reply_markup)

@bot.on_message(filters.regex("BACK"))
async def back(bot, msg):
    ReplyKeyboardRemove(True)
    reply_markup1= ReplyKeyboardMarkup(start_msg_but, one_time_keyboard=True, resize_keyboard=True)
    await msg.reply_text(text="<b>Use The Buttons To Control Me</b>", reply_markup=reply_markup1)

print("*RESPAWNED*, IAM ALIVE")
bot.run()