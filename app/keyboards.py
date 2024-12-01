from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
InlineKeyboardMarkup, InlineKeyboardButton)

from aiogram.utils.keyboard import InlineKeyboardBuilder

from app.database.requests import get_townCategoies, get_town

main = ReplyKeyboardMarkup(keyboard = [
    [KeyboardButton(text='Климатические параменты холодного периода')]
  ],
  resize_keyboard=True, input_field_placeholder='выбери пункт меню'
)

async def categories():
    all_categories = await get_townCategoies()
    keyboard = InlineKeyboardBuilder()
    for category in all_categories:
        keyboard.add(InlineKeyboardButton(text = category.Column_Town,callback_data = f'category_{category.Column_Id}'))
    return keyboard.adjust(1).as_markup()

async def items(Column_Id):
    all_items = await get_town(Column_Id)
    keyboard = InlineKeyboardBuilder()
    for item in all_items:
        keyboard.add(InlineKeyboardButton(text = item.Column_3, callback_data = f'items_{item.Column_Id}'))
    return keyboard.adjust(1).as_markup()