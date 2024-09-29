## keyboards.py

from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

# main = ReplyKeyboardMarkup(
#     keyboard=[
#         [KeyboardButton(text="Каталог")],
#         [KeyboardButton(text="Корзина")],
#         [KeyboardButton(text="Контакты"), KeyboardButton(text="О нас")],
#     ],
#     resize_keyboard=True,
#     input_field_placeholder="Выберите пункт меню",
# )

# Главное меню
main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🛒 Корзина"), KeyboardButton(text="📦 Мои заказы")],
        [KeyboardButton(text="🔍 Поиск товаров"), KeyboardButton(text="ℹ️ Поддержка")],
        [KeyboardButton(text="🛠 Категории товаров")],
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите пункт меню",
)

catalog = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Процессоры", callback_data="cpu")],
        [InlineKeyboardButton(text="Видеокарты", callback_data="gpu")],
        [InlineKeyboardButton(text="Мат. платы", callback_data="motherboard")],
        [InlineKeyboardButton(text="Оперативная память", callback_data="ram")],
        [InlineKeyboardButton(text="SSD", callback_data="ssd")],
        [InlineKeyboardButton(text="Охлаждение", callback_data="cooling")],
        [InlineKeyboardButton(text="Оформить заказ", callback_data="checkout")],
    ]
)

cpu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Ryzen", callback_data="ryzen")],
        [InlineKeyboardButton(text="Intel", callback_data="intel")],
        [InlineKeyboardButton(text="Назад", callback_data="back")],
    ]
)
gpu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Nvidia", callback_data="nvidia")],
        [InlineKeyboardButton(text="AMD", callback_data="amd")],
        [InlineKeyboardButton(text="Назад", callback_data="back")],
    ]
)
motherboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="ASUS", callback_data="asus")],
        [InlineKeyboardButton(text="MSI", callback_data="msi")],
        [InlineKeyboardButton(text="Gigabyte", callback_data="gigabyte")],
        [InlineKeyboardButton(text="Назад", callback_data="back")],
    ]
)
ram = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Corsair", callback_data="corsair")],
        [InlineKeyboardButton(text="Kingston", callback_data="Kingston")],
        [InlineKeyboardButton(text="Samsung", callback_data="samsung")],
        [InlineKeyboardButton(text="Назад", callback_data="back")],
    ]
)
ssd = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Samsung", callback_data="samsung_ssd")],
        [InlineKeyboardButton(text="Western Digital", callback_data="western")],
        [InlineKeyboardButton(text="Seagate", callback_data="seagate")],
        [InlineKeyboardButton(text="Назад", callback_data="back")],
    ]
)
cooling = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Cooler Master", callback_data="cooler")],
        [InlineKeyboardButton(text="Noctua", callback_data="noctua")],
        [InlineKeyboardButton(text="Назад", callback_data="back")],
    ]
)
checkout = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Оформить заказ", callback_data="checkout")],
        [InlineKeyboardButton(text="Назад", callback_data="back")],
    ]
)

ryzen = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="AMD RYZEN 5600    10.000₽", callback_data="ryzen5600"
            )
        ],
        [
            InlineKeyboardButton(
                text="AMD RYZEN 7700    18.000₽", callback_data="ryzen7700"
            )
        ],
        [
            InlineKeyboardButton(
                text="AMD RYZEN 7700X    19.600₽", callback_data="ryzen7700x"
            )
        ],
        [
            InlineKeyboardButton(
                text="AMD RYZEN 8700    22.400₽", callback_data="ryzen8700"
            )
        ],
        [
            InlineKeyboardButton(
                text="AMD RYZEN 8700X    23.900₽", callback_data="ryzen8700x"
            )
        ],
        [
            InlineKeyboardButton(
                text="AMD RYZEN 9700X    28.560₽", callback_data="ryzen9700x"
            )
        ],
        [InlineKeyboardButton(text="AMD RYZEN 9700", callback_data="ryzen9700")],
        [InlineKeyboardButton(text="AMD RYZEN 9700X", callback_data="ryzen9700x")],
        [InlineKeyboardButton(text="AMD RYZEN 9800X", callback_data="ryzen9800x")],
        [InlineKeyboardButton(text="AMD RYZEN 9800", callback_data="ryzen9800")],
        [InlineKeyboardButton(text="Назад", callback_data="back")],
    ],
)

intel = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Intel Core i5-10300H", callback_data="i5-10300h")],
        [InlineKeyboardButton(text="Intel Core i5-10300", callback_data="i5-10300")],
        [InlineKeyboardButton(text="Intel Core i5-10300T", callback_data="i5-10300t")],
        [InlineKeyboardButton(text="Intel Core i5-10300U", callback_data="i5-10300u")],
        [InlineKeyboardButton(text="Intel Core i5-10300F", callback_data="i5-10300f")],
        [
            InlineKeyboardButton(
                text="Intel Core i7-14900KF", callback_data="i7-14900kf"
            )
        ],
    ]
)

