from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
import app.database.requests as rq

import app.keyboards as kb

router = Router()

@router.message(CommandStart())
async def command_start_handler(message: Message):
    await message.answer("Hello!", reply_markup= kb.main)

@router.message(F.text == 'Климатические параменты холодного периода')
async def catalog(message: Message):
    await message.answer('Выберите интересующую область:', reply_markup= await kb.categories())


@router.callback_query(F.data.startswith('category_'))
async def category(callback: CallbackQuery):
    await callback.message.answer('Выберите город',
                                  reply_markup = await kb.items(callback.data.split('_')[1]))

@router.callback_query(F.data.startswith('items_'))
async def town_info(callback: CallbackQuery):
    town_data = await rq.get_towm_info(callback.data.split('_')[1])
    await callback.message.answer(f' Город: {town_data.Column_3}\n\n'
    f'Температура воздуха наиболее холодных суток,°C,обеспеченностью: \n'
    f'0,98 - {town_data.Column_4} °C\n'
    f'0,92 - {town_data.Column_5} °C\n\n'
    f'Температура воздуха наиболее холодной пятидневки, °C, обеспеченностью: \n'
    f'0,98 - {town_data.Column_6} °C\n'
    f'0,92 - {town_data.Column_7} °C\n\n'
    f'Температура воздуха, °C, обеспеченностью 0,94 - {town_data.Column_8} °C\n\n'
    f'Абсолютная минимальная температура воздуха,°C  - {town_data.Column_9} °C\n\n'
    f'Средняя суточная амплитуда температуры воздуха наиболее холодного месяца, °C - {town_data.Column_10}\n\n'
    f'Продолжительность, сут, и средняя температура воздуха, °C, периода со средней суточной температурой воздуха: \n'
    f'<= 0 °C : \n'
    f'продолжительность - {town_data.Column_11} сут\n'
    f'средняя температура - {town_data.Column_12} °C\n'
    f'<= 8 °C : \n'
    f'продолжительность -  {town_data.Column_13} сут\n'
    f'средняя температура - {town_data.Column_14} °C\n'
    f'<= 10 °C : \n'
    f'продолжительность - {town_data.Column_15} сут\n'
    f'средняя температура - {town_data.Column_16} °C\n\n'
    f'Средняя месячная относительная влажность воздуха наиболее холодного месяца,%  - {town_data.Column_17}%\n\n' 
    f'Средняя месячная относительная влажность воздуха в 15 ч наиболее холодного месяца,%  - {town_data.Column_18}%\n\n'
    f'Количество осадко в за ноябрь - март, мм - {town_data.Column_19} мм\n\n'
    f'Преобладающее направление ветра за декабрь - февраль - {town_data.Column_20}\n\n'
    f'Максимальная из средних скоростей ветра по румбам за январь, м/с - {town_data.Column_21} м/с\n\n'
    f'Средняя скорость ветра, м/с, за период со средней суточной температурой воздуха <= 8 °C - {town_data.Column_22} м/с\n',
                                  reply_markup = await kb.items(callback.data.split('_')[1]))


