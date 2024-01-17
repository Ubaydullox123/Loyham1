# from bs4 import BeautifulSoup
# # from transliterate import translit
# import requests
# respons = requests.get('https://islom.uz')
# soup= BeautifulSoup(respons.text,'html.parser')
# andijon = 1
# # select tegi ichidagi optionlarni izlash
# options = soup.select('select[name="region"] option')
# # # optionlarning text va value ni chiqarish
# for option in options:
#     print(f" {option.text}, {option['value']}")



























# boshlanish
from telegram import InlineKeyboardButton,InlineKeyboardMarkup
from telegram.ext import CommandHandler,CallbackQueryHandler,MessageHandler,Updater

t = "6751046691:AAFn1W3vFyfO0CpjgHMw1Yyrzy7QSKzEpQU"

from bs4 import BeautifulSoup
# from transliterate import translit
import requests

respons = requests.get('https://islom.uz')
soup= BeautifulSoup(respons.text,'html.parser')
def mintaqani_tanlash():
    # select tegi ichidagi optionlarni izlash
    options = soup.select('select[name="region"] option')
    print(len(options))
    # optionlarning text va value ni chiqarish
    for option in options:
        return option.text

# div_elements = soup.find_all('div', class_='a')

# # Har bir div ichidagi a elementlarini izlash va ma'lumotlarni chiqarish
# for div in div_elements:
#     a_elements = div.find_all('a', class_='reg')
#     for a in a_elements:
#         print(f"href: {a['href']}, text: {a.text}")



# respons = requests.get('https://islom.uz/vaqtlar/27/12')
#
# soup= BeautifulSoup(respons.text,'html.parser')
# regions = soup.find_all('tr')
# l = []
# for i in regions:
#     a = i.find_all('td')
#     b = [h.text for h in a]
#     l.append(b)
# print(l)

def star_hand(update,context):
    update.message.reply_text(text=f"Assalamu alykum {update.message.from_user.first_name}\n"
                                   f"Shahringizni tanlang",reply_markup=InlineKeyboardMarkup(city()))


def city():
    return [
        [InlineKeyboardButton(text=f"Fergana",callback_data='37'),
        InlineKeyboardButton(text=f"Toshkent",callback_data='27')],
        [InlineKeyboardButton(text=f"Namangan", callback_data='15'),
        InlineKeyboardButton(text=f"Andijon", callback_data='1')],
        [InlineKeyboardButton(text=f"Buxoro", callback_data='4'),
         InlineKeyboardButton(text=f"Samarqand", callback_data='18')],
        [InlineKeyboardButton(text=f"Jizzax", callback_data='жиззах'),
         InlineKeyboardButton(text=f"Navoiy", callback_data='14')],
        [InlineKeyboardButton(text=f"Qashqadaryo", callback_data='93'),
         InlineKeyboardButton(text=f"Qoraqqolpoq", callback_data='андижан')],
        [InlineKeyboardButton(text=f"Surxandaryo", callback_data='наманган'),
         InlineKeyboardButton(text=f"Xorazm", callback_data='андижан')],
        [InlineKeyboardButton(text=f"Guliston", callback_data='5')]
    ]
def back():
    return [
        [InlineKeyboardButton(text="Orqaga",callback_data="back1")]]

def inline_handler(update,context):
    global region_num
    query = update.callback_query
    region_num = query.data
    respons = requests.get(f'https://islom.uz/region/{region_num}')
    soup = BeautifulSoup(respons.text, 'html.parser')
    elemets = soup.find_all(class_='p_clock')
    name_namoz = soup.find_all(class_="p_v")
    context.bot.delete_message(chat_id=query.message.chat_id, message_id=query.message.message_id)
    buttons = []
    for i,j in zip(elemets,name_namoz):
        buttons.append([InlineKeyboardButton(text=f"{j.text} : {i.text}",callback_data='1',parse_mode="HTML")])
    buttons.append([InlineKeyboardButton(text="back",callback_data='back1')])
    query.message.reply_text(text='Namoz vaqtlari',reply_markup=InlineKeyboardMarkup(buttons))
    if query.data == "back1":
        query.message.reply_text(text='tanlang',reply_markup=InlineKeyboardMarkup(city()))
def main():
    updater = Updater(token=t)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start',star_hand))
    dispatcher.add_handler(CallbackQueryHandler(inline_handler))
    updater.start_polling()
    updater.idle()

if __name__=="__main__":
    main()
# Tugash




