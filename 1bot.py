import os
from dotenv import load_dotenv
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram import F
from aiogram.utils.keyboard import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.enums import ParseMode


load_dotenv()
logging.basicConfig(level=logging.INFO)
bot = Bot(token=os.getenv('TOKEN'),parse_mode="HTML")
dp = Dispatcher()

#клавиатура с основным меню
def get_keyboard():
    buttons = [
        [
            types.InlineKeyboardButton(text="О нас", callback_data="about_button"),
            types.InlineKeyboardButton(text="Помощь", callback_data="help_button")
        ],
        [types.InlineKeyboardButton(text="Помощь/вопрос/консультация", callback_data="vopros_button")],
        [
            types.InlineKeyboardButton(text="Подбор техники", callback_data="podbor_button"),
            types.InlineKeyboardButton(text="Выгода лизинга", callback_data="lizing_button")
        ],
        [types.InlineKeyboardButton(text="Другие наши услуги", callback_data="other_button")],
        [types.InlineKeyboardButton(text="Решённые нами кейсы по лизингу", callback_data="case_button")],
        [
            types.InlineKeyboardButton(text="Кредитование", callback_data="kredit_button"),
            types.InlineKeyboardButton(text="Бонус", callback_data="bonus_button")
        ]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard
#клавиатура со ссылками на соц сети
def keyboard2():
    buttons = [
        [
            types.InlineKeyboardButton(text="Telegram", url="https://t.me/lisingprmlianavinkovatova"),
            types.InlineKeyboardButton(text="Instagram", url="https://www.instagram.com/lising.prm?igsh=MXVkeXNia2t6dWZnMw%3D%3D&utm_source=qr"),
            types.InlineKeyboardButton(text="VK", url="https://vk.com/lising_prm"),
        ]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

#Фабрика колбэков
def callback(cal_data,cal_text,cal_key):
    @dp.callback_query(F.data == cal_data)
    async def send_random_value(callback: types.CallbackQuery):
        global msg
        global msg1
        previous_message_id = callback.message.message_id
        try:
            await msg.delete()
        except:
            pass
        try:
            await msg1.delete()
        except:
            pass
        try:
            await bot.delete_message(chat_id=callback.message.chat.id, message_id=previous_message_id)
        except:
            pass
        try:
            await start_msg.delete()
        except:
            pass
        msg = await callback.message.answer("Выберите интересующий раздел! ", reply_markup=get_keyboard())
        msg1= await callback.message.answer(
            cal_text,
            reply_markup=cal_key)
        await callback.answer()  # /Если нужен ответ с текстом - заменить на await callback.answer(text="Спасибо что нажали!",show_alert=True)



#/start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    global start_msg
    #if message.chat.id == int(os.getenv('Channel_ID')):
    start_msg = await message.answer("Здравствуйте, спасибо Вам за подписку!",reply_markup=get_keyboard()
        )


#/колбэки вызываем через функцию callback(cal_data,cal_text,cal_key)
#О нас
callback("about_button",
         "Команда «Лизинг и брокерство» состоит из опытных финансовых специалистов, готовых оказать профессиональную помощь в любой ситуации.\n"
                "Наши сотрудники обладают высокой квалификацией и стремятся к постоянному профессиональному развитию.\n"
                "Мы являемся официальными партнёрами банков и имеем более чем 13-летний опыт в сфере финансовых услуг.\n",
         keyboard2()
         )
#Помощь
callback("help_button",
         "1. Интервью с клиентом и анализ потребностей.\n"
         "2. Анализ кредитной истории.\n"
         "3. Заключение договора.\n"
         "4. Разработка персонализированного плана.\n"
         "5. Реализация плана и успешное завершение сделки\n",
         keyboard2()
         )
#Помощь/вопрос/консультация
callback("vopros_button",
"Мы всегда готовы предоставить профессиональную консультацию по финансовым вопросам, чтобы удовлетворить потребности наших клиентов.\n"
        "Наша команда специалистов обладает широким опытом в сфере финансовых услуг и готова помочь вам принять обоснованные решения для достижения ваших финансовых целей.\n"
        "Мы подберем оптимальное решение, которое соответствует вашим потребностям и целям. Обращайтесь к нам, и мы поможем вам эффективно управлять своими финансами!\n",
         keyboard2()
         )
#Подбор техники
callback("podbor_button",
"Мы найдем наилучший вариант, который подходит к вашим требованиям и целям.\n"
        "Обращайтесь к нам, чтобы получить помощь в эффективном управлении вашими финансами!\n",
         keyboard2()
         )
#Выгода лизинга
callback("lizing_button",
"Хотите обновить своё оборудование без больших затрат? Лизинг - идеальный вариант!\n"
        "Получите необходимое имущество уже сегодня и оплатите его постепенно.\n"
        "Современная техника всегда под рукой, а обновление оборудования легко и удобно.\n"
        "Не откладывайте свой успех на потом, выберите лизинг уже сейчас!\n",
         keyboard2()
         )
#Другие наши услуги
callback("other_button",
"Дорогие клиенты, предлагаем Вам оформить с нами:\n\n"
        "1. Лизинг для юридических и физических лиц.\n"
        "2. Регистрация бизнеса открытие ИП и ООО.\n"
        "3. Анализ кредитной история для юридических и физических лиц.\n"
        "4. Страхование всех видов.\n"
        "5. Открытие расчётных счётов.\n"
        "6. Все виды кредитования для юридических и физических лиц\n"
        "7. Ипотека.\n"
        "8. Инвестирование.\n",
         keyboard2()
         )
#Решенные нами кейсы по лизингу
callback("case_button",
"1. Нагрузка клиента на ИП 15 договоров лизинга.\n"
                                  "Одобрены тягач + полуприцеп\n"
                                  "<b>Аванс 1000 рублей!</b>\n\n"
                                  "2. Банкротство директора компании в прошлом.\n"
                                  "Одобрена дорожная техника.\n"
                                  "<b>Аванс 30%. </b>\n\n"
                                  "3. Клиент с задолженностью на ФССП и с просрочками по кредитным договорам.\n"
                                  "Одобрено 2 самосвала.\n"
                                  "<b>Аванс 2%.</b> 😱\n\n"
                                  "4. Клиент с отказами Службы безопасности в лизинговых компаниях.\n"
                                  "Одобрен тягач на 10,5 млн.\n"
                                  "<b>Аванс 15%. </b>\n",
         keyboard2()
         )
#Кредитование
callback("kredit_button",
"При выборе лизинга у нас, мы рады предложить вам уникальный бонус - бесплатный анализ вашей Кредитной истории!\n"
                                  "Этот ценный подарок поможет нам лучше понять вашу финансовую ситуацию и предложить вам наилучшие условия.\n",
         keyboard2()
         )
#Бонус
callback("bonus_button",
"При оформлении кредита, вы получаете в подарок уникальный сертификат на 1000 рублей, который можно использовать в любой известной торговой сети.\n"
                                  "Данный бонус вы можете получить после выдачи кредита.\n",
         keyboard2()
         )

async def main():
    await dp.start_polling(bot)
if __name__ == "__main__":
    asyncio.run(main())