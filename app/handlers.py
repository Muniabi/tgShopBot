## handlers.py

from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
import app.keyboards as kb
import asyncio

from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

router = Router()

cart_items = []

# Список всех товаров (можно изменить по мере необходимости)
products = [{"name": "AMD Ryzen 5600", "price": "10.000₽", "description": "Процессор 6 ядер, 12 потоков."},
    {"name": "AMD Ryzen 7700", "price": "18.000₽", "description": "Процессор 8 ядер, 16 потоков."},
    {"name": "AMD Ryzen 7700X", "price": "19.600₽", "description": "Процессор 8 ядер, 16 потоков, высокочастотный."},
    {"name": "AMD Ryzen 8700", "price": "22.400₽", "description": "Процессор 8 ядер, 16 потоков, высокочастотный."},
    {"name": "AMD Ryzen 8700X", "price": "23.900₽", "description": "Процессор 8 ядер, 16 потоков, высокочастотный."},
    {"name": "AMD Ryzen 9700X", "price": "28.560₽", "description": "Процессор 8 ядер, 16 потоков, высокочастотный."},
    {"name": "AMD Ryzen 9700", "price": "28.560₽", "description": "Процессор 8 ядер, 16 потоков."},
    {"name": "AMD Ryzen 9800X", "price": "28.560₽", "description": "Процессор 8 ядер, 16 потоков, высокочастотный."},
    {"name": "AMD Ryzen 9800", "price": "28.560₽", "description": "Процессор 8 ядер, 16 потоков."},
    {"name": "Intel Core i5-10300H", "price": "11.000₽", "description": "Процессор 4 ядра, 8 потоков, для ноутбуков."},
    {"name": "Intel Core i5-10300", "price": "12.000₽", "description": "Процессор 6 ядер, 12 потоков, для настольных компьютеров."},
    {"name": "Intel Core i5-10300T", "price": "13.000₽", "description": "Процессор 6 ядер, 12 потоков, для ноутбуков."},
    {"name": "Intel Core i5-10300U", "price": "14.000₽", "description": "Процессор 6 ядер, 12 потоков, для ноутбуков."},
    {"name": "Intel Core i5-10300F", "price": "15.000₽", "description": "Процессор 6 ядер, 12 потоков, для настольных компьютеров, без видеоядра."},
    {"name": "Intel Core i7-14900KF", "price": "25.000₽", "description": "Процессор 8 ядер, 16 потоков, высокочастотный, для настольных компьютеров."},
    {"name": "NVIDIA GeForce RTX 2070", "price": "50.000₽", "description": "Видеокарта, 8 гб памяти, 2560 ядер, 14 ГГц."},
    {"name": "NVIDIA GeForce RTX 2060", "price": "30.000₽", "description": "Видеокарта, 6 гб памяти, 2176 ядер, 14.5 ГГц."},
    {"name": "NVIDIA GeForce RTX 3060", "price": "25.000₽", "description": "Видеокарта, 12 гб памяти, 3840 ядер, 15.5 ГГц."},
    {"name": "NVIDIA GeForce RTX 3070", "price": "30.000₽", "description": "Видеокарта, 8 гб памяти, 2560 ядер, 14.5 ГГц."},
    {"name": "NVIDIA GeForce RTX 3090", "price": "70.000₽", "description": "Видеокарта, 24 гб памяти, 5888 ядер, 14.5 ГГц."},
    {"name": "NVIDIA GeForce RTX 3090 Ti", "price": "100.000₽", "description": "Видеокарта, 24 гб памяти, 5888 ядер, 14.5 ГГц, высокочастотная."},
    {"name": "ASUS ROG STRIX Z490-F", "price": "15.000₽", "description": "Материнская плата, форм-фактор ATX, Intel Z490, 4 слота памяти, 6 SATA, 2 M.2, 1 U.2, 1 HDMI, 1 DisplayPort, 1 USB 3.2 Gen 2, 1 USB 3.2 Gen 1, 1 LAN, 1 Wi-Fi, 1 Bluetooth."},
    {"name": "ASUS ROG STRIX Z490", "price": "25.000₽", "description": "Материнская плата, форм-фактор ATX, Intel Z490, 4 слота памяти, 6 SATA, 2 M.2, 1 U.2, 1 HDMI, 1 DisplayPort, 1 USB 3.2 Gen 2, 1 USB 3.2 Gen 1, 1 LAN, 1 Wi-Fi, 1 Bluetooth."},
    {"name": "ASUS ROG STRIX Z590", "price": "30.000₽", "description": "Материнская плата, форм-фактор ATX, Intel Z590, 4 слота памяти, 6 SATA, 2 M.2, 1 U.2, 1 HDMI, 1 DisplayPort, 1 USB 3.2 Gen 2, 1 USB 3.2 Gen 1, 1 LAN, 1 Wi-Fi, 1 Bluetooth."},
]



