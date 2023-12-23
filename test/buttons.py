from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


tugma=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="👑 Click Premium"),
            KeyboardButton(text="💳 Kartalarim"),
        ],
        [
            KeyboardButton(text="💸 To'lov" ,callback_data="payother"),
            KeyboardButton(text="💰 Balans"),
        ],
        [
            KeyboardButton(text="🔀 O'tkazmalar"),
            KeyboardButton(text="📆 Tolovlar tarixi"),
        ],
        [
            KeyboardButton(text="↙️ Kiruvchi hisoblar"),
            KeyboardButton(text="🌟 Saralangan to'lovlar"),
        ],
        [
            KeyboardButton(text="💠 Click-Hamyon"),
            KeyboardButton(text="😍 KATTA CASHBACK"),
        ],
        [
            KeyboardButton(text="🧮 Mening qarzlarim"),
        ],
        [
            KeyboardButton(text="📍 Joylarda to'lovlar"),
            KeyboardButton(text="⚙️ Sozlamalar"),
        ],
        [
            KeyboardButton(text="💌 Biz bilan aloqa"),
            KeyboardButton(text="🆕 Nima yangiliklar?"),
        ],
   
    ],
    resize_keyboard=True
)

tugma1=ReplyKeyboardMarkup(
    keyboard=[

        [
            KeyboardButton(text="⬅️ Asosiy menuga"),
        
        ],
        [
            KeyboardButton(text="🏠  Mening uyim"),
            KeyboardButton(text="✈️ Aviachipta"),
        ],
        [
            KeyboardButton(text="📱   Mobli operator"),
            KeyboardButton(text="🌐 Internet to'plamlar"),
        ],
        [
            KeyboardButton(text="🛰 Iternet provayderlar"),
            KeyboardButton(text="📺 TV"),
        ],
        [
            KeyboardButton(text="☎️ Telefoniya"),
            KeyboardButton(text="🏦 Kridit qaytarish"),
        ],
        [
            KeyboardButton(text="🏡  Komunal to'lovlar"),
            KeyboardButton(text="🌐 Hosting va domenlar"),
        ],
        [
            KeyboardButton(text="🎲 Internet xizmatlar"),
            KeyboardButton(text="🕌 Xayriya"),
        ],
        [
            KeyboardButton(text="⚖️ Soliqlar"),
            KeyboardButton(text="🏛 Davlat xizmatlari va DYHXX (GAI)"),
        ],
        [
            KeyboardButton(text="🎓  Talim "),
            KeyboardButton(text="💊 Sog'liq"),
        ],
        [
            KeyboardButton(text="🎪  Ko'ngil ochar "),
            KeyboardButton(text="🛡 Sug'urta"),
        ],
        [
            KeyboardButton(text="🚖  Taksi "),
            KeyboardButton(text="🅿️ Transport parkofka"),
        ],
        [
            KeyboardButton(text="🗞  Hisob raqamga to'lov"),
        
        ],
        [
            KeyboardButton(text="📧  Kvitansiyaga buyurtma berish"),
        
        ],
        [
            KeyboardButton(text=" ⬅️ Asosiy menuga"),
        
        ],
       ],
        resize_keyboard=True
        )


insozlamalar=ReplyKeyboardMarkup(
    keyboard=[

        [
            KeyboardButton(text="⬅️ Asosiy menuga"),
        
        ],
        [
            KeyboardButton(text="🏠  CLICK-PIN bilan tasdiqlash"),
            KeyboardButton(text="✈️ Mening do'stlarim"),
        ],
        [
            KeyboardButton(text="📱   Xabarnomalar "),
            KeyboardButton(text="🌐  Tilni o'zgartirish"),
        ],
        [
            KeyboardButton(text="🛰 Foydalanuvchi uchun qo'llanma "),
            KeyboardButton(text="📺 Malumotlarni o'chirish"),
        ],
        
        [
            KeyboardButton(text=" ⬅️ Asosiy menuga"),
        
        ],
       ],
        resize_keyboard=True
        )   


tugma2=ReplyKeyboardMarkup(
    keyboard=[

        [
            KeyboardButton(text="Bekor qilish"),
        
        ],],
        resize_keyboard=True
        )


tugma3=ReplyKeyboardMarkup(
    keyboard=[

        [
            KeyboardButton(text="⬅️ Asosiy menuga"),
        
        ],],
        resize_keyboard=True
        
        )

