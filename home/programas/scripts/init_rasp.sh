#/bin/bash
home=/home/pi

#actualizar pip
sudo apt-get install python3-pip -y

#actualizar pyTelegramBotAPI
pip install pyTelegramBotAPI

#iniciar bot de python
programas=$home/programas
cd $programas
echo "iniciando bot de telegram ip.py"
python3 bots_telegram/bot_ip/ip.py & > bot_ip.txt


#iniciar pihole
cd $home/docker/pihole
echo "iniciando pihole"
docker compose up -d