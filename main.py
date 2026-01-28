import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

API_TOKEN = "8318538621:AAFFK0vvmiliads_eIL2jWAZhG3jksc15wk"

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# ====== USERLAR ======
USTOZ = {
    "name": "👨‍🏫 Ustoz: Tojiev Azamat",
    "username": "True2197"
}

OQUVCHILAR = [
    {"name": "👨‍🎓 Mansurbek", "username": "rajabov_mansurbek"},
    {"name": "👨‍🎓 Bobur", "username": "ulugbekov_bobur"},
    {"name": "👨‍🎓 Nurali", "username": "khusinov7"},
    {"name": "👨‍🎓 Sayidboy", "username": "Sayidboy7"},
    {"name": "👨‍🎓 Hamrozbek", "username": "subxonberdiyev_o1"},
    {"name": "👨‍🎓 Maksim", "username": "UzMaxim"},
]

# ====== /start ======
@dp.message(Command("start"))
async def start_command(message: types.Message):
    kb = InlineKeyboardBuilder()
    kb.button(text="📩 Murojaat qilish", callback_data="contact")

    await message.answer(
        "🤖 IT Yordam Botiga xush kelibsiz!\n\n"
        "IT bo‘yicha yordam olish uchun quyidagi tugmani bosing 👇",
        reply_markup=kb.as_markup()
    )

# ====== /help ======
@dp.message(Command("help"))
async def help_command(message: types.Message):
    await message.answer(
        "🆘 Yordam:\n"
        "/start – botni ishga tushirish\n"
        "/help – yordam"
    )

# ====== MUROJAAT ======
@dp.callback_query(F.data == "contact")
async def contact_menu(callback: types.CallbackQuery):
    kb = InlineKeyboardBuilder()

    kb.button(
        text=USTOZ["name"],
        url=f"https://t.me/{USTOZ['username']}"
    )

    for o in OQUVCHILAR:
        kb.button(
            text=o["name"],
            url=f"https://t.me/{o['username']}"
        )

    kb.adjust(1)

    await callback.message.answer(
        "📞 Kim bilan bog‘lanmoqchisiz?\n\n"
        "👇 Ism ustiga bosing:",
        reply_markup=kb.as_markup()
    )
    await callback.answer()

# ====== RUN ======
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
