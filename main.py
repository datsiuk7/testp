import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram import executor
from olxGet import olxGetf as mainOlx
import dataOlx
from datetime import datetime
users = dataOlx.users_revers
dataOlx = dataOlx.data
import os
os.system('color')
sound_in_my_terminal = False
colors = {
    "red":"\033[91m",
    "violet":"\033[95m",
    "green":"\033[92m",
    "yell":"\033[93m",
    "blue":"\033[94m",
    "white":"\033[97m",
}
time_start = datetime.now().time().strftime('%H:%M:%S')
status = {
    "Час запуску" : time_start,
    "Група" : None,
}
badAds={}
for group_id in dataOlx:
    badAds[group_id] = {}

def msg(text, color = "white"):
    color = colors[color]
    if text[:3] == "BAD":
        color = colors["red"]
    elif text[:3] == "NEW":
        color = colors["green"]
        if sound_in_my_terminal: os.system('PowerShell -c (New-Object Media.SoundPlayer "C:\\Windows\\Media\\notify.wav").PlaySync();')
    
    current_time = datetime.now().time()
    time_now = current_time.strftime('%H:%M:%S')
    print(color+"|{:^10}|{:^25}|".format(time_now, text))
    print(colors["white"]+"-"*38)

API_TOKEN = '5981502805:AAGmYbk1njt09hA3T0aQNNmh4F2RPW4XbrE'  
group_id = -1001878784957

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

statusAds = "BAD"
async def send_message_from_terminal():
    global statusAds, badAds
    while True:
        msg("Новий перебір лінків", "blue")
        for group_id in  dataOlx:
            msg(f"{'-'*30} {users.get(group_id)} {'-'*30}", "yell")
            for data in dataOlx[group_id]:
                # print(data)
                statusAdsSave = statusAds
                if statusAds == "BAD":
                    resultAds = mainOlx(dataOlx[group_id][data]["link"])
                    try:
                        statusAds, getAds = resultAds
                        if data not in badAds[group_id]:
                            badAds[group_id][data] = [0, 0, 0]
                        if statusAds == "error":
                            await asyncio.sleep(20)
                        if statusAds == "NEW":
                            badAds[group_id][data][0] += 1
                        elif statusAds == "SAME":
                            badAds[group_id][data][1] += 1                    
                        else:
                            badAds[group_id][data][2] += 1 

                        if statusAds not in status:
                            status[statusAds] = 1
                        else:
                            status[statusAds] += 1

                        if statusAds == "SAME":
                            msg(f"те саме оголошення", "violet")
                            continue
                        if not getAds:
                            msg(f"повернуто пустий результат", "red")
                            continue
                        if any(keyword.lower() in getAds['description'].lower() for keyword in dataOlx[group_id][data]["filterDelete"]) or any(keyword.lower() in getAds['title'].lower() for keyword in dataOlx[group_id][data]["filterDelete"]):
                            msg("спрацював фільтр видалення", "blue")
                            continue
                        if any(keyword.lower() in getAds['description'].lower() for keyword in dataOlx[group_id][data]["filterFind"]) or any(keyword.lower() in getAds['title'].lower() for keyword in dataOlx[group_id][data]["filterFind"]) or dataOlx[group_id][data]["filterFind"] == []:
                            if not dataOlx[group_id][data]["filterFind"] == []:
                                msg("спрацював фільтр знайдених слів(додав оголошення)", "green")
                        else:
                            msg("спрацював фільтр знайдених слів(видалив оголошення)", "red")
                            continue
                    except Exception as e:
                        msg(f"спрацювало виключення {e}", "red")
                        continue

                    await bot.send_photo(
                        chat_id = group_id,
                        caption = """
    <b>{}</b>
    💰 {} грн.
    🔑<i>{}</i>
    {}
    <a href="{}">🔗 Відкрити на OLX</a>

    {}
                        """.format(
                        
                        getAds['title'], 
                        getAds['price'], 
                        data, 
                        getAds['user_reg'], 
                        getAds['url'], 
                        getAds['description']

                        ), 
                        photo = getAds['img'],
                        parse_mode=types.ParseMode.HTML
                        )
                    await asyncio.sleep(20)
                else:
                    statusAds = "BAD"
                    if statusAds not in status:
                        status[statusAds] = 1
                    else:
                        status[statusAds] += 1
                    await asyncio.sleep(10)
                
                msg(f"{statusAdsSave}, {data} | добре, наступне")
                print()
            await asyncio.sleep(1)