nvidia = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="NVIDIA GeForce RTX 2070", callback_data="rtx2070")],
        [InlineKeyboardButton(text="NVIDIA GeForce RTX 2060", callback_data="rtx2060")],
        [InlineKeyboardButton(text="NVIDIA GeForce RTX 3060", callback_data="rtx3060")],
        [InlineKeyboardButton(text="NVIDIA GeForce RTX 3070", callback_data="rtx3070")],
        [InlineKeyboardButton(text="NVIDIA GeForce RTX 3090", callback_data="rtx3090")],
        [
            InlineKeyboardButton(
                text="NVIDIA GeForce RTX 3090 Ti", callback_data="rtx3090ti"
            )
        ],
        [InlineKeyboardButton(text="Назад", callback_data="back")],
    ],
)
asus = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="ASUS ROG STRIX Z490-F", callback_data="z490f")],
        [InlineKeyboardButton(text="ASUS ROG STRIX Z490", callback_data="z490")],
        [InlineKeyboardButton(text="ASUS ROG STRIX Z590", callback_data="z590")],
        [InlineKeyboardButton(text="Назад", callback_data="back")],
    ],
)
amd = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="RX Radeon 6500X", callback_data="6500x")],
        [InlineKeyboardButton(text="RX Vega 56", callback_data="vega56")],
        [InlineKeyboardButton(text="RX Vega 64", callback_data="vega64")],
        [InlineKeyboardButton(text="RX Radeon 6700XT", callback_data="6700xt")],
        [InlineKeyboardButton(text="RX Vega 7", callback_data="vega7")],
        [InlineKeyboardButton(text="RX Vega 8", callback_data="vega8")],
        [InlineKeyboardButton(text="Назад", callback_data="back")],
    ]
)
msi = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="MSI Z490-F", callback_data="msi490f")],
        [InlineKeyboardButton(text="MSI Z490", callback_data="msi490")],
        [InlineKeyboardButton(text="MSI Z590", callback_data="msi590")],
        [InlineKeyboardButton(text="Назад", callback_data="back")],
    ]
)

gigabyte = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Gigabyte Z490-D", callback_data="gigabyte490d")],
        [InlineKeyboardButton(text="Gigabyte Z490", callback_data="gigabyte490")],
        [InlineKeyboardButton(text="Gigabyte Z590", callback_data="gigabyte590")],
        [InlineKeyboardButton(text="Назад", callback_data="back")],
    ]
)

kingston = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Kingston A400", callback_data="kingstona400")],
        [InlineKeyboardButton(text="Kingston A2000", callback_data="kingstona2000")],
        [InlineKeyboardButton(text="Kingston A1000", callback_data="kingstona1000")],
        [InlineKeyboardButton(text="Назад", callback_data="back")],
    ]
)

samsung_ssd = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Samsung 970 EVO Plus", callback_data="samsung970evoplus"
            )
        ],
        [InlineKeyboardButton(text="Samsung 980 Pro", callback_data="samsung980pro")],
        [
            InlineKeyboardButton(
                text="Samsung 980 Evo Plus", callback_data="samsung980evoplus"
            )
        ],
        [InlineKeyboardButton(text="Назад", callback_data="back")],
    ],
)

western = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Western Digital WD2003FZEX", callback_data="wd2003fzex"
            )
        ],
        [
            InlineKeyboardButton(
                text="Western Digital WD2003FZEX", callback_data="wd2003fzex"
            )
        ],
        [
            InlineKeyboardButton(
                text="Western Digital WD2003FZEX", callback_data="wd2003fzex"
            )
        ],
        [InlineKeyboardButton(text="Назад", callback_data="back")],
    ]
)

seagate = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Seagate ST1000DM006", callback_data="st1000dm006")],
        [InlineKeyboardButton(text="Seagate ST1000DM006", callback_data="st1000dm006")],
        [InlineKeyboardButton(text="Seagate ST1000DM006", callback_data="st1000dm006")],
        [InlineKeyboardButton(text="Назад", callback_data="back")],
    ]
)

cooler = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Cooler Master MasterWatt 600", callback_data="coolermaster600"
            )
        ],
        [
            InlineKeyboardButton(
                text="Cooler Master MasterWatt 800", callback_data="coolermaster800"
            )
        ],
        [
            InlineKeyboardButton(
                text="Cooler Master MasterWatt 1000", callback_data="coolermaster1000"
            )
        ],
        [InlineKeyboardButton(text="Назад", callback_data="back")],
    ]
)

noctua = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Noctua NF-A12", callback_data="nf-a12")],
        [InlineKeyboardButton(text="Noctua NF-A14", callback_data="nf-a14")],
        [InlineKeyboardButton(text="Noctua NF-A16", callback_data="nf-a16")],
        [InlineKeyboardButton(text="Назад", callback_data="back")],
    ]
)

corsair = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Corsair RM850", callback_data="rm850")],
        [InlineKeyboardButton(text="Corsair RM750", callback_data="rm750")],
        [InlineKeyboardButton(text="Corsair RM650", callback_data="rm650")],
        [InlineKeyboardButton(text="Назад", callback_data="back")],
    ]
)
