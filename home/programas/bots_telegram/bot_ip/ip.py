import telebot
import requests
import threading
import subprocess

PWD="aFUSyLghIZyjxTowPw3CS80GwcvUy5p4QyCx4QFDzGJ7enMhis"
MI_ID = 793773363
TOKEN = "5882883789:AAFtElRe8KWia20loGYq-2zYynPm2q4MJog"

bot = telebot.TeleBot(TOKEN)

def public_ip():
    try:
        public = requests.get('http://checkip.amazonaws.com').text.strip()
    except:
        public = 'unknown'

    return str(public)

def usuario_incorrecto(message):
    bot.send_message(MI_ID,"Intento entrar un usuario mal intencionado")
    bot.reply_to(message,"Usuario no autorizado")
    print("Usuario no autorizado")
    print(message.chat.id)




@bot.message_handler(commands=["help", "start"])
def enviar(message):
    if message.chat.id == MI_ID:
        ip = public_ip()
        bot.reply_to(message,ip)
        print(message.chat.id)

    else:
        usuario_incorrecto(message)

@bot.message_handler(commands=["actualizar"])
def actualizar(message):
    if message.chat.id == MI_ID:
        subprocess.call("echo " +PWD+ "| sudo -S apt-get update -y && sudo apt-get upgrade -y > log.txt", shell=True)

    else:
        usuario_incorrecto(message)



def iniciar_bot():
    bot.send_message(MI_ID,"Iniciando Raspberry")
    bot.infinity_polling()

if __name__ == '__main__':
    print("Iniciando Bot")
    hilo_bot = threading.Thread(name="hilo_bot",target=iniciar_bot)
    hilo_bot.start()