@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Добро пожаловать! Выберите нужную опцию из меню ниже:", reply_markup=kb.main_menu)

@router.message(F.text == "🔍 Поиск товаров") 
async def search_from_menu(message: Message):
    await message.answer("Введите ключевые слова для поиска товаров:", reply_markup=kb.search)
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

@router.message(F.text == "❌ Назад")
async def catalog(message: Message):
    await message.answer("Главное меню", reply_markup=kb.main_menu)

@router.message(F.text == "ℹ️ Поддержка")
async def cmd_help(message: Message):
    await message.answer("🤖 Вы нажали на кнопку помощи.\n💬 Свободный специалист поддержки напишет вам в ближайшее время.\n⏳ Ожидайте...", reply_markup=kb.main_menu)
    
    # Задержка 5 секунд перед ответом специалиста
    await asyncio.sleep(5)

    # Сообщение от специалиста
    await message.answer("💬 Привет! Я специалист поддержки. Как я могу вам помочь? 😊")
    
    # Создаём клавиатуру с кнопкой "отменить обращение"
    cancel_keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="❌ Отменить обращение", callback_data="cancel_support_request")]
    ])
    
    # Отправляем сообщение с клавиатурой
    await message.answer("Если вы хотите отменить обращение, нажмите на кнопку ниже:", reply_markup=cancel_keyboard)

# Обработчик для нажатия на кнопку "отменить обращение"
@router.callback_query(F.data == "cancel_support_request")
async def cancel_support_request(callback: CallbackQuery):
    await callback.answer("✅ Обращение в поддержку отменено.")
    await callback.message.edit_reply_markup()  # Убираем клавиатуру


@router.message(F.text == "📚 Категории товаров")
async def catalog(message: Message):
    await message.answer("Выберите категорию товара", reply_markup=kb.catalog)


@router.callback_query(F.data == "cpu")
async def cpu(callback: CallbackQuery):
    await callback.answer("Вы выбрали категорию")
    await callback.message.edit_text(
        "Вы выбрали категорию: Процессоры", reply_markup=kb.cpu
    )


@router.callback_query(F.data == "gpu")
async def gpu(callback: CallbackQuery):
    await callback.answer("Вы выбрали категорию")
    await callback.message.edit_text(
        "Вы выбрали категорию: Видеокарты", reply_markup=kb.gpu
    )


@router.callback_query(F.data == "ram")
async def ram(callback: CallbackQuery):
    await callback.answer("Вы выбрали категорию")
    await callback.message.edit_text(
        "Вы выбрали категорию: Оперативная память", reply_markup=kb.ram
    )


@router.callback_query(F.data == "ssd")
async def ssd(callback: CallbackQuery):
    await callback.answer("Вы выбрали категорию")
    await callback.message.edit_text("Вы выбрали категорию: SSD", reply_markup=kb.ssd)


@router.callback_query(F.data == "motherboard")
async def motherboard(callback: CallbackQuery):
    await callback.answer("Вы выбрали категорию")
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
