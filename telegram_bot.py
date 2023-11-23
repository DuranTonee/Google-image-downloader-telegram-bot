from icrawler.builtin import GoogleImageCrawler
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from create_bot import bot
import os

class FSMDownloader(StatesGroup):
    keyword = State()
    img_license = State()
    color = State()
    number = State()


colors = ["No filter 🌐", "Black and white 🔘", "Transparent 🌀", "Red 🔴", "Orange 🟠", "Yellow 🟡",
          "Green 🟢", "Teal 🧊", "Blue 🔵", "Purple 🟣", "Pink 🎀", "White ⚪️", "Gray 💿", "Black ⚫️", "Brown 🟤"]

# @dp.message_handler(commands="start", state=None)
async def start(message: types.Message):
    await FSMDownloader.keyword.set()
    await message.answer("Enter a keyword for images.")

# @dp.message_handler(state=FSMDownloader.keyword)
async def load_keyword(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["keyword"] = message.text
    await FSMDownloader.next()
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.row('noncommercial', 'commercial')
    await message.answer("What about a license?", reply_markup=keyboard)

async def load_licence(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["license"] = message.text
    keyboard = types.ReplyKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=True)
    button1 = colors[0]
    button2 = colors[1]
    button3 = colors[2]
    button4 = colors[3]
    button5 = colors[4]
    button6 = colors[5]
    button7 = colors[6]
    button8 = colors[7]
    button9 = colors[8]
    button10 = colors[9]
    button11 = colors[10]
    button12 = colors[11]
    button13 = colors[12]
    button14 = colors[13]
    keyboard.row(button1, button2, button3)
    keyboard.row(button4, button5, button6)
    keyboard.row(button7, button8, button9)
    keyboard.row(button10, button11, button12)
    keyboard.row(button13, button14)
    await FSMDownloader.next()
    await message.answer("Do you need a color filter?", reply_markup=keyboard)

# @dp.message_handler(state=FSMDownloader.color)
async def load_color(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["color"] = message.text    
        if data["color"] == "No filter 🌐":
            data['filter_color'] = "color"
        elif data["color"] == "Black and white 🔘":
            data['filter_color'] = "blackandwhite"
        elif data["color"] == "Transparent 🌀":
            data['filter_color'] = "transparent"
        elif data["color"] == "Red 🔴":
            data['filter_color'] = "red"
        elif data["color"] == "Orange 🟠":
            data['filter_color'] = "orange"
        elif data["color"] == "Yellow 🟡":
            data['filter_color'] = "yellow"
        elif data["color"] == "Green 🟢":
            data['filter_color'] = "green"
        elif data["color"] == "Teal 🧊":
            data['filter_color'] = "teal"
        elif data["color"] == "Blue 🔵":
            data['filter_color'] = "blue"
        elif data["color"] == "Purple 🟣":
            data['filter_color'] = "purple"
        elif data["color"] == "Pink 🎀":
            data['filter_color'] = "pink"
        elif data["color"] == "White ⚪️":
            data['filter_color'] = "white"
        elif data["color"] == "Gray 💿":
            data['filter_color'] = "gray"
        elif data["color"] == "Black ⚫️":
            data['filter_color'] = "black"
        elif data["color"] == "Brown 🟤":
            data['filter_color'] = "brown"
        else:
            await message.answer("Use a keyboard below.")
            return

    await FSMDownloader.next()
    await message.answer("How many images do you need? (below 10)")

# @dp.message_handler(state=FSMDownloader.number)
async def load_number(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        try: 
            data['number'] = int(message.text)
        except ValueError:
            await message.answer("Enter a valid value")
            return

        if data['number'] > 10:
            await message.answer("Enter a value less than 10")
            return
        else:

            await message.answer("Okay, starting. Wait a sec...")
            img_keyword = data["keyword"]
            filters = dict(color=data['filter_color'],
                           license=data['license'])
            crawler = GoogleImageCrawler(storage={'root_dir': 'images'})
            crawler.crawl(keyword=img_keyword,
                          max_num=data['number'],
                          overwrite=True,
                          filters=filters
                          )
    
    button_start = "/start"
    keyboard_start = types.ReplyKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=True)
    keyboard_start.add(button_start)

    files = sorted(os.listdir('images'))
    for filename in files:
        with open(f'images/{filename}', 'rb') as path:
            await bot.send_document(message.chat.id, document=path, reply_markup=keyboard_start)
            os.remove(f"images/{filename}")

    await state.finish()

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start, commands="start", state=None)
    dp.register_message_handler(load_keyword, state=FSMDownloader.keyword)
    dp.register_message_handler(load_licence, state=FSMDownloader.img_license)
    dp.register_message_handler(load_color, state=FSMDownloader.color)
    dp.register_message_handler(load_number, state=FSMDownloader.number)
