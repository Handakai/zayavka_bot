
API_TOKEN = '1403287746:AAEXSPIkgf7AkyukI_6bTLHno6sF5ML__IY' # Сюда вписываете токен бота
admin_id =  259281983 # Сюда вписываете свой ID телеграмм (посмотреть можно в боте @my_id_bot)

first_message = 'Привет, чтобы с нами работать необходимо подать заявку 🤝' # Текст, который будет отправлен после /start

rules = '''© Наши правила:\n1. Запрещен спам, флуд, срач. (Предупреждение)
2. Запрещены пересылки с других каналов, ссылки на сторонние ресурсы, реклама. (Бан)
3. Запрещены материалы с содержанием (порно, насилие, убийства, призывы к экстремизму, реклама наркотиков). (Бан)
4. Запрещено оскорблять администрацию и модераторов. (Бан)
5. Запрещены конфликты в чате. (Предупреждение)
6. Запрещено попрошайничество в беседе. (Бан)
7. Получили 3 предупреждения? Бан.
 
Вы подтверждаете, что ознакомились и согласны с условиями и правилами нашего проекта?'''

rules_with_confirmation = rules + '\n\n' + '✅ Вы приняли наши правила' # Заменять текст по надобности


question_1 = 'Вопрос первый: *Откуда вы узнали о нас?*'
question_2 = 'Вопрос второй: \n🔹 Имеется ли у Вас опыт работы в данной сфере?\nЕсли есть возможность, приложите скриншоты (@imgurbot_bot)'
question_3 = 'Вопрос третий: \n🔸 Сколько готовы уделять времени?'
question_4 = 'Вопрос четвертый: \n🔹 Вы же понимаете, что лить мы будем на забугор(не Русский тикток)?'

summary = 'Откуда узнали: _{answers[0]}_\nОпыт: _{answers[1]}_\nСколько готовы уделять времени: _{answers[2]}_\nLast: _{answers[3]}_' # Не трогать



for_false = 'Ваша заявка отклонена' # Текст если заявка отклонена
for_true = 'Заявка отправлена 🚀' # Текст если заявка принята


text_for_admin = 'Новая заявка - ' # Заявка подставиться


message_for_user_if_accepted = 'Ваша заявка принята, добро пожаловать [в нашу команду](t.me/joinchat/AAAAAFX1dWgrGnsnMHcqyg)' # Сообщение о принятии заявки которое отправляется юзеру
# Чтобы сделать кнопочную ссылку на канал то напишите слово в скобках "[]" и потом слитно ссылку в других скобках "()"
# Например: Вступить в [канал](t.me/LINK38j19d9k2x0s)

################### keyboards ##########################
greet_kb = 'Полетели 🚀' # Первая кнопка после приветствия
rules_confirmation_kb = 'Согласен, продолжаем 👌' # Кнопка для подтверждения правил

applying = ['Отправить ✅', 'Удалить заявку ❌'] # Кнопки перед отправкой сообщения пользователем, от подтверждает отправить заявку или нет

admin_applying = ['Принять ✅', 'Отклонить ❌'] # Кнопки для администратора Принять/Отклонить заявку

# 
# Для переноса строки в сообщениях используйте символ "\n"
# 

# Reddington - t.me/RichmondSeller
