## handlers.py

from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
import app.keyboards as kb
import asyncio
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import aiohttp

router = Router()

# Список всех товаров (можно изменить по мере необходимости)
products = [
    {"id": 1, "name": "AMD Ryzen 5600", "price": "10.000", "description": "Процессор 6 ядер, 12 потоков."},
    {"id": 2, "name": "AMD Ryzen 7700", "price": "18.000", "description": "Процессор 8 ядер, 16 потоков."},
    {"id": 3, "name": "AMD Ryzen 7700X", "price": "19.600", "description": "Процессор 8 ядер, 16 потоков, высокочастотный."},
    {"id": 4, "name": "AMD Ryzen 8700", "price": "22.400", "description": "Процессор 8 ядер, 16 потоков, высокочастотный."},
    {"id": 5, "name": "AMD Ryzen 8700X", "price": "23.900", "description": "Процессор 8 ядер, 16 потоков, высокочастотный."},
    {"id": 6, "name": "AMD Ryzen 9700X", "price": "28.560", "description": "Процессор 8 ядер, 16 потоков, высокочастотный."},
    {"id": 7, "name": "AMD Ryzen 9700", "price": "28.560", "description": "Процессор 8 ядер, 16 потоков."},
    {"id": 8, "name": "AMD Ryzen 9800X", "price": "28.560", "description": "Процессор 8 ядер, 16 потоков, высокочастотный."},
    {"id": 9, "name": "AMD Ryzen 9800", "price": "28.560", "description": "Процессор 8 ядер, 16 потоков."},
    {"id": 10, "name": "Intel Core i5-10300H", "price": "11.000", "description": "Процессор 4 ядра, 8 потоков, для ноутбуков."},
    {"id": 11, "name": "Intel Core i5-10300", "price": "12.000", "description": "Процессор 6 ядер, 12 потоков, для настольных компьютеров."},
    {"id": 12, "name": "Intel Core i5-10300T", "price": "13.000", "description": "Процессор 6 ядер, 12 потоков, для ноутбуков."},
    {"id": 13, "name": "Intel Core i5-10300U", "price": "14.000", "description": "Процессор 6 ядер, 12 потоков, для ноутбуков."},
    {"id": 14, "name": "Intel Core i5-10300F", "price": "15.000", "description": "Процессор 6 ядер, 12 потоков, для настольных компьютеров, без видеоядра."},
    {"id": 15, "name": "Intel Core i7-14900KF", "price": "25.000", "description": "Процессор 8 ядер, 16 потоков, высокочастотный, для настольных компьютеров."},
    {"id": 16, "name": "NVIDIA GeForce RTX 2070", "price": "50.000", "description": "Видеокарта, 8 гб памяти, 2560 ядер, 14 ГГц."},
    {"id": 17, "name": "NVIDIA GeForce RTX 2060", "price": "30.000", "description": "Видеокарта, 6 гб памяти, 2176 ядер, 14.5 ГГц."},
    {"id": 18, "name": "NVIDIA GeForce RTX 3060", "price": "25.000", "description": "Видеокарта, 12 гб памяти, 3840 ядер, 15.5 ГГц."},
    {"id": 19, "name": "NVIDIA GeForce RTX 3070", "price": "30.000", "description": "Видеокарта, 8 гб памяти, 2560 ядер, 14.5 ГГц."},
    {"id": 20, "name": "NVIDIA GeForce RTX 3090", "price": "70.000", "description": "Видеокарта, 24 гб памяти, 5888 ядер, 14.5 ГГц."},
    {"id": 21, "name": "NVIDIA GeForce RTX 3090 Ti", "price": "100.000", "description": "Видеокарта, 24 гб памяти, 5888 ядер, 14.5 ГГц, высокочастотная."},
    {"id": 22, "name": "ASUS ROG STRIX Z490-F", "price": "15.000", "description": "Материнская плата, форм-фактор ATX, Intel Z490, 4 слота памяти, 6 SATA, 2 M.2, 1 U.2, 1 HDMI, 1 DisplayPort, 1 USB 3.2 Gen 2, 1 USB 3.2 Gen 1, 1 LAN, 1 Wi-Fi, 1 Bluetooth."},
    {"id": 23, "name": "ASUS ROG STRIX Z490", "price": "25.000", "description": "Материнская плата, форм-фактор ATX, Intel Z490, 4 слота памяти, 6 SATA, 2 M.2, 1 U.2, 1 HDMI, 1 DisplayPort, 1 USB 3.2 Gen 2, 1 USB 3.2 Gen 1, 1 LAN, 1 Wi-Fi, 1 Bluetooth."},
    {"id": 24, "name": "ASUS ROG STRIX Z590", "price": "30.000", "description": "Материнская плата, форм-фактор ATX, Intel Z590, 4 слота памяти, 6 SATA, 2 M.2, 1 U.2, 1 HDMI, 1 DisplayPort, 1 USB 3.2 Gen 2, 1 USB 3.2 Gen 1, 1 LAN, 1 Wi-Fi, 1 Bluetooth."},
    {"id": 25, "name": "Cooler Master MasterWatt 600", "price": "4.500", "description": "Блок питания, 600W, надежный и эффективный."},
    {"id": 26, "name": "Cooler Master MasterWatt 800", "price": "5.500", "description": "Блок питания, 800W, надежный и эффективный."},
    {"id": 27, "name": "Cooler Master MasterWatt 1000", "price": "6.500", "description": "Блок питания, 1000W, надежный и эффективный."},
    {"id": 28, "name": "Noctua NF-A12", "price": "2.000", "description": "Вентилятор, 120мм, высокоэффективный."},
    {"id": 29, "name": "Noctua NF-A14", "price": "2.500", "description": "Вентилятор, 140мм, высокоэффективный."},
    {"id": 30, "name": "Noctua NF-A16", "price": "3.000", "description": "Вентилятор, 160мм, высокоэффективный."},
    {"id": 31, "name": "Samsung 970 EVO Plus", "price": "6.000", "description": "SSD, 1TB, NVMe, высокая скорость."},
    {"id": 32, "name": "Samsung 980 Pro", "price": "7.000", "description": "SSD, 1TB, NVMe, высокая скорость."},
    {"id": 33, "name": "Samsung 980 Evo Plus", "price": "6.500", "description": "SSD, 1TB, NVMe, высокая скорость."},
    {"id": 34, "name": "Western Digital WD2003FZEX", "price": "4.000", "description": "HDD, 2TB, 7200 об/мин."},
    {"id": 35, "name": "Seagate ST1000DM006", "price": "3.500", "description": "HDD, 1TB, 7200 об/мин."}
]

