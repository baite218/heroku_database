import os
import telebot
import logging
import psycopg2
from config import *
from flask import Flask, request

bot = telebot.TeleBot(BOT_TOKEN)
server = Flask(__name__)
"""что это?"""
logger = telebot.logger
logger.setLevel(logging.DEBUG)

db_connection = psycopg2.connect(DB_URI, sslmode="require")
db_object = db_connection.cursor()





# def update_messages_count(user_id):
#     db_object.execute(f"UPDATE users SET messages = messages + 1 WHERE id = {user_id}")
#     db_connection.commit()


# @bot.message_handler(commands=["start"])
# def start(message):
#     user_id = message.from_user.id
#     username = message.from_user.username
#     bot.reply_to(message, f"Hello, {username}!")

#     db_object.execute(f"SELECT id FROM users WHERE id = {user_id}")
#     result = db_object.fetchone()

#     if not result:
#         db_object.execute("INSERT INTO users(id, username, messages) VALUES (%s, %s, %s)", (user_id, username, 0))
#         db_connection.commit()

#     update_messages_count(user_id)


# @bot.message_handler(commands=["stats"])
# def get_stats(message):
#     db_object.execute("SELECT * FROM users ORDER BY messages DESC LIMIT 10")
#     result = db_object.fetchall()

#     if not result:
#         bot.reply_to(message, "No data...")
#     else:
#         reply_message = "- Top flooders:\n"
#         for i, item in enumerate(result):
#             reply_message += f"[{i + 1}] {item[1].strip()} ({item[0]}) : {item[2]} messages.\n"
#         bot.reply_to(message, reply_message)

#     update_messages_count(message.from_user.id)


# @bot.message_handler(func=lambda message: True, content_types=["text"])
# def message_from_user(message):
#     user_id = message.from_user.id
#     update_messages_count(user_id)







# @server.route(f"/{BOT_TOKEN}", methods=["POST"])
# def redirect_message():
#     json_string = request.get_data().decode("utf-8")
#     update = telebot.types.Update.de_json(json_string)
#     bot.process_new_updates([update])
#     return "!", 200

# if __name__ == "__main__":
#     bot.remove_webhook()
#     bot.set_webhook(url=APP_URL)
#     server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))








