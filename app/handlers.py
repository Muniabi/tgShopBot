## handlers.py

from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
import app.keyboards as kb

from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

router = Router()

cart_items = []

# Список всех товаров (можно изменить по мере необходимости)
products = [
    {"name": "AMD Ryzen 5600", "price": "10.000₽", "description": "Процессор 6 ядер, 12 потоков."},
    {"name": "Intel Core i5-10300H", "price": "15.000₽", "description": "Процессор 4 ядра, 8 потоков."},
    {"name": "NVIDIA GeForce RTX 3060", "price": "40.000₽", "description": "Видеокарта с 12 ГБ GDDR6 памяти."},
    {"name": "Corsair RM850", "price": "8.000₽", "description": "Блок питания на 850 Вт, 80 Plus Gold."},
    {"name": "ASUS PRIME Z490-F", "price": "20.000₽", "description": "Материнская плата Z490."},
    {"name": "Kingston A2000", "price": "5.000₽", "description": "SSD на 1 ТБ, M.2."},
    {"name": "Cooler Master MasterWatt 650", "price": "10.000₽", "description": "Блок питания на 650 Вт, 80 Plus Gold."},
    {"name": "AMD Ryzen 5700", "price": "12.000₽", "description": "Процессор 8 ядер, 16 потоков."},
    {"name": "Intel Core i7-10700H", "price": "25.000₽", "description": "Процессор 8 ядер, 16 потоков."},
    {"name": "NVIDIA GeForce RTX 3070", "price": "50.000₽", "description": "Видеокарта с 16 ГБ GDDR6 памяти."},
    {"name": "Corsair RM650", "price": "6.000₽", "description": "Блок питания на 650 Вт, 80 Plus Gold."},
    {"name": "ASUS PRIME Z590-A", "price": "25.000₽", "description": "Материнская плата Z590."},
    {"name": "Samsung 970 EVO Plus", "price": "8.000₽", "description": "SSD на 1 ТБ, PCIe 3.0."},
    {"name": "Cooler Master MasterWatt 750", "price": "12.000₽", "description": "Блок питания на 750 Вт, 80 Plus Gold."},
    {"name": "AMD Ryzen 5800", "price": "15.000₽", "description": "Процессор 8 ядер, 16 потоков."},
    {"name": "Intel Core i9-10800H", "price": "35.000₽", "description": "Процессор 8 ядер, 16 потоков."},
    {"name": "NVIDIA GeForce RTX 3080", "price": "60.000₽", "description": "Видеокарта с 20 ГБ GDDR6X памяти."},
    {"name": "Corsair RM750", "price": "7.000₽", "description": "Блок питания на 750 Вт, 80 Plus Gold."},
    {"name": "ASUS PRIME Z590-E", "price": "30.000₽", "description": "Материнская плата Z590."},
    {"name": "Samsung 980 PRO", "price": "10.000₽", "description": "SSD на 1 ТБ, PCIe 4.0."},
    {"name": "Cooler Master MasterWatt 850", "price": "15.000₽", "description": "Блок питания на 850 Вт, 80 Plus Gold."}
]



@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Добро пожаловать! Выберите нужную опцию из меню ниже:", reply_markup=kb.main_menu)

@router.message(F.text == "🔍 Поиск товаров")
async def search_from_menu(message: Message):
    await message.answer("Введите ключевые слова для поиска товаров:")

@router.message(F.text)
async def search_products(message: Message):
    query = message.text.lower()
    matching_products = [
        product for product in products if query in product["name"].lower()
    ]

    if matching_products:
        response = "Найденные товары:\n"
        for product in matching_products:
            response += f"\n🔹 {product['name']} - {product['price']}\nОписание: {product['description']}\n"
    else:
        response = "К сожалению, по вашему запросу ничего не найдено."

    await message.answer(response)

@router.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer("Вы нажали на кнопку помощи")


@router.message(F.text == "Каталог")
async def catalog(message: Message):
    await message.answer("Выберите категорию товара", reply_markup=kb.catalog)


@router.callback_query(F.data == "cpu")
async def cpu(callback: CallbackQuery):
    await callback.answer("Вы выбрали категорию", show_alert=True)
    await callback.message.edit_text(
        "Вы выбрали категорию: Процессоры", reply_markup=kb.cpu
    )


@router.callback_query(F.data == "gpu")
async def gpu(callback: CallbackQuery):
    await callback.answer("Вы выбрали категорию", show_alert=True)
    await callback.message.edit_text(
        "Вы выбрали категорию: Видеокарты", reply_markup=kb.gpu
    )


@router.callback_query(F.data == "ram")
async def ram(callback: CallbackQuery):
    await callback.answer("Вы выбрали категорию", show_alert=True)
    await callback.message.edit_text(
        "Вы выбрали категорию: Оперативная память", reply_markup=kb.ram
    )


