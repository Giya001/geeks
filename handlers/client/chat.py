import random

import requests
import wikipedia
from aiogram import types
from aiogram.dispatcher.filters import state
from aiogram.types import ReplyKeyboardRemove
from keyboards.inline import get_voice
from keyboards.default import get_start, get_start_admin
from loader import bot, dp, ADMIN
from utils.database import users
from states import MyStates

wikipedia.set_lang("uz")
like, dislike = 0, 0


@dp.callback_query_handler()
async def callback_query(call: types.CallbackQuery):
    global like, dislike
    data = call.data
    if data == "like":
        like += 1
        await call.answer(f"like {like}")
    elif data == "dislike":
        dislike += 1
        await call.answer(f"dislike {dislike}")


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if message.from_user.id == int(ADMIN):
        await message.answer("Assalomu alaykum Admin!", reply_markup=await get_start_admin())
    else:
        await message.answer("Assalomu alaykum botimizga xush kelibsiz!", reply_markup=await get_start_admin())
        user = users.select_users_by_id(message.from_user.id)
        if not user:
            fio = f"{message.from_user.first_name} {message.from_user.last_name} "
            users.create_user(fio, message.from_user.id, message.from_user.last_name)
            await message.answer("F.I.O kiriting:")
            await MyStates.about.set()
        elif not len(user[1]) > 0:
            await message.answer("F.I.O kiriting:")
            await MyStates.about.set()


@dp.message_handler(state=MyStates.about)
async def about(message: types.Message):
    print(("about-", message.text))
    await message.answer("Telefon nomeringizni kiritng", reply_markup=ReplyKeyboardRemove())
    await MyStates.number.set()


@dp.message_handler(state=MyStates.number)
async def number(message: types.Message):
    print("number-", message.text)
    await message.answer("O`zingiz haqida qisqacha ma`lumot bering:", reply_markup=ReplyKeyboardRemove())
    await MyStates.info.set()


@dp.message_handler(state=MyStates.info)
async def info(message: types.Message):
    await message.answer("Raxmat!!", reply_markup=ReplyKeyboardRemove())
    await state.finish()


@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await message.answer("Nima yordam kerak?", reply_markup=ReplyKeyboardRemove())


photo_id = [
    "CAACAgIAAxkBAAEMMTpmUKM-lfl66iPDPWD5AAFNiB566XwAAucMAAIa8JlLx9FMjVhVP2Q1BA",
    "CAACAgIAAxkBAAEMIxRmR3iYdWYGdr4X8_xj8PfULpSurgACSy8AAgaYuEoDarUtJAABvhY1BA",
    "CAACAgIAAxkBAAEMMTxmUKOrmBk7LS-wJNGFuUr515kdwQACHBAAAsSmWUu-HZnvjOJURjUE"

]


@dp.message_handler(commands=['sticker'])
async def sticker(message: types.Message):
    random_sticket_id = random.choice(photo_id)
    await bot.send_sticker(chat_id=message.chat.id,
                           sticker=random_sticket_id,
                           reply_markup=await get_voice())
    # await bot.send_sticker(chat_id=message.chat.id,
    #                        sticker="CAACAgIAAxkBAAEMIz9mR3t1OnHNMpJ_oAk4MVHD95DLwgACNg8AAh4J8UlSVZzp6JZtezUE",
    #                        reply_markup=await get_voice() )
    #


# @dp.message_handler(commands=['photo'])
# async def photo(message: types.Message):
#     await bot.send_photo(chat_id=message.chat.id,
#                          photo="https://storage.kun.uz/source/1/aVO4uzANUDBDpwbFJSkKelMuPvDI-RHO.jpg",
#                          caption="Sizga yoqdimi?", reply_markup=ReplyKeyboardRemove())
photo_urls = [
    "https://storage.kun.uz/source/1/aVO4uzANUDBDpwbFJSkKelMuPvDI-RHO.jpg",
    "https://static.vecteezy.com/vite/assets/photo-masthead-375-b8ae1548.webp",
    "https://images.unsplash.com/photo-1508921912186-1d1a45ebb3c1?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8cGhvdG98ZW58MHx8MHx8fDA%3D",
    "data:image/jpeg;base64,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"

]