def get_status_text(group_id):
    statusText = ""
    # for k, v in status.items():
    #     statusText += f"{k}: {v}\n"
    # statusText += "--------\n"
    for k, v in badAds[group_id].items():
        statusText += f"⬆{v[0]}-{v[1]}-{v[2]}⬇ : {k}\n"
    return statusText

def filters(chat_id):
    data_text = ""
    for data in dataOlx[chat_id]:
        data_text += """<i>Назва</i>: <b>{name}</b>\n<i>Видалені слова</i>: {filterDelete}\n<i>Включені слова</i>: {filterFind}\nПосилання: <a href="{link}">🔗 Відкрити на OLX</a>\n\n""".format(
            name=data,
            filterDelete=", ".join(dataOlx[chat_id][data]["filterDelete"]),
            filterFind=", ".join(dataOlx[chat_id][data]["filterFind"]),
            link=dataOlx[chat_id][data]["link"]
        )
    
    return data_text

keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
keyboard.add(types.KeyboardButton("інфо"), types.KeyboardButton("Працюєш?)"), types.KeyboardButton("Для чого бот"))
keyboard.add(types.KeyboardButton("Фільтри"), types.KeyboardButton("Статус"))

async def send_welcome_message(chat_id, text, msgId, msgText=""):
    message = await bot.send_message(
        chat_id,
        text,
        parse_mode=types.ParseMode.HTML,
        disable_web_page_preview=True,
        reply_markup=keyboard
    )
    msg(f"надсилання повідомлення <{msgText}>", "yell")
    await asyncio.sleep(15)  # Зачекати заданий час
    await bot.delete_message(message.chat.id, msgId)
    await asyncio.sleep(5)
    await bot.delete_message(message.chat.id, message.message_id)

@dp.message_handler(commands=['start'])
async def handle_start(message: types.Message):
    msg(f"{message.chat.id}", "red")
    await send_welcome_message(message.chat.id, "почнімо)", message.message_id, "start")


command_handlers = {
    "інфо": ("Можна розмістити до 5 запитів на 1 групу!", "інфо"),
    "працюєш?)": ("Так працюю))", "Працюєш?)"),
    "для чого бот": ("Бот призначений для стягнення даних із олх, та присилати відповідні оголошення задані фільтрами.", "Для чого бот"),

    "фільтри": ("", "Фільтри"),
    "статус": ("", "Статус"),
    "звук": ("", "звук"),
}

@dp.message_handler(lambda message: message.text.lower() in command_handlers.keys())
async def handle_commands(message: types.Message):
    # print(message.chat.id)
    global sound_in_my_terminal
    command_text, reply_text = command_handlers[message.text.lower()]
    if message.text.lower() == "статус":
        command_text = get_status_text(message.chat.id)
    if message.text.lower() == "фільтри":
        command_text = filters(message.chat.id)
    if message.text.lower() == "звук":
        sound_in_my_terminal = not sound_in_my_terminal
        msg("Звук включений", "green") if sound_in_my_terminal else msg("Звук вимкнено", "red")
        await send_welcome_message(message.chat.id, "Звук включений", message.message_id, "Звук включений") if sound_in_my_terminal else await send_welcome_message(message.chat.id, "Звук вимкнено", message.message_id, "Звук вимкнено")
        return
    try:
        await send_welcome_message(message.chat.id, f"Вітаю {message.from_user.full_name}!\n"+command_text, message.message_id, message.text)
    except Exception as e:
        print(f"Вітаю {message.from_user.full_name}!\n"+command_text)
        print("помилка", e)

async def on_message(message: types.Message):
    msg("надійшло повідомлення", "yell")
    time = 10
    bot_msg = await bot.send_message(message.chat.id, f"Повідомлення буде видалено через {time} секунд.", reply_markup=keyboard)
    await asyncio.sleep(2)
    await bot_msg.delete()
    await asyncio.sleep(time)
    await message.delete()

async def run_message():
    dp.register_message_handler(on_message, content_types=types.ContentTypes.TEXT)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.create_task(send_message_from_terminal())
        loop.create_task(run_message())
        loop.create_task(executor.start_polling(dp, skip_updates=True))
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        loop.close()
        msg("завершено", "green")