@router.callback_query(F.data == "ssd")
async def ssd(callback: CallbackQuery):
    await callback.answer("Вы выбрали категорию", show_alert=True)
    await callback.message.edit_text("Вы выбрали категорию: SSD", reply_markup=kb.ssd)


@router.callback_query(F.data == "motherboard")
async def motherboard(callback: CallbackQuery):
    await callback.answer("Вы выбрали категорию", show_alert=True)
    await callback.message.edit_text(
        "Вы выбрали категорию: Материнские платы", reply_markup=kb.motherboard
    )


@router.callback_query(F.data == "ryzen")
async def ryzen(callback: CallbackQuery):
    await callback.message.edit_text(
        "Процессоры RYZEN В наличии:", reply_markup=kb.ryzen
    )


@router.callback_query(F.data == "intel")
async def intel(callback: CallbackQuery):
    await callback.answer("Вы выбрали Intel")
    await callback.message.edit_text(
        "Процессоры Intel В наличии:", reply_markup=kb.intel
    )


@router.callback_query(F.data == "nvidia")
async def nvidia(callback: CallbackQuery):
    await callback.message.edit_text(
        "Видеокарты Nvidia В наличии:", reply_markup=kb.nvidia
    )


@router.callback_query(F.data == "asus")
async def asus(callback: CallbackQuery):
    await callback.message.edit_text(
        "Материнские платы ASUS В наличии:", reply_markup=kb.asus
    )


@router.callback_query(F.data == "amd")
async def amd(callback: CallbackQuery):
    await callback.message.edit_text("Видеокарты AMD В наличии:", reply_markup=kb.amd)


@router.callback_query(F.data == "msi")
async def msi(callback: CallbackQuery):
    await callback.message.edit_text(
        "Материнские платы MSI В наличии:", reply_markup=kb.msi
    )


@router.callback_query(F.data == "gigabyte")
async def gigabyte(callback: CallbackQuery):
    await callback.message.edit_text(
        "Материнские платы Gigabyte В наличии:", reply_markup=kb.gigabyte
    )


@router.callback_query(F.data == "kingston")
async def kingston(callback: CallbackQuery):
    await callback.message.edit_text(
        "Оперативная память Kingston В наличии:", reply_markup=kb.kingston
    )


@router.callback_query(F.data == "samsung")
async def samsung(callback: CallbackQuery):
    await callback.message.edit_text(
        "Оперативная память Samsung В наличии:", reply_markup=kb.samsung
    )


@router.callback_query(F.data == "corsair")
async def samsung(callback: CallbackQuery):
    await callback.message.edit_text(
        "Оперативная память Corsair В наличии:", reply_markup=kb.corsair
    )


@router.callback_query(F.data == "western")
async def western(callback: CallbackQuery):
    await callback.message.edit_text(
        "Жесткие диски Western Digital В наличии:", reply_markup=kb.western
    )


@router.callback_query(F.data == "seagate")
async def seagate(callback: CallbackQuery):
    await callback.message.edit_text(
        "Жесткие диски Seagate В наличии:", reply_markup=kb.seagate
    )


@router.callback_query(F.data == "samsung_ssd")
async def samsung(callback: CallbackQuery):
    await callback.message.edit_text(
        "SSD диски Samsung В наличии:", reply_markup=kb.samsung_ssd
    )


@router.callback_query(F.data == "cooler")
async def samsung(callback: CallbackQuery):
    await callback.message.edit_text(
        "Охлаждение Cooler Master В наличии:", reply_markup=kb.cooler
    )


@router.callback_query(F.data == "noctua")
async def noctua(callback: CallbackQuery):
    await callback.message.edit_text(
        "Охлаждение Noctua В наличии:", reply_markup=kb.noctua
    )


@router.callback_query(F.data == "back")
async def back(callback: CallbackQuery):
    await callback.answer("Вы вернулись в главное меню")
    await callback.message.edit_text(
        "Вы вернулись в главное меню", reply_markup=kb.catalog
    )


@router.callback_query(F.data == "checkout")
async def checkout(callback: CallbackQuery):
    await callback.message.answer("Вы хотите оформить заказ?")
    await callback.message.edit_reply_markup(
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Да", callback_data="confirm_checkout")],
                [InlineKeyboardButton(text="Отмена", callback_data="cancel_checkout")],
            ]
        )
    )


@router.callback_query(F.data == "confirm_checkout")
async def confirm_checkout(callback: CallbackQuery):
    await callback.message.answer("Заказ успешно оформлен")


@router.callback_query(F.data == "cancel_checkout")
async def cancel_checkout(callback: CallbackQuery):
    await callback.message.answer("Заказ отменен")
    await callback.message.edit_reply_markup(reply_markup=kb.catalog)
