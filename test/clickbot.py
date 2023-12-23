# from aiogram import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import Bot, Dispatcher, types,executor
from textlar import *
from buttons import *


TOKEN="6576033143:AAHfq4yxxpdW4-ZZlpGdSIO7hc6g2zh8F_g"


bot=Bot(TOKEN)
dp=Dispatcher(bot)



@dp.message_handler(text_contains="Kartalarim")
async def kartaanswer(message: types.Message):
    
    await message.answer("Sizning kartalaringiz:", reply_markup=keyboard)



@dp.message_handler(text_contains="Balans")
async def kartaanswer(message: types.Message):
   
    await message.answer(f"{balans_tekst}", reply_markup=keyboard_balans)





@dp.message_handler(text_contains="To'lov")
async def tolovanseww(message: types.Message):
    await message.answer(f"🔍 Endi servislarni Inline-rejimda qidirishingiz mumkin", reply_markup=keyboard_tolov_izlash)
    await message.answer(  "Xizmatlar turini tanlang yoki servis nomini kiriting 👇",reply_markup=tugma1)


@dp.message_handler(text_contains="O'tkazmalar")
async def otkazmalaruchun(message: types.Message):
    await message.answer(f"O'tkazma turini tanlang 👇", reply_markup=keyboard_otkazmalar)
    await message.answer( "Ortga qaytish  👇" ,reply_markup=tugma2)


@dp.message_handler(text_contains="Tolovlar tarixi")
async def balansanswer(message: types.Message):
    
    await message.answer(f"{tarix_tekst}", reply_markup=keyboard_tarix)

@dp.message_handler(text_contains=" Saralangan to'lovlar")
async def saratolovjavob(message: types.Message):
    
    await message.answer(f"{sara_tolovtekst}", reply_markup=keyboard_saratolov)



@dp.message_handler(commands=["start"])
@dp.message_handler(text_contains="Asosiy menuga")
@dp.message_handler(text_contains="Bekor qilish")
async def in_menu(message: types.Message):
    await message.answer("Kerakli bo'limni tanlang 👇", reply_markup=tugma)


@dp.message_handler(text_contains="Click Premium")
async def kartanswer(message: types.Message):
    
    await message.answer(f"{premium_text}", reply_markup=keyboard_pro)


@dp.message_handler(text_contains=" Click-Hamyon")
async def hamyonanswer(message: types.Message):
    
    await message.answer(f"{click_hamyontekst}", reply_markup=keyboard_hamyon)


@dp.message_handler(text_contains=" KATTA CASHBACK")
async def kattacashback(message: types.Message):
   
    await message.answer(f"{katta_Cashbacktekst}", reply_markup=keyboard_cashback)


@dp.message_handler(text_contains=" Mening qarzlarim")
async def myqarzlar(message: types.Message):
    
    await message.answer(f"{qarzlar_tekst}", reply_markup=keyboard_qazlarim)


@dp.message_handler(text_contains="Kiruvchi hisoblar")
async def habarkiriuvchi(message: types.Message):
    await message.answer("😊 Hozirda sizda to'lov uchun hisoblar mavjud emas")

@dp.message_handler(text_contains=" Joylarda to'lovlar")
async def joyidatolov(message: types.Message):
   
    await message.answer(f"📸 QR-kodni rasmga olib yuboring yoki USSD-kodni tering", reply_markup=tugma3)

@dp.message_handler(text_contains=" Biz bilan aloqa")
async def bizbilanaloqa(message: types.Message):
   
    await message.answer(f"Assalomu alaykum! Sizga qanday yordam bera olaman?", reply_markup=tugma3)


@dp.message_handler(text_contains="Sozlamalar")
async def sozlamalarga(message: types.Message):
   
    await message.answer(f"Kerakli bo'limni tanlang 👇", reply_markup=insozlamalar)


@dp.message_handler(text_contains="Nima yangiliklar")
async def nimayangilik(message: types.Message):
   
    await message.answer_photo("https://assets.stickpng.com/images/629e24f2974c5f2c1ceaa620.png")
    await message.answer(f"{click_yangiliktekst}", reply_markup=pastgi_tugma)

@dp.message_handler()
async def habar(message: types.Message):
    await message.answer((message.text).upper() )
    

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)



