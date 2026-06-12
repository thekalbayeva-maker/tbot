import os
import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

# Бот токенін жүктеу (Сервердегі Environment Variables ішінен алады)
BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    exit("Қате: BOT_TOKEN айнымалысы табылмады! Оны сервер баптауларына қосыңыз.")

# Логтарды баптау (Бұлтта қателерді көру үшін қажет)
logging.basicConfig(level=logging.INFO)

# Бот пен Диспатчерді инициализациялау
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Кнопкаларды (Reply-клавиатура) жасау
def get_main_keyboard() -> ReplyKeyboardMarkup:
    kb = [
        [KeyboardButton(text="ℹ️ Біз туралы")],
        [KeyboardButton(text="🎯 Бағыттар"), KeyboardButton(text="📞 Контактілер")]
    ]
    return ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,  # Кнопкаларды экранға шақтау
        input_field_placeholder="Төмендегі мәзірден таңдаңыз..."
    )

# /start командасына жауап
@dp.message(CommandStart())
async def cmd_start(message: Message):
    welcome_text = (
        f"Сәлеметсіз бе, {message.from_user.full_name}! 👋\n\n"
        "**Жастар ресурстық орталығының** ресми ботына қош келдіңіз!\n"
        "Өзіңізге қажетті ақпаратты алу үшін төмендегі батырмаларды қолданыңыз."
    )
    await message.answer(welcome_text, parse_mode="Markdown", reply_markup=get_main_keyboard())

# "Біз туралы" батырмасы
@dp.message(F.text == "ℹ️ Біз туралы")
async def about_us(message: Message):
    text = (
        "🌟 **Біз туралы**\n\n"
        "Жастар ресурстық орталығы — жастардың бастамаларын қолдауға, "
        "олардың әлеуетін дамытуға және қоғамдық өмірге белсенді тартуға арналған ашық кеңістік. "
        "Біздің миссиямыз — жас буынның жарқын болашағын бірге құру!"
    )
    await message.answer(text, parse_mode="Markdown")

# "Бағыттар" батырмасы
@dp.message(F.text == "🎯 Бағыттар")
async def directions(message: Message):
    text = (
        "🎯 **Біздің негізгі жұмыс бағыттарымыз:**\n\n"
        "1️⃣ **Волонтерлық қозғалыс** — қайырымдылық іс-шаралар мен әлеуметтік жобалар.\n"
        "2️⃣ **Кәсіби бағдар беру** — жастарға мамандық таңдауда және жұмысқа орналасуда көмек көрсету.\n"
        "3️⃣ **Психологиялық-құқықтық көмек** — жастарға арналған тегін кеңестер мен қолдау.\n"
        "4️⃣ **Мәдени-бұқаралық іс-шаралар** — спорттық, интеллектуалдық және мәдени жобалар, алдағы іс-шаралар анонсы."
    )
    await message.answer(text, parse_mode="Markdown")

# "Контактілер" батырмасы
@dp.message(F.text == "📞 Контактілер")
async def contacts(message: Message):
    text = (
        "📞 **Байланыс мәліметтері:**\n\n"
        "📍 **Мекенжай:** [Сайтта көрсетілген мекенжай]\n"
        "📱 **Телефон нөмірі:** +7 (XXX) XXX-XX-XX\n"
        "📧 **Пошта:** info@jastar.kz\n\n"
        "🌐 Біздің әлеуметтік желілерімізге жазылып, жаңалықтардан қалыс қалмаңыз!"
    )
    await message.answer(text, parse_mode="Markdown")

# Ботты іске қосу функциясы
async def main():
    # Бот өшіп тұрғанда келген ескі хабарламаларды өшіру (Дұрыс жұмыс істеу үшін)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())