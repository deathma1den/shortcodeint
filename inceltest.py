import datetime
import random
import telebot

# Создаем бота
bot = telebot.TeleBot("6528001118:AAEHD2vTHQAwvV39AeLI_RDuloSC-Ch9wq8")

# Хранилище статистики
stats = {}

# Обработчик команды /indel
@bot.message_handler(commands=["incel"])
def incel(message):
    # Получаем список участников чата
    chat_id = message.chat.id
    user_id = message.from_user.id

    try:
        chat_member = bot.get_chat_member(chat_id, user_id)
        # Check if the user is a chat member
        if chat_member.status in ("member", "administrator", "creator"):
            victim = random.choice(users)

            # Отправляем ему сообщение
            bot.send_message(victim.user.id, "Ты инцел!")

    # Обновляем статистику
            if victim.user.id not in stats.keys():
                stats[victim.user.id] = 1
            else:
                stats[victim.user.id] += 1
        else:
            bot.send_message(chat_id, "You are not a member of this chat.")
    except Exception as e:
        bot.send_message(chat_id, f"An error occurred: {str(e)}")


# Обработчик команды /stats
@bot.message_handler(commands=["stats"])
def stats(message):
    # Получаем пользователя
    user = message.from_user

    # Если ключа `user.id` нет в статистике, возвращаем 0
    if user.id not in stats.keys():
        bot.send_message(message.chat.id, "У тебя нет статистики")
        return

    # Отправляем сообщение с статистикой
    bot.send_message(message.chat.id, f"Ты был инцелом {stats[user.id]} раз")
# Запускаем бота
bot.polling()