@dp.message_handler(content_types=types.ContentType.CONTACT)
async def contact(message: types.Message):
    users.update_user(message.contact.phone_number, message.from_user.id)
    await message.answer('Qabul qilindi')


@dp.message_handler(commands=['photo'])
async def photo(message: types.Message):
    random_photo_url = random.choice(photo_urls)
    await bot.send_photo(chat_id=message.chat.id,
                         photo=random_photo_url,
                         caption="Sizga yoqdimi?",
                         reply_markup=ReplyKeyboardRemove())


@dp.message_handler(commands=['weather'])
async def weather(message: types.Message):
    res = requests.get('http://api.weatherapi.com/v1/current.json?key=637a0367057542d9936143247240705&q=Tashkent')
    if res.status_code == 200:
        response = res.json()
        print(response)
        name = response['location']['name']
        country = response['location']['country']
        tz = response['location']['tz_id']
        temp_c = response['current']['temp_c']
        text = (f"<em>Shahar</em> - <b> {name} </b>\n"
                f"<em>Davlat</em> - <b> {country} </b>\n"
                f"<em>Vaqt mintaqasi</em> - <b> {tz} </b>\n"
                f"<em>Harorat</em> - <b> {temp_c} </b>\n")
        await message.answer(text, parse_mode="HTML")


@dp.message_handler(commands=['currency'])
async def currency(message: types.Message):
    res = requests.get('https://cbu.uz/uz/arkhiv-kursov-valyut/json/')
    if res.status_code == 200:
        response = res.json()
        print(response)
        for item in response:
            ccy = item['Ccy']
            name = item['CcyNm_UZ']
            rate = item['Rate']
            if ccy == 'USD' or ccy == "EUR" or ccy == "RUB":
                text = (f"<b>{ccy}</b> \n"
                        f"1 {name} - {rate} sum")
                await message.answer(text, parse_mode='HTML')


@dp.message_handler(commands=['books'])
async def books(message: types.Message):
    res = requests.get('https://www.googleapis.com/books/v1/volumes?q=backend')
    for i in range(0, 9):
        i += 1
        if res.status_code == 200:
            response = res.json()
            book_info = response["items"][i]["volumeInfo"]

            title = book_info.get("title", "No title")
            description = book_info.get("description", "No description")
            photo = book_info["imageLinks"].get("thumbnail", "No image")
            publisher = book_info.get("publisher", "No publisher")
            published_date = book_info.get("publishedDate", "No published date")

            text = (f"<em>Nomi</em> - <b> {title} </b>\n"
                    f"<em>Qisqacha ma`lumot</em> - <b> {description} </b>\n"
                    f"<em>Photo</em> - <b> {photo} </b>\n"
                    f"<em>Yozuvchi</em> - <b> {publisher} </b>\n"
                    f"<em>Chiqarilgan sanasi</em> - <b> {published_date} </b>\n"

                    )
            await message.answer(text, parse_mode="HTML")


@dp.message_handler()
async def echo(message: types.Message):
    # await message.answer(message.text)
    # await message.reply(message.text)
    await bot.send_message(chat_id=message.chat.id, text=message.text)


@dp.message_handler(commands=['aboutme'])
async def aboutme(message: types.Message):
    user = users.get_user()  # Assuming you have a method to retrieve user information
    for user in users:
        text = (
            f"<i>FIO</i> - <b>{user.fio}</b>\n"
            f"<i>USERNAME</i> - <b>{user.username}</b>\n"
            f"<i>CHAT</i> - <b>{user.chat}</b>\n"
            f"<i>PHONE</i> - <b>{user.phone}</b>\n"
        )
        await message.answer(text=text, parse_mode="HTML")
        user(text=text, parse_mode="HTML")
