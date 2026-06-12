import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

# Сіз ұсынған Бот Токен
BOT_TOKEN = "8743390723:AAFinYf69gdeOp0PT1KSk46FivSRYi_IKjw"

# Логтарды баптау (Серверде боттың жұмысын бақылау үшін)
logging.basicConfig(level=logging.INFO)

# Бот пен Диспатчерді инициализациялау
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Батырмалар мәзірін жасау функциясы
def get_main_keyboard() -> ReplyKeyboardMarkup:
    kb = [
        [KeyboardButton(text="ℹ️ Біз туралы")],
        [KeyboardButton(text="🎯 Бағыттар"), KeyboardButton(text="📞 Контактілер")]
    ]
    return ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,  # Батырмаларды экран өлшеміне ыңғайлау
        input_field_placeholder="Төмендегі мәзірден таңдаңыз..."
    )

# /start командасына жауап (Сәлемдесу)
@dp.message(CommandStart())
async def cmd_start(message: Message):
    welcome_text = (
        f"Сәлеметсіз бе, {message.from_user.full_name}! 👋\n\n"
        "**Жастар ресурстық орталығының** ресми ботына қош келдіңіз!\n"
        "Өзіңізге қажетті ақпаратты алу үшін төмендегі батырмаларды қолданыңыз."
    )
    await message.answer(welcome_text, parse_mode="Markdown", reply_markup=get_main_keyboard())

# "ℹ️ Біз туралы" батырмасы басылғанда
@dp.message(F.text == "ℹ️ Біз туралы")
async def about_us(message: Message):
    text = (
        "🌟 **Біз туралы**\n\n"
        "Жастар ресурстық орталығы — жастардың бастамаларын қолдауға, "
        "олардың әлеуетін дамытуға және қоғамдық өмірге белсенді тартуға арналған ашық кеңістік. "
        "Біздің миссиямыз — жас буынның жарқын болашағын бірге құру!"
    )
    await message.answer(text, parse_mode="Markdown")

# "🎯 Бағыттар" батырмасы басылғанда
@dp.message(F.text == "🎯 Бағыттар")
async def directions(message: Message):
    text = (
        "🎯 **Біздің негізгі жұмыс бағыттарымыз:**\n\n"
        "1️⃣ **Волонтерлық қозғалыс** — қайырымдылық іс-шаралар мен әлеуметтік жобалар.\n"
        "2️⃣ **Кәсіби бағдар беру** — жастарға мамандық таңдауда және жұмысқа орналасуда көмек көрсету.\n"
        "3️⃣ **Психологиялық-құқықтық көмек** — жастарға арналған тегін кеңестер мен қолдау.\n"
        "4️⃣ **Мәдени-бұқаралық іс-шаралар** — спорттық, интеллектуалдық және мәдени жобалар."
    )
    await message.answer(text, parse_mode="Markdown")

# "📞 Контактілер" батырмасы басылғанда
@dp.message(F.text == "📞 Контактілер")
async def contacts(message: Message):
    text = (
        "📞 **Байланыс мәліметтері:**\n\n"
        "📍 **Мекенжай:** Жастар Орталығы ғимараты, 1-қабат\n"
        "📱 **Телефон нөмірі:** +7 (777) 123-45-67\n"
        "📧 **Пошта:** info@jastar.kz\n\n"
        "🌐 Біздің әлеуметтік желілерімізге жазылып, жаңалықтардан қалыс қалмаңыз!"
    )
    await message.answer(text, parse_mode="Markdown")

# Ботты іске қосу
async def main():
    # Бот өшіп тұрғанда келген ескі хабарламаларды өткізіп жіберу
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())