cart_items = []




# Функция для генерации кнопок товаров
def generate_product_buttons(products):
    buttons = [
        [InlineKeyboardButton(text=p['name'], callback_data=f"product_{p['id']}")]
        for p in products
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

# Общий обработчик для категорий
async def handle_category(callback: CallbackQuery, category_name: str, products_list: list):
    await callback.answer(f"Вы выбрали категорию: {category_name}")
    await callback.message.edit_text(
        f"{category_name} в наличии:",
        reply_markup=generate_product_buttons(products_list)
    )

# Обработчик для показа деталей товара
@router.callback_query(F.data.startswith("product_"))
async def show_product_details(callback: CallbackQuery):
    product_id = int(callback.data.split("_")[1])
    product = next((p for p in products if p["id"] == product_id), None)
    
    if product:
        product_info = f"📦 {product['name']}\nЦена: {product['price']}\nОписание: {product['description']}"
        await callback.message.edit_text(
            product_info,
            reply_markup=InlineKeyboardMarkup(
                inline_keyboard=[
                    [InlineKeyboardButton(text="🛒 Добавить в корзину", callback_data=f"add_to_cart_{product_id}")],
                    [InlineKeyboardButton(text="⬅️ Назад", callback_data="back_to_list")]
                ]
            )
        )

# Обработчик для добавления товара в корзину
@router.callback_query(F.data.startswith("add_to_cart_"))
async def add_to_cart(callback: CallbackQuery):
    # print(f"Callback data: {callback.data}")  # Логируем callback.data
    try:
        product_id = int(callback.data.split("_")[-1])  # Извлекаем product_id
        product = next((p for p in products if p["id"] == product_id), None)
        
        if product:
            cart_items.append(product)  # Добавляем товар в корзину
            await callback.answer(f"Товар {product['name']} добавлен в корзину.")
            await callback.message.edit_reply_markup()  # Убираем клавиатуру после добавления
        else:
            await callback.answer("Товар не найден.")
    except (IndexError, ValueError) as e:
        print(f"Ошибка: {str(e)}")  # Логируем ошибку
        await callback.answer("Ошибка: неверные данные.")


# Обработчик для возврата в список товаров
@router.callback_query(F.data == "back_to_list")
async def back_to_list(callback: CallbackQuery):
    await callback.message.edit_text(
        "Выберите товар из списка:",
        reply_markup=generate_product_buttons(products)
    )

# Обработчик для команды /start
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

    await asyncio.sleep(5)
    await message.answer("💬 Привет! Я специалист поддержки. Как я могу вам помочь? 😊")

    cancel_keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="❌ Отменить обращение", callback_data="cancel_support_request")]
    ])

    await message.answer("Если вы хотите отменить обращение, нажмите на кнопку ниже:", reply_markup=cancel_keyboard)