import random
import telebot
from telebot import types
d = [
    "https://youtu.be/Qvedyro_8mM",
    "https://youtu.be/5GyUm9uc1G0",
    "https://youtu.be/4ZNrQxIJeS4",
    "https://youtu.be/5ML9zpdHYO0",
    "https://youtu.be/r2tWE19ekT0",
    "https://youtu.be/eM0kMAnmZmk",
    "https://youtu.be/Hzxu0QghHck",
    "https://youtu.be/hVskI8q1kyk",
    "https://youtu.be/w33BCNRNoEo",
    "https://youtu.be/K4QxiHy2DQg",
    "https://youtu.be/mADTIsFnuN8",
    "https://youtu.be/bQyfCsr0OVk",
    "https://youtu.be/mofTWo3-tcs",
    "https://youtu.be/M_sF_eSLIzc",
    "https://youtu.be/05LZA9Cwwwo",
    "https://youtu.be/4VhIXe0FGeY",
    "https://youtu.be/cPL3k9YXLlo",
    "https://youtu.be/OHFPY_zQZI4",
    "https://youtu.be/lboo2xhGj_E",
    "https://youtu.be/ms1ZfVt7Wxw",
    "https://youtu.be/0wSK1FeGUhA",
    "https://youtu.be/wyq2zVFkWCw",
    "https://youtu.be/gC5tJVZY1iQ",
    "https://youtu.be/w33rGpXK8o0",
    "https://youtu.be/l83qp0VnAtI",
    "https://youtu.be/0370kmm1WQU",
    "https://youtu.be/v2r8HBo2cRc",
    "https://youtu.be/5KIRKLhj83o",
    "https://youtu.be/2pE6ssSYuL4",
    "https://youtu.be/7UtFVFZO9WY",
    "https://youtu.be/wD0NcRnCB7g",
    "https://youtu.be/X0ijsSgEQGg",
    "https://youtu.be/9qjSs76IX1A",
    "https://youtu.be/oetA1GHzEY4",
    "https://youtu.be/urJHykvmm4k",
    "https://youtu.be/mh-dzhgSq7Q",
    "https://youtu.be/3CADvmdGnYU",
    "https://youtu.be/u-mKydVy7mY",
    "https://youtu.be/MSFW8MwGIMg",
    "https://youtu.be/GigOIMeKohg",
    "https://youtu.be/4pK6gwniyto",
    "https://youtu.be/3dW5BvmITug",
    "https://youtu.be/jGMIjl8GE1w",
    "https://youtu.be/AmIMNSckaCs",
    "https://youtu.be/8vruN9dcPWs",
    "https://youtu.be/PoOCdesuwIo",
    "https://youtu.be/HuLFkTdgxBM",
    "https://youtu.be/4RAWUvpdEYM",
    "https://youtu.be/gZcAn8JsmM8",
    "https://youtu.be/bDhzaEjp2_k",
    "https://youtu.be/tcSmqadH4_M",
    "https://youtu.be/nbuFuDt2ubo",
    "https://youtu.be/JoAqs3MR184",
    "https://youtu.be/HVsdxcP3GTw",
    "https://youtu.be/zXcu6FKpQNM",
    "https://youtu.be/Yb8FgcqFnYg",
    "https://youtu.be/K1bofvVYbgc",
    "https://youtu.be/fTVva3KLAUM",
    "https://youtu.be/NiqnqqTsVsE",
    "https://youtu.be/92brtGCQJkg",
    "https://youtu.be/ENWUWm6MJ4I",
    "https://youtu.be/8_y41n__sC8",
    "https://youtu.be/eLamN1aj-sw",
    "https://youtu.be/l89MJPYqGaw",
    "https://youtu.be/qdy6fZbPfEE",
    "https://youtu.be/aR0MpVJxR54",
    "https://youtu.be/4XRaILwC-cM",
    "https://youtu.be/JVXP_2KL0BA",
    "https://youtu.be/hieCKSLArko",
    "https://youtu.be/0wjtIKQ0oiQ",
    "https://youtu.be/Adr0caiCzCI",
    "https://youtu.be/0uYCBag4ses",
    "https://youtu.be/-k17PimsZHI",
    "https://youtu.be/VC9dlwLLMjQ",
    "https://youtu.be/fx1W9pIIt8U",
    "https://youtu.be/XN0TNzsMQxQ",
    "https://youtu.be/6Ccxx2J2W3s",
    "https://youtu.be/HjxLFacHrZw",
    "https://youtu.be/YGVKmQA-Q5s",
    "https://youtu.be/a9m8BSGzBfs",
    "https://youtu.be/QJ_27TNNHFo",
    "https://youtu.be/6Tq38Wk_53w",
    "https://youtu.be/IpyvgCMmurA",
    "https://youtu.be/gie2cyo1VHM",
    "https://youtu.be/0M1sJLEB1rQ",
    "https://youtu.be/jQpypipWscs",
    "https://youtu.be/lIem1yVKl6I",
    "https://youtu.be/SeQ17rZkfbs",
    "https://youtu.be/MiUkGEkdQBA",
    "https://youtu.be/ESiSVbSzB4w",
    "https://youtu.be/p7fjjf8Y6D0",
    "https://youtu.be/Zd0yXmB_10Q",
    "https://youtu.be/6ilR4DveVXE",
    "https://youtu.be/f5P_YeYIvYE",
    "https://youtu.be/fqcQnl1_PiA",
    "https://youtu.be/8OuB-xtOkKk",
    "https://youtu.be/EiVHspK9za8",
    "https://youtu.be/jcjfwd9C4oo",
    "https://youtu.be/B3FhVOUpKEg",
    "https://youtu.be/HpL6ymFEuu4",
    "https://youtu.be/IXHx3y59Foc",
    "https://youtu.be/IoewGMm-aS8",
    "https://youtu.be/YCcgBJdP7Mc",
    "https://youtu.be/PtQiiknWUcI",
    "https://youtu.be/ZT2C1adrZIM",
    "https://youtu.be/EEtZOiyk5l4",
    "https://youtu.be/lgHd4bXwsaw",
    "https://youtu.be/m2kOu6J2Zhc",
    "https://youtu.be/5sYMNfrlpxY",
    "https://youtu.be/ldywUFXvr5w",
    "https://youtu.be/iXljedQWyHA",
    "https://youtu.be/ffWR8sm6XT0",
    "https://youtu.be/T6_KCiek2lY",
    "https://youtu.be/Q5BpjYSedqc",
    "https://youtu.be/YQCuXkJSaRc",
    "https://youtu.be/YmIqm_KsH3A",
    "https://youtu.be/REywO7fKs9o",
    "https://youtu.be/U0zx-xsTRdA",
    "https://youtu.be/JXD3ADSOWt4",
    "https://youtu.be/Ps0Sr5teQTM",
    "https://youtu.be/gpiqdqgITXY",
    "https://youtu.be/4w0an9uJ6ig",
    "https://youtu.be/XM-SR1uc3b8",
    "https://youtu.be/03cw9QKx7ak",
    "https://youtu.be/iskVS7obEXg",
    "https://youtu.be/KCxEPmb-C_U",
    "https://youtu.be/n_xvU-AxIb4",
    "https://youtu.be/uEaouwm3ebA",
    "https://youtu.be/__phmXk1A0c",
    "https://youtu.be/2t-Dx6myC0E",
    "https://youtu.be/ZzAx8ZuflWE",
    "https://youtu.be/7qHlYlDzsxo",
    "https://youtu.be/MWTg1yCWqtQ",
    "https://youtu.be/sZ5SI6n1Ljs",
    "https://youtu.be/39qGEdY1aos",
    "https://youtu.be/Z_ZfH8pC3_A",
    "https://youtu.be/CWMUdtMK7kU",
    "https://youtu.be/aG4ozL417VQ",
    "https://youtu.be/zyd1U7jUmD8",
    "https://youtu.be/dCbu9m7DlEY",
    "https://youtu.be/ODLbiQsweCE",
    "https://youtu.be/WCL0DdF9rzE",
    "https://youtu.be/gfKUUAQcbuM",
    "https://youtu.be/ysEbF0xkWWQ",
    "https://youtu.be/0SqNghgDAsQ",
    "https://youtu.be/DMiVKRRJyhg",
    "https://youtu.be/fIu2dQPBcBc",
    "https://youtu.be/fT9ZHpxq4A0",
    "https://youtu.be/DrZ7sr-yKOI",
    "https://youtu.be/yNj_TMICRh8",
    "https://youtu.be/u_DLt2EnOrA",
    "https://youtu.be/-PkwZ-WZbz4",
    "https://youtu.be/rbN1Z44BYfA",
    "https://youtu.be/mXf_OyPHosg",
    "https://youtu.be/d71yH9SHuyU",
    "https://youtu.be/-UURgg_WpYw",
    "https://youtu.be/wAntCuxS-Ys",
    "https://youtu.be/OSzVtFUYA4A",
    "https://youtu.be/rQ-f2wgZ6xo",
    "https://youtu.be/lnY4jhgypTU",
    "https://youtu.be/IvogNMvqUcA",
    "https://youtu.be/fIu2dQPBcBc",
    "https://youtu.be/p4d9LP5ZWqc",
    "https://youtu.be/O6TTDYYn51k",
    "https://youtu.be/-oCFdNjwnrY",
    "https://youtu.be/ij6YGGy7e-o",
    "https://youtu.be/sqAYwKlH4hI",
    "https://youtu.be/9-8pyoo1T50",
    "https://youtu.be/2oZVyEAUeOg",
    "https://youtu.be/b52cfb6lweU",
    "https://youtu.be/rs9VcWdAbnE",
    "https://youtu.be/7UmbcHPVOHo",
    "https://youtu.be/6BqpU4V0Ypk",
    "https://youtu.be/GnJ51fVaFLE",
    "https://youtu.be/Pz-GMJlKHNo",
    "https://youtu.be/uYpBIrhW114",
    "https://youtu.be/YQY-kvB8SwQ",
    "https://youtu.be/l9d1HXE7SH0",
    "https://youtu.be/MeExbtpIPaw",
    "https://youtu.be/WpojDncIWOw",
    "https://youtu.be/du2K88Cynq8",
    "https://youtu.be/2W8vvEBfKx4",
    "https://youtu.be/_AvFWDik4C4",
    "https://youtu.be/JjmH6vdTpdY",
    "https://youtu.be/RsLz-HfFO4M",
    "https://youtu.be/vD0X5Zm9Gjo",
    "https://youtu.be/ywx6m7_BZng",
    "https://youtu.be/Xnjg2B3_AJE",
    "https://youtu.be/rI9bCkIu0uY",
    "https://youtu.be/SA5f_jBVq5A",
    "https://youtu.be/94NgNNs1O3Q",
    "https://youtu.be/RDbzApTFy0E",
    "https://youtu.be/EdGZ8PqFqcQ",
    "https://youtu.be/IJA7Uyh9r8E",
    "https://youtu.be/6YMD2RediSs",
    "https://youtu.be/3BJfS9p7rc8",
    "https://youtu.be/T8dnN1kpvEY",
    "https://youtu.be/cHmKb5RcsVI",
    "https://youtu.be/76owU7BTLd0",
    "https://youtu.be/kPzeTh_Evtg",
    "https://youtu.be/UaCAWTnB35E",
    "https://youtu.be/Qq6fptZuESM",
    "https://youtu.be/4ZzF08kW7-U",
    "https://youtu.be/uuX3XbRlnxQ",
    "https://youtu.be/_wNsZEqpKUA",
    "https://youtu.be/pVCoZG0-hfE",
    "https://youtu.be/mSHAbpnMtgk",
    "https://youtu.be/RQaaSLaEyT4",
    "https://youtu.be/HlBYdiXdUa8",
    "https://youtu.be/qPzMonT_n70",
    "https://youtu.be/yfqpqiTMUEg",
    "https://youtu.be/bYsWewkVehw",
    "https://youtu.be/Dek5HtNdIHY",
    "https://youtu.be/TDZbXvvfp0w",
    "https://youtu.be/i9CBKGLVCME",
    "https://youtu.be/G2_5rPbUDNA",
    "https://youtu.be/bSMZgXzC9AA",
    "https://youtu.be/167se17RNHw",
    "https://youtu.be/8NctXDM1kRA",
    "https://youtu.be/z1t3NOq_VxU",
    "https://youtu.be/3r0OGNy4NGg",
    "https://youtu.be/WYzFhuON1ss",
    "https://youtu.be/UYEaEko8gas",
    "https://youtu.be/cVl62Bp09Fo",
    "https://youtu.be/WooElIJrZkA",
    "https://youtu.be/K88Soi6Atz4",
    "https://youtu.be/2tQVj_nOlbo",
    "https://youtu.be/pkbMUvQwjTE",
    "https://youtu.be/GbVN8cREj5g",
    "https://youtu.be/xt-klD7gxqc",
    "https://youtu.be/3oIXoLpG6pk",
    "https://youtu.be/dQ72f1smDEU",
    "https://youtu.be/Tnxyls_aayg",
    "https://youtu.be/dLgWmsFiOAA",
    "https://youtu.be/qBBeTMFh9QY",
    "https://youtu.be/-6yUiSKFiD0",
    "https://youtu.be/51iNsTs9jMM",
    "https://youtu.be/pO6wDBss8PI",
    "https://youtu.be/y6vUETgKMQQ",
    "https://youtu.be/2ZMEZB1RYio",
    "https://youtu.be/uhwPxaUmNZU",
    "https://youtu.be/YcrZpLNd0qU",
    "https://youtu.be/C45QLU0v81E",
    "https://youtu.be/zWeXEHfspVE",
    "https://youtu.be/nAE5bLo02rA",
    "https://youtu.be/ToyiLndDMvQ",
    "https://youtu.be/Z3-kBDynUG4",
    "https://youtu.be/3GpbzF4dZ3k",
    "https://youtu.be/BXgWrFgmWZM",
    "https://youtu.be/6yDwWw4TH30",
    "https://youtu.be/JMHXN8bngFk",
    "https://youtu.be/4U-HMk9l-S0",
    "https://youtu.be/wYiZ-U6w2GM",
    "https://youtu.be/wZ0m6b6U2xs",
    "https://youtu.be/tw3-ukOLDrM",
    "https://youtu.be/b7mIkrIXYww",
    "https://youtu.be/e3aj9VmMxC8",
    "https://youtu.be/9ItU1VnO5Fw",
    "https://youtu.be/v4YVcDpboVQ",
    "https://youtu.be/HkcJ4fitzh4",
    "https://youtu.be/L7VYh02jCZ4",
    "https://youtu.be/LBDQNLr5mJo",
    "https://youtu.be/FqYGxmy1_Kg",
    "https://youtu.be/ESAZYlp563I",
    "https://youtu.be/VBvHyx3cVZw",
    "https://youtu.be/hs7KMdNszWY",
    "https://youtu.be/E5Dy3W_ZK2U",
    "https://youtu.be/N5gLfP4uPsw",
    "https://youtu.be/f_hNjPmQq-M",
    "https://youtu.be/qllwSyyt-Pg",
    "https://youtu.be/69x9GToyJUs",
    "https://youtu.be/JjzGFQfYLto",
    "https://youtu.be/B9xJhLMm_8Y",
    "https://youtu.be/f1xxxi12ueo",
    "https://youtu.be/hejXrtl4XuM",
    "https://youtu.be/oDb6Jfxprpk",
    "https://youtu.be/nohkDYpXcUU",
    "https://youtu.be/Y8ROQeWryqI",
    "https://youtu.be/DgUajO7Tf3c",
    "https://youtu.be/xhnZ189VnUU",
    "https://youtu.be/6B_uDsIemXo",
    "https://youtu.be/_juO-4GYYoY",
    "https://youtu.be/sC8fDWHuIvM",
    "https://youtu.be/-iqvcKmePP4",
    "https://youtu.be/iGzg7X4TN_Y",
    "https://youtu.be/FDRZHZsjFRI",
    "https://youtu.be/IFxMAsaimMk",
    "https://youtu.be/EfwAQuw2tkw",
    "https://youtu.be/7Ey_cd_8Qsk",
    "https://youtu.be/ta93_HOnu-8",
    "https://youtu.be/UgCmw7XnEuA",
    "https://youtu.be/OY0xu6_foU0",
    "https://youtu.be/-2QhjFN_P54",
    "https://youtu.be/qBDbO_bAdFM",
    "https://youtu.be/pBSGl2uq3_4",
    "https://youtu.be/tqQnUio-j4g",
    "https://youtu.be/VFBXx7O9BxU",
    "https://youtu.be/YdmKGnmr_Y0",
    "https://youtu.be/HenJQ-I28QA",
    "https://youtu.be/8SWvEFh4B9U",
    "https://youtu.be/T1Y2zzew528",
    "https://youtu.be/f4mednegDUQ",
    "https://youtu.be/shsU03EaA8A",
    "https://youtu.be/UNY9HLmlsoM",
    "https://youtu.be/AyPeDZ-I8pY",
    "https://youtu.be/Q3YFRDdRRRc",
    "https://youtu.be/Jrv8SgoVWTM",
    "https://youtu.be/nrcakd1sfrs",
    "https://youtu.be/zWFSp8I7xzU",
    "https://youtu.be/FKnhT-9IM_M",
    "https://youtu.be/I1ff3qFmVy4",
    "https://youtu.be/PXIX_du2xz8",
    "https://youtu.be/FgB1h89IC4M",
    "https://youtu.be/zzAkmC3lPqs",
    "https://youtu.be/hIm37FjecTo",
    "https://youtu.be/zXtXrJb3vqI",
    "https://youtu.be/uWN9yTdBfPA",
    "https://youtu.be/3YCbLCMqtvM",
    "https://youtu.be/eJGG6XZGuic",
    "https://youtu.be/f4bvcm3Ob78",
    "https://youtu.be/VV_3xCLDxhc",
    "https://youtu.be/yBYYO4KDupI",
    "https://youtu.be/aX503YuinDk",
    "https://youtu.be/8jJgNdi-u5k",
    "https://youtu.be/D-113xcG0xg",
    "https://youtu.be/SXjQwijlVGw",
    "https://youtu.be/XsKxyQvnC6A",
    "https://youtu.be/5z5TimPaqkg",
    "https://youtu.be/8YSEGx1J1dI",
    "https://youtu.be/pLp4COtl3Zw",
    "https://youtu.be/Fl2S5dqK2vQ",
    "https://youtu.be/1s-RPWem_Uk",
    "https://youtu.be/qx4FLF5QcAw",
    "https://youtu.be/yYbcI0H146s",
    "https://youtu.be/zOCgvzfcWfg",
    "https://youtu.be/Pwhh8tSwzDI",
    "https://youtu.be/gbJPc6fbYBQ",
    "https://youtu.be/lGMK0uOZvBw",
    "https://youtu.be/Ur7kRASt6jk",
    "https://youtu.be/jvEWaW_m_mY",
    "https://youtu.be/BLSrXy9Oz68",
    "https://youtu.be/UUH6ywJuQOs",
    "https://youtu.be/QHLROLKDaXg",
    "https://youtu.be/IJtXIZkzzPg",
    "https://youtu.be/8iTjWgBc7Bw",
    "https://youtu.be/CzbPd8T5ndw",
    "https://youtu.be/wJ1RWozpcNk",
    "https://youtu.be/416ZqXR-41w",
    "https://youtu.be/9IIo5EstpY0",
]




@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, str(random.sample(d, 1)))
    bot.send_message(message.chat.id, "================================")
    bot.send_message(message.chat.id, str(random.sample(d, 1)))

bot.polling(none_stop=True)