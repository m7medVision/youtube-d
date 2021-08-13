from pytube.extract import video_id
from telegram.ext import *
from pytube import *
from telegram import *



print("Bot started :)")



updater = Updater('Your Token')
def ask_for_link(update,context):
    updater.bot.send_message(chat_id=update.effective_chat.id ,text="من فضلك ارسل رابط مقطع اليوتيوب ")
    return DOWNLOADER





def Downloader(update,context):
    try:
        link=str(update.message.text)

        Video_Url = YouTube(link)
        Video= Video_Url.streams.get_highest_resolution()
        Video.download()
        updater.bot.send_video(chat_id=update.message.chat_id, video=open(f'{Video.title}.mp4', 'rb'), supports_streaming=True,filename=f"{Video.title}" ,caption=Video.title)
        print("Done")
        pass
    except :
        updater.bot.send_message(chat_id=update.effective_chat.id , text = "هناك خطاء ما  ... \n\n ( من فضلك تأكد من الرابط )")
DOWNLOADER = 0





YouTube_handler=ConversationHandler(
    entry_points=[CommandHandler("start", ask_for_link)] , 
    states={
        DOWNLOADER :[MessageHandler(Filters.text , callback=Downloader )]
        
        },
    fallbacks=[CommandHandler("quit" , quit)]) 




updater.dispatcher.add_handler(YouTube_handler)
updater.start_polling()
updater.idle()
