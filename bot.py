import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# Mensaje de bienvenida
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 ¡Hola! Soy HolaCartagenaBot.\n"
        "Te doy recomendaciones de restaurantes, playas, tours y ayudó a hacer reservas en Cartagena.\n\n"
        "¿Qué deseas saber hoy?"
    )

# Respuestas generales
async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    if "restaurante" in text:
        await update.message.reply_text(
            "🍽️ Aquí tienes restaurantes recomendados en Cartagena:\n\n"
            "⭐ **Café del Mar** — Vista al mar\n"
            "⭐ **La Mulata** — Comida local\n"
            "⭐ **Carmen Cartagena** — Alta cocina\n\n"
            "¿Quieres que te haga una reserva?"
        )

    elif "playa" in text:
        await update.message.reply_text(
            "🏖️ Playas recomendadas:\n\n"
            "🌴 Playa Blanca\n"
            "🌴 Islas del Rosario\n"
            "🌴 Bocagrande (urbana)\n\n"
            "¿Quieres un tour o transporte?"
        )

    elif "tour" in text or "tours" in text:
        await update.message.reply_text(
            "🚤 Tours disponibles:\n\n"
            "• Islas del Rosario\n"
            "• Chiva Rumbera\n"
            "• Ciudad amurallada histórica\n\n"
            "Puedo ayudarte a reservar. ¿Cuál te interesa?"
        )

    else:
        await update.message.reply_text("No entendí muy bien. ¿Qué estás buscando en Cartagena? 😊")

async def main():
    # Reemplaza tu token aquí
    TOKEN = "AQUÍ_TU_TOKEN_DEL_BOT"

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))

    print("Bot iniciado correctamente.")
    await app.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
