from telethon import Button
from telethon import TelegramClient, events
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from Config import Config
import dns.resolver
dns.resolver.default_resolver=dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers=['8.8.8.8']
import pymongo
mydb=pymongo.MongoClient("mongodb+srv://emin:emin@cluster0.tsbm4n6.mongodb.net/?retryWrites=true&w=majority")
mydatam=mydb["data1"]
datam=mydatam["user"]
keyboard = InlineKeyboardMarkup([
    [
        InlineKeyboardButton(
            "➕ Məni Qrupa Əlavə Et ➕",
            url="http://t.me/Goldensozbot?startgroup=new",
        )
    ],
    [
        InlineKeyboardButton("🇦🇿  Bot Sahibi ", url="t.me/emin_orjinal"),
        InlineKeyboardButton("🔎 Əmrlər", callback_data="emr"),
    ],
    [
        InlineKeyboardButton(
            "✨ Yeniliklər ✨", url="https://t.me/goldenbotresmi")
    ],
])


DOCS_MESSAGE = "• **Salam** 📖\n\n• **Mən Söz Oyun Botuyam** 🎮 \n\n• **Əyləncəli vaxt Keçirmək üçün Mənimlə Oynaya bilərsən** ✍🏻 \n\n• **Oynamaq üçün məni bir qrupa əlavə edib yönetici etmək lazimdir** . 💭"
DOCS_BUTTONS = [
    [
        InlineKeyboardButton(
            "➕ Məni Qrupa Əlavə Et ➕",
            url="http://t.me/Goldensozbot?startgroup=new",
        )
    ],
    [
        InlineKeyboardButton("🇦🇿  Bot Sahibi ", url="t.me/emin_orjinal"),
        InlineKeyboardButton("🔎 Əmrlər", callback_data="eme"),
    ],
    [
        InlineKeyboardButton(
            "✨ Yeniliklər ✨", url="https://t.me/goldenbotresmi")
    ],
]           


@Client.on_callback_query()
def callback_query(client, CallbackQuery): 
     if CallbackQuery.data == "emr":
         PAGE1_TEXT = "**Bot Əmrləri Haqqinda** \n\n/game - Yeni oyun başladar\n\n/stop - Oyunu Dayandırar\n\n/rating - Qlobal İstifadəçi Sıralamasini Göstərər\n\n/kec - Bilmədiyiniz Sözü keçər"

         PAGE1_BUTTON = [
               [
                     InlineKeyboardButton("↩️ Geri Qayıt", callback_data="geer"),
               ]
         ]

         CallbackQuery.edit_message_text(
             PAGE1_TEXT,
             reply_markup = InlineKeyboardMarkup (PAGE1_BUTTON)
         )         

     elif CallbackQuery.data == "geer":
         CallbackQuery.edit_message_text( 
             DOCS_MESSAGE, 
             reply_markup = InlineKeyboardMarkup(DOCS_BUTTONS)
         ) 

START = """
• **Salam** 📖\n\n• **Mən Söz Oyun Botuyam** 🎮 \n\n• **Əyləncəli vaxt Keçirmək üçün Mənimlə Oynaya bilərsən** ✍🏻 \n\n• **Oynamaq üçün məni bir qrupa əlavə edib yönetici etmək lazimdir** . 💭
"""

    
    
    
    
    
    
"""
PRIVATE /start MESSAGE
"""
@Client.on_message(filters.command("start") & filters.private)
async def priv_start(c:Client, m:Message):
    await c.send_message(m.chat.id, START, reply_markup=keyboard)
    try:
        datam.insert_one({"_id":m.chat.id,"user":"id"})
    except:
        pass


@Client.on_message(filters.new_chat_members, group=1)
async def hg(bot: Client, msg: Message):       
    for new_user in msg.new_chat_members:
        if str(new_user.id) == str(Config.BOT_ID):
            await msg.reply(
                f'''`Hey` {msg.from_user.mention} `məni` {msg.chat.title} `qrupuna əlavə etdiyin üçün Təşəkkürlər⚡️`\n\n**Mən Söz Oyun Botuyam 🎮 • Əyləncəli vaxt Keçirmək üçün Mənimlə Oynaya bilərsən ✍🏻 ✨**''')            
            try:
                datam.insert_one({"_id"m.chat.id,"user":"id"})
            except:
                pass  
        elif str(new_user.id) == str(Config.OWNER_ID):
            await msg.reply(
                f'''{msg.from_user.mention} Sahibim İndicə Qrupa qoşuldu.''')   
