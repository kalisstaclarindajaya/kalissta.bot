from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, filters, MessageHandler


key_token = "6367302968:AAFzDOgLBQWInlqZPf1JRSIhEQcB6rtwlus" #Masukkan KEY_TOKEN BOT
user_bot = "kalissta1_bot" #masukkan @user bot


async def  start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Gunakan /help untuk menampilkan apa yang dapat saya berikan...")

async def  help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("kirim pesan, bot akan membalas.. \nList topik obrolan yang dapat kamu gunakan: \n1. oi \n2. haii \n3. selamat pagi / selamat siang / selamat malam \n4. siapa kamu? \n5. apa yang bisa kamu lakukan disini? \n6. apakah kamu tahu bagaimana suara kucing? \n7. apakah kamu tahu bagaimana suara buaya? \n8. kamu tahu apa yang lucu? \n9. apakah kamu lelah? \n10. apa yang kamu butuhin sekarang? \n11. menurutmu lebih sakit terkena jarum atau terkena pisau? \n12. senang bisa chattingan denganmu")


async def text_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text_diterima : str = update.message.text
    print(f"Pesan diterima : {text_diterima}")
    text_lwr_diterima = text_diterima.lower()
    if 'oi' in text_lwr_diterima:
        await update.message.reply_text("wahhh, kamu sopan sekali😁")
    elif 'haii' in text_lwr_diterima:
        await update.message.reply_text("hai hai haiii")
    elif 'selamat pagi' in text_lwr_diterima:
        await update.message.reply_text("pagii, semangat buat hari ini..")
    elif 'selamat siang' in text_lwr_diterima:
        await update.message.reply_text("siangg, tetap semangat jalanin harinya..")
    elif 'selamat malam' in text_lwr_diterima:
        await update.message.reply_text("malamm, jangan lupa istirahat yaa..")
    elif 'siapa kamu?' in text_lwr_diterima:
        await update.message.reply_text(f"aku adalah {user_bot}")
    elif 'apa yang bisa kamu lakukan disini?' in text_lwr_diterima:
        await update.message.reply_text("aku bisa menemanimu walau hanya melalui chattingan..")
    elif 'apakah kamu tahu bagaimana suara kucing?' in text_lwr_diterima:
        await update.message.reply_text("miaww miaww🐱")
    elif 'apakah kamu tahu bagaimana suara buaya?' in text_lwr_diterima:
        await update.message.reply_text("kalau aku chat ada yang marah ga ya? \naku cuma chat sama kamu doang kok.. \ngimana kalo pindah ke whatsapp? kalau di DM takut numpuk \naku janji kalo aku bakalan setia \nmasa cewe secantik kamu ga punya pacar \n")
    elif 'kamu tahu apa yang lucu?' in text_lwr_diterima:
        await update.message.reply_text("yang lucu adalah ketika dia hanya bercanda seharusnya kamu tertawa bukannya menyimpan rasa")
    elif 'apakah kamu lelah?' in text_lwr_diterima:
        await update.message.reply_text("yaa, aku lelah menunggu dia yang tidak pasti..")
    elif 'apa yang kamu butuhin sekarang?' in text_lwr_diterima:
        await update.message.reply_text("aku butuh kepastian darinya karena sampai sekarang belum juga dikasih kepastian.. \n\n🎶mau dibawa kemana hubungan kita")
    elif 'menurutmu lebih sakit terkena jarum atau terkena pisau?' in text_lwr_diterima:
        await update.message.reply_text("menurutku yang lebih sakit adalah ketika kamu mau cemburu tapi gapunya hak karena bukan siapa siapanya")
    elif 'senang bisa chattingan denganmu' in text_lwr_diterima:
        await update.message.reply_text("aku juga senang bisa chatingan denganmu..")
    else:
        await update.message.reply_text("maaf bot tidak mengerti")

    
async def photo_message(update: Update, context:ContextTypes.DEFAULT_TYPE):
    return await update.message.reply_text("wahh gambar kamu bagus banget..")
        
async def  error(update: Update, context:ContextTypes.DEFAULT_TYPE):
    print(f"error... : {context.error}")


if __name__ == '__main__':
    print("Mulai")
    app = Application.builder().token(key_token).build()
    #COMMAND :
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    #MESSAGE:
    app.add_handler(MessageHandler(filters.TEXT, text_message))
    app.add_handler(MessageHandler(filters.PHOTO, photo_message))
    #error :
    app.add_error_handler(error)
    #polling :
    app.run_polling(poll_interval=1)