# Обработчик для нажатия на кнопку "отменить обращение"
@router.callback_query(F.data == "cancel_support_request")
async def cancel_support_request(callback: CallbackQuery):
    await callback.answer("✅ Обращение в поддержку отменено.")
    await callback.message.edit_reply_markup()

@router.message(F.text == "📚 Категории товаров")
async def catalog(message: Message):
    await message.answer("Выберите категорию товара", reply_markup=kb.catalog)

# Обработчик для просмотра корзины
@router.message(F.text == "🛒 Корзина")
async def view_cart(message: Message):
    if not cart_items:
        await message.answer("Ваша корзина пуста.")
    else:
        cart_content = "Ваши товары в корзине:\n"
        for item in cart_items:
            cart_content += f"🔹 {item['name']} - {item['price']}\n"
        cart_content += "\nВыберите действие:"
        await message.answer(cart_content, reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Очистить корзину", callback_data="clear_cart")],
                [InlineKeyboardButton(text="Оплатить", callback_data="checkout")],
                [InlineKeyboardButton(text="⬅️ Назад", callback_data="back_to_list")]
            ]
        ))

# Обработчик для очистки корзины
@router.callback_query(F.data == "clear_cart")
async def clear_cart(callback: CallbackQuery):
    cart_items.clear()  # Очищаем корзину
    await callback.answer("Корзина очищена.")
    await callback.message.edit_text("Ваша корзина пуста.", reply_markup=None)


@router.callback_query(F.data == "back_to_list")
async def back_to_list(callback: CallbackQuery):
    await callback.message.edit_text(
        "Процессоры Intel В наличии:", reply_markup=kb.intel
    )


@router.callback_query(F.data == "cpu")
async def cpu(callback: CallbackQuery):
    await callback.answer("Вы выбрали категорию Процессоры")
    await callback.message.edit_text(
        "Выберите производителя процессоров:",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="AMD", callback_data="cpu_amd")],
                [InlineKeyboardButton(text="Intel", callback_data="cpu_intel")],
                [InlineKeyboardButton(text="⬅️ Назад", callback_data="back_to_category")]
            ]
        )
    )

@router.callback_query(F.data == "cpu_amd")
async def cpu_amd(callback: CallbackQuery):
    await callback.answer("Вы выбрали AMD")
    await callback.message.edit_text(
        "Процессоры AMD в наличии:",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                *[
                    [InlineKeyboardButton(text=p['name'], callback_data=f"product_{p['id']}")]
                    for p in products if "Ryzen" in p["name"]
                ],
                [InlineKeyboardButton(text="⬅️ Назад", callback_data="back_to_cpu")]  # Изменено на back_to_cpu
            ]
        )
    )

@router.callback_query(F.data == "cpu_intel")
async def cpu_intel(callback: CallbackQuery):
    await callback.answer("Вы выбрали Intel")
    await callback.message.edit_text(
        "Процессоры Intel в наличии:",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                *[
                    [InlineKeyboardButton(text=p['name'], callback_data=f"product_{p['id']}")]
                    for p in products if "Intel" in p["name"]
                ],
                [InlineKeyboardButton(text="⬅️ Назад", callback_data="back_to_cpu")]  # Изменено на back_to_cpu
            ]
        )
    )

