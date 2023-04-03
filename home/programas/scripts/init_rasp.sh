#/bin/bash
home=/home/pi

#actualizar pip
sudo apt-get install python3-pip -y

# #actualizar pyTelegramBotAPI
# pip install pyTelegramBotAPI

# #iniciar bot de python
# programas=$home/programas
# cd $programas
# echo "iniciando bot de telegram ip.py"
# python3 bots_telegram/bot_ip/ip.py & > bot_ip.txt


#iniciar todos los contenedores
cd $home/docker/pihole
echo "iniciando pihole"
docker-compose up -d

cd $home/docker/nginx
echo "iniciando pagina web"
docker-compose up -d

cd $home/docker/portainer
echo "iniciando portainer"
docker-compose up -d
# /home/pi/programas/scripts/init_rasp.sh