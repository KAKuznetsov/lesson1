from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

import settings

import logging
# Enable logging
logging.basicConfig(filename="bot.log", level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    await update.message.reply_text(update.message.text)

async def talk_to_me(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    text = update.message.text
    print(text)
    await update.message.reply_text(f'Ваше сообщение: {text}')    


async def greeting_user(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    print("Вызвана команда /start")
    user = update.effective_user
    # print(user)
    # print(update)
    # print(1/0)
    await update.message.reply_html(
        rf"Привет уважаемый {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    ) 

def main():
    # mybot = Updater("settings.API_KEY")
    
    # Регулярные частые обращения за обновлениями, несколько раз в секунду
    # mybot.start_polling()
    # Чтобы бот работал постоянно, мы должны его запустить в бесконечном цилке
    # mybot.idle()

    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(settings.API_KEY).build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", greeting_user))
    # application.add_handler(CommandHandler("help", help_command))

    # on non command i.e message - echo the message on Telegram
    # application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))


    # talk to me with text 
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, talk_to_me))    

    logging.info("Bot Started!")

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)

    logging.info("Bot Started!")


if __name__ == "__main__":
    main()    