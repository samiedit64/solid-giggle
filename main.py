import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, CallbackQueryHandler

# Logging setup
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# ================= CONFIGURATION =================
BOT_TOKEN = "8705610610:AAGVEK1_M8q6KPoycE-UBfTcyCKoG2UITVI"
ADMIN_ID = 8092317887
# =================================================

# Force Subscribe Channels
REQUIRED_CHANNELS = ["@YourChannel1", "@YourChannel2"]

# Start Command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("English", callback_data="lang_en"),
         InlineKeyboardButton("Bengali", callback_data="lang_bn"),
         InlineKeyboardButton("Hindi", callback_data="lang_hi")],
        [InlineKeyboardButton("Open 101+ Monster Menu", callback_data="main_menu")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "Welcome to the Ultimate Monster All-In-One Bot!\n"
        "Please select your language to continue:",
        reply_markup=reply_markup
    )

# Callback Query Handler
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    data = query.data
    
    if data.startswith("lang_"):
        lang = data.split("_")[1].upper()
        await query.edit_message_text(
            f"Language selected: {lang}\nNow click below to open your 101 Features Menu:",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Open 101 Features Menu", callback_data="main_menu")]])
        )
        
    elif data == "main_menu":
        keyboard = [
            [InlineKeyboardButton("AI Chat & Multi-AI", callback_data="feat_ai"),
             InlineKeyboardButton("All-in-One Downloader", callback_data="feat_download")],
            [InlineKeyboardButton("AI Hashtag Generator", callback_data="feat_hashtag"),
             InlineKeyboardButton("Utility Tools Hub", callback_data="feat_tools")],
            [InlineKeyboardButton("Contact Admin / DM", callback_data="contact_admin"),
             InlineKeyboardButton("Admin Panel", callback_data="admin_panel")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "101+ Monster Features Menu\n"
            "Select any feature below to activate it instantly:",
            reply_markup=reply_markup
        )
        
    elif data == "contact_admin":
        await query.edit_message_text(
            "To contact the Bot Owner / Developer, click below:",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("DM Developer", url=f"tg://user?id={ADMIN_ID}")]])
        )
        
    elif data == "admin_panel":
        if query.from_user.id == ADMIN_ID:
            await query.edit_message_text(
                "Welcome to Master Admin Panel\n"
                "Here you can manage channels, broadcast messages, and add sub-admins.",
                reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Broadcast Message", callback_data="broadcast_msg")]]))
        else:
            await query.answer("You are not the authorized Admin of this bot!", show_alert=True)

# Main Function
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("Monster Bot is running successfully...")
    app.run_polling()

if __name__ == '__main__':
    main()
