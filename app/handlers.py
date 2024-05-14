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


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply("Хай!", reply_markup=kb.main)
    await message.answer("Ну что ты голова?")


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