@router.callback_query(F.data == "back_to_category")
async def back_to_category(callback: CallbackQuery):
    await callback.message.edit_text(
        "Выберите категорию товара:",
        reply_markup=kb.catalog
    )

@router.callback_query(F.data == "back_to_cpu")
async def back_to_cpu(callback: CallbackQuery):
    await callback.message.edit_text(
        "Выберите производителя процессоров:",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="AMD", callback_data="cpu_amd")],
                [InlineKeyboardButton(text="Intel", callback_data="cpu_intel")],
                [InlineKeyboardButton(text="⬅️ Назад", callback_data="back_to_category")]
            ]
        )
    )

# Дополнительные категории и производители
@router.callback_query(F.data == "gpu")
async def gpu(callback: CallbackQuery):
    await callback.answer("Вы выбрали категорию")
    await callback.message.edit_text(
        "Выберите производителя видеокарт:",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Nvidia", callback_data="gpu_nvidia")],
                [InlineKeyboardButton(text="⬅️ Назад", callback_data="back_to_category")]
            ]
        )
    )

@router.callback_query(F.data.startswith("gpu_"))
async def show_gpu_products(callback: CallbackQuery):
    manufacturer = "NVIDIA" if callback.data == "gpu_nvidia" else "AMD"
    products_list = [p for p in products if manufacturer in p["name"]]

    await callback.message.edit_text(
        f"Видеокарты {manufacturer} в наличии:",
        reply_markup=generate_product_buttons(products_list)
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

# Обработчик для оформления заказа
@router.callback_query(F.data == "checkout")
async def checkout(callback: CallbackQuery):
    if not cart_items:
        await callback.answer("Ваша корзина пуста, добавьте товары для оформления заказа.")
        return
    await callback.message.answer("Вы хотите оформить заказ?")
    await callback.message.edit_reply_markup(
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Да", callback_data="confirm_checkout")],
                [InlineKeyboardButton(text="Отмена", callback_data="cancel_checkout")],
            ]
        )
    )

@router.callback_query(F.data == "cancel_checkout")
async def cancel_checkout(callback: CallbackQuery):
    await callback.message.answer("Заказ отменен.")
    await callback.message.edit_reply_markup(reply_markup=kb.catalog)



#  Касса для оформления заказа

import aiohttp

# Функция для расчета общей суммы
def calculate_total(cart_items):
    return sum(float(item['price'].replace('.', '').replace(',', '.')) for item in cart_items)

# Функция для создания платежа
# async def create_payment(amount, description):
#     url = 'https://yoomoney.ru/api/quickpay/confirmation'
#     headers = {
#         'Authorization': f'Bearer {"97D24FDB207174DDF3D9651C4CFCEEAD89AADD5FE9077843741FA813C32D81CA"}',  # Ваш API-ключ от YooMoney
#     }
#     data = {
#         'amount': amount,
#         'currency': 'RUB',
#         'confirmation': {
#             'type': 'redirect',
#             'return_url': 'https://t.me/RaymanShopBot',  # URL, куда пользователю будет предложено вернуться
#         },
#         'description': description,
#         'capture': True,
#     }
    
#     async with aiohttp.ClientSession() as session:
#         async with session.post(url, json=data, headers=headers) as response:
#             return await response.json()

import asyncio

@router.callback_query(F.data == "confirm_checkout")
async def confirm_checkout(callback: CallbackQuery):
    # Отправляем начальное сообщение
    message = await callback.message.answer("💳 Оформление заказа. Пожалуйста, подождите...")

    # Обновляем текст с задержкой
    await asyncio.sleep(2)  # Задержка перед обновлением текста
    await message.edit_text("🕒 Обработка платежа...")

    await asyncio.sleep(2)  # Задержка перед обновлением текста
    await message.edit_text("🔍 Проверка данных...")

    await asyncio.sleep(2)  # Задержка перед обновлением текста
    await message.edit_text("✅ Платеж успешно обработан! Заказ подтвержден.")
    cart_items.clear()

    # Финальное сообщение о статусе оплаты
    await callback.message.answer("🎉 Заказ оплачен! Спасибо за покупку! ✅")




