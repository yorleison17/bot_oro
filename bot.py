import logging
from telegram import Bot
from telegram.ext import Application, CommandHandler

# Configuración de logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

# Credenciales
TOKEN = "7581025511:AAEdxP8cPlynjkbfeXTDzKz_9JPjSb5MRN4"
CHAT_ID = 8264626126

# --- Handlers ---
async def start(update, context):
    await update.message.reply_text("✅ Bot iniciado correctamente y listo para enviar alertas.")

# --- Main ---
def main():
    # Crear aplicación
    app = Application.builder().token(TOKEN).build()

    # Registrar comando /start
    app.add_handler(CommandHandler("start", start))

    # Confirmación al dueño SOLO UNA VEZ
    bot = Bot(TOKEN)
    try:
        bot.send_message(chat_id=CHAT_ID, text="🚀 Bot desplegado en Render y funcionando 24/7.")
    except Exception as e:
        logging.error(f"No se pudo enviar mensaje de inicio: {e}")

    # Mantener bot vivo
    app.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()
