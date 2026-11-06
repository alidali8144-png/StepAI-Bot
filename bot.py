import asyncio
from baleio import Bot, Dispatcher
from baleio.filters import CommandStart
from baleio.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

TOKEN = "536607652:p8xIUjWGRQq5o8ZRlOuM4F8T4kvBSuCvNAk"
MINIAPP_URL = "https://stepai.ir/"

dp = Dispatcher()

@dp.message(CommandStart())
async def start_handler(message: Message):
    welcome_text = (
        "سلام! به StepAI خوش آمدید. 🌟\n\n"
        "برای ثبت‌نام و دریافت نام کاربری و رمز عبور، لطفاً به آیدی ادمین (@stepai) پیام دهید.\n\n"
        "پس از دریافت رمز، روی دکمه زیر کلیک کنید و وارد مینی‌اپ شوید:"
    )
    keyboard = [[InlineKeyboardButton(text="🚀 ورود به مینی‌اپ StepAI", web_app=WebAppInfo(url=MINIAPP_URL))]]
    await message.answer(welcome_text, reply_markup=InlineKeyboardMarkup(inline_keyboard=keyboard))

async def main():
    bot = Bot(token=TOKEN)
    print("✅ ربات روشن شد!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())