from telegram.ext import ApplicationBuilder, CommandHandler

class BaseBot:
    def __init__(self, token: str):
        self.token = token
        self.app = ApplicationBuilder().token(token).build()
        self._register_default_handlers()

    def _register_default_handlers(self):
        self.app.add_handler(CommandHandler("start", self.start))

    async def start(self, update, context):
        await update.message.reply_text("Бот запущен.")

    def run(self):
        self.app.run_polling()