# Boshlanish
# from telegram.ext import CommandHandler,Filters,MessageHandler,Updater,ConversationHandler,CallbackQueryHandler
# from bs4 import BeautifulSoup as BS
# from telegram import KeyboardButton,ReplyKeyboardMarkup
# from telegram import InlineKeyboardMarkup,InlineKeyboardButton
# import requests
# tokenn = "6751046691:AAFn1W3vFyfO0CpjgHMw1Yyrzy7QSKzEpQU"
#
# def start_hold(update,context):
#     update.message.reply_text(text=f"Assalomu Allaykum {update.message.from_user.first_name}"
#                                   f"{update.message.from_user.last_name} Shaxringizni tanlang",
#                                                         reply_markup=InlineKeyboardMarkup(menu3()))
#
# def menu3():
#     return [
#             [InlineKeyboardButton(text="Farg'ona", callback_data="Фарғона"),
#              InlineKeyboardButton(text="Namangan", callback_data="Наманган")],
#
#             [InlineKeyboardButton(text="Andijon", callback_data="Андижон"),
#              InlineKeyboardButton(text="Samarqand", callback_data="Самарқанд")],
#
#             [InlineKeyboardButton(text="Buxoro", callback_data="Бухоро")],
#
#             [InlineKeyboardButton(text="Rishton", callback_data="Риштон")],
#
#             [InlineKeyboardButton(text="Toshkent", callback_data="Тошкент"),
#              InlineKeyboardButton(text="Jizzax", callback_data="Жиззах")],
#
#             [InlineKeyboardButton(text="Navoiy", callback_data="Навоий"),
#              InlineKeyboardButton(text="Nukus", callback_data="Нукус")],
#     ]
# def menu4():
#     return [
#             [InlineKeyboardButton(text="Farg'ona", callback_data="Фарғона"),
#              InlineKeyboardButton(text="Namangan", callback_data="Наманган")],
#
#             [InlineKeyboardButton(text="Andijon", callback_data="Андижон"),
#              InlineKeyboardButton(text="Samarqand", callback_data="Самарқанд")],
#
#             [InlineKeyboardButton(text="Buxoro", callback_data="Бухоро")],
#
#             [InlineKeyboardButton(text="Rishton", callback_data="Риштон")],
#
#             [InlineKeyboardButton(text="Toshkent", callback_data="Тошкент"),
#              InlineKeyboardButton(text="Jizzax", callback_datata="Жиззах")],
#
#             [InlineKeyboardButton(text="Navoiy", callback_data="Навоий"),
#              InlineKeyboardButton(text="Nukus", callback_data="Нукус")],
#     ]
#
#
# def menu(update,context):
#     global data
#     query = update.callback_query
#     t = requests.get(f"https://islom.uz/")
#     html_t = BS(t.content, "html.parser")
#     for inq in html_t.select(".lang_s"):
#         tq = inq.select(".custom-select")[0].text
#         print(tq)
#         for el in html_t.select(".in_header_p"):
#             max = el.select(".p_clock")[0].text
#             max1 = el.select(".p_v ")[0].text
#             mix = el.select(".p_clock ")[1].text
#             mix1 = el.select(".p_v ")[1].text
#             min = el.select(".p_clock ")[2].text
#             min1 = el.select(".p_v ")[2].text
#             mii = el.select(".p_clock ")[3].text
#             mii1 = el.select(".p_v ")[3].text
#             mis = el.select(".p_clock ")[4].text
#             mis1 = el.select(".p_v ")[4].text
#             mil = el.select(".p_clock ")[5].text
#             mil1 = el.select(".p_v ")[5].text
#             t_max = max[::]
#             t_mix = mix[::]
#             t_min = min[::]
#             t_mii = mii[::]
#             t_mis = mis[::]
#             t_mil = mil[::]
#             t_max1 = max1[::]
#             t_mix1 = mix1[::]
#             t_mia1 = mii1[::]
#             t_min1 = min1[::]
#             t_mis1 = mis1[::]
#             t_mil1 = mil1[::]
#         if query.data in tq:
#             button = [[InlineKeyboardButton(text="Orqaga qaytish", callback_data="back")]]
#             query.message.reply_text(text=f"Namoz vaqtlari {t_max} {t_max1} {t_mix} {t_mix1} {t_min} {t_min1} {t_mii} {t_mia1} {t_mis} {t_mis1} {t_mil} {t_mil1}",
#                                      reply_markup=InlineKeyboardMarkup(button))
#     if query.data == "back":
#         query.message.reply_text(text="Viloyatlar",reply_markup=InlineKeyboardMarkup(menu4()))
#
#
# def main():
#     updater = Updater(token=tokenn)
#     dispatcher = updater.dispatcher
#     dispatcher.add_handler(CommandHandler("start",start_hold))
#     dispatcher.add_handler(CallbackQueryHandler(menu))
#     updater.start_polling()
#     updater.idle()
# if __name__ == "__main__":
#     main()
# Tugash