keyboard = InlineKeyboardMarkup(row_width=1)
buttons = [
        InlineKeyboardButton(text="★ ALOQ *** 8067 Humo ", callback_data="asosiykarta"),
        InlineKeyboardButton(text="CLICK *** 6391", callback_data="clickvisa"),
        InlineKeyboardButton(text="🆕💳 Yangi karta qo'shish ", callback_data="addcard"),
    ]
keyboard.add(*buttons)

keyboard_balans = InlineKeyboardMarkup(row_width=1)
buttons = [
        InlineKeyboardButton(text="🙈  Balansni yashirish", callback_data="yashirbalans"),
        InlineKeyboardButton(text="💳 Yangi karta qo'shish ", callback_data="addkarta"),
        InlineKeyboardButton(text="✅ Hamyonni faollashtirish", callback_data="aktivkard"),
    ]
keyboard_balans.add(*buttons)


keyboard_tarix = InlineKeyboardMarkup(row_width=1)
buttons = [
        InlineKeyboardButton(text="💸 To'lovlarni ko'rsatish", callback_data="wievtolov"),
        InlineKeyboardButton(text="Xizmatni ulash ", callback_data="addservis"),
    ]
keyboard_tarix.add(*buttons)


keyboard_saratolov=InlineKeyboardMarkup(row_width=1)
buttons=[
        InlineKeyboardButton(text="➕ Yangi qo'shish" , callback_data="addnew tolov"),
    ]
keyboard_saratolov.add(*buttons)

keyboard_tolov_izlash=InlineKeyboardMarkup(row_width=1)
buttons=[
        InlineKeyboardButton(text="izlash" , callback_data="search_tolov"),
    ]
keyboard_tolov_izlash.add(*buttons)


keyboard_pro = InlineKeyboardMarkup(row_width=1)
buttons = [
        InlineKeyboardButton(text="Oyiga 50'000 so'mga ulash ", callback_data="button_pro"),
    ]
keyboard_pro.add(*buttons)


keyboard_hamyon = InlineKeyboardMarkup(row_width=1)
buttons = [
        InlineKeyboardButton(text="✅ Hamyonni faollashtirish", callback_data="aktivhamyon"),
        InlineKeyboardButton(text="ℹ️  Click-Hamyon tariflar ", callback_data="clicktariflar"),
        InlineKeyboardButton(text="➕ Click-Hamyonni to'ldirish", callback_data="hamyonto'ldirish"),
        InlineKeyboardButton(text="💸  Hamyondan to'lov", callback_data="hamyondantolov"),
        InlineKeyboardButton(text="❌ Hamyonni yopish", callback_data="yopishhamyon"),
        InlineKeyboardButton(text="⭐️ Kartani asosiyga aylantirish", callback_data="asosiykartagaot"),
        InlineKeyboardButton(text="⬅️  Ortga", callback_data="ortgaqayt"),
    ]
keyboard_hamyon.add(*buttons)


keyboard_otkazmalar = InlineKeyboardMarkup(row_width=1)
buttons = [
        InlineKeyboardButton(text="📱  Telefon raqami orqali", callback_data="chereztel"),
        InlineKeyboardButton(text="💳 Karta raqami orqali ", callback_data="cheerekard"),
        InlineKeyboardButton(text="➕ Click-Hamyonga o'tkazma", callback_data="hamyonto'lagani"),
        InlineKeyboardButton(text="🔁O'z kartalarim orasida", callback_data="mykardscherez"),
        InlineKeyboardButton(text="💬 Telegram chat orqali", callback_data="chereztelegram"),
        InlineKeyboardButton(text=" QR kod bo'yicha o'tkazma", callback_data="cherezqr"),
        InlineKeyboardButton(text="  Meni QR kodim", callback_data="myqr"),
    ]
keyboard_otkazmalar.add(*buttons)

keyboard_cashback = InlineKeyboardMarkup(row_width=1)
buttons = [
        InlineKeyboardButton("🤝 Hamkorlik ro'yhati", callback_data="button_cashback"),
    ]
keyboard_cashback.add(*buttons)

keyboard_qazlarim = InlineKeyboardMarkup(row_width=1)
buttons = [
        InlineKeyboardButton("Boshlash", callback_data="button_begin"),
    ]
keyboard_qazlarim.add(*buttons)


pastgi_tugma = InlineKeyboardMarkup(row_width=3)
buttons = [
        InlineKeyboardButton(text="<--", callback_data="bir"),
        InlineKeyboardButton(text="1\5 ", callback_data="orta"),
        InlineKeyboardButton(text="-->", callback_data="ikki"),
    ]
pastgi_tugma.add(*buttons)