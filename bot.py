import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from sites.pornhub import phub
from sites.dl import ydl


bot = Client(
    'SearcherBot',
    api_hash="",
    api_id=,
    bot_token=""
)

async def progress(current, total, client, info):
            percent = f"⬆️Subiendo video\n\n{current * 100 / total:.2f}%"
            await asyncio.sleep(.5)
            await info.edit(percent)


@bot.on_message()
async def msg_handler(client, message: Message):
    username = message.from_user.username
    name = message.from_user.first_name
    if message.text == '/start':
        await message.reply(f"Hola [{name}](https://t.me/{username}), cuando desees puedes comenzar a buscar", disable_web_page_preview=True, reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton("Ayuda", callback_data='help')
            ]]
            ))
    elif message.text == '/help':
        await message.reply_text("""
📤Solo envie el nombre de el/la actriz/actor/video/
similitud que desea buscar, se mostraran los 
primeros 🗒10 resultados de su busqueda, tal 
y como si lo buscara en Pornhub🧡🖤.\n

Si desea descargar los videos con los mismos 
links que el bot le proporciona puede hacerlo,
solo envielos y el bot se lo subira, la calidad
predeterminada de los videos es 720p o la menor 
que tenga el video a esa, ya que no se puede 
elegir calidad

Esperamos que disfrute de __@PornhubSearcherBot__🖤🧡""")

    elif message.text.startswith("https://es.pornhub.com/"):

        m = await message.reply("OwO, descargando, para luego ser subido U.U")

        fname = await ydl(message.text)

        await m.delete()

        info = await message.reply(f"⬆️Subiendo video: {fname}", quote=True)
        
        await message.reply_document(fname, progress=progress, progress_args=(client, info), thumb="weloveporn.jpg")

        await info.delete()
        await message.reply("Video Subido correctamente✅, disfrute el nopor coshino😈")
    
    elif message.text: 
        sp = phub(message.text)
        await message.reply_photo(photo="weloveporn.jpg")
        msg = f"Resultados de {message.text} en __@PornhubSearcherBot__\n\n"
        
        for i in sp:
            msg += i.a.get('title')+"\n"
            msg += f"[Link al video](https://es.pornhub.com{i.a.get('href')})\n\n"    

        await message.reply(msg, disable_web_page_preview=True)


@bot.on_callback_query(filters.regex('help'))
async def query_help(client, query):
    await query.answer("Ayudando...")
    await query.message.edit("""
📤Solo envie el nombre de el/la actriz/actor/video/
similitud que desea buscar, se mostraran los 
primeros 🗒10 resultados de su busqueda, tal 
y como si lo buscara en Pornhub🧡🖤.\n

Si desea descargar los videos con los mismos 
links que el bot le proporciona puede hacerlo,
solo envielos y el bot se lo subira, la calidad
 predeterminada de los videos es la maxima, 
ya que no se puede elegir calidad

Esperamos que disfrute de __@PornhubSearcherBot__""")
       

if __name__ == '__main__':
    print("Bot iniciado")
    bot.run()
