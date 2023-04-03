- [Configurar](#configurar)
- [rasppi](#rasppi)
- [home](#home)
  - [docker](#docker)
    - [portainer](#portainer)
    - [pihole](#pihole)
    - [nginx](#nginx)
- [Dependencias](#dependencias)
- [scripts](#scripts)
  - [sftp.sh](#sftpsh)
    - [Opciones de ejecución](#opciones-de-ejecución)
  - [ssh.sh](#sshsh)
    - [Opciones de ejecución](#opciones-de-ejecución-1)
  - [variables.sh](#variablessh)
# Configurar 
1. Para configurar los script primero que nada configurar el script de [variables.sh](#variablessh)
2. Dar permisos de ejecución a los scripts
```bash
    sudo chmod +x *
```

3. A continuación crearemos los alias
```bash
alias sshpi="cd ~/Documentos/Documentos_pablo/rasppi/scripts/ && ./ssh.sh"
```
```bash
alias sftppi="cd ~/Documentos/Documentos_pablo/rasppi/scripts/ && ./sftp.sh"
```
4. Configurar el puerto del ssh para que estea donde quieras
Cambias el puerto en este fichero
```bash
nano /etc/ssh/sshd_config
```

Reinicias el servicion ssh.
```bash
service ssh restart
```

# rasppi
Vamos a crear un fichero de configuracion para nuestra raspberry pi

En este proyecto tenemos dos carpetas importantes:
- [home](#home): Donde estaran los ficheros que se guarden en la raspberrypi
- [sripts](#scripts): Donde se guardara los scripts para configurar y acceder a la raspberrypi



# home
En este directorio tendremos 2 carpetas [docker](#docker) y [programas](#programas).

## docker
Aquí definiremos los contenedores que vamos a usar que son los siguientes:

- [rasppi](#rasppi).
- [portainer](#portainer).
- [pihole](#pihole).
- [nginx](#nginx).

### portainer
Portainer es un gestor de contenedores basado en docker que usaremos para configurar los contenedores mediante la web

Su estructura es la [siguiente](home/docker/portainer/)
```yml
version: "3"
services:
  portainer:
    image: portainer/portainer-ce:latest
    ports:
      - 9443:9443
    volumes:
      - data:/data
      - /var/run/docker.sock:/var/run/docker.sock
    restart: always
volumes:
  data:
```

Tendremos la version 3
estamos usando la imagen portainer/portainer-ce:latest es decir la ultima que exista
Y la estaremos usando en el `puerto 9443`.

### pihole
Pihole es un servidor dns privado que usaremos para bloquear anuncios entre otros dominios potencialemente peligrosos.
Su estructura es la [siguiente](home/docker/portainer/).
Definiremos la contraseña que está alli puesta.
usaremos el puerto `"9000:80/tcp"` para acceder a la página web.
Y reservaremos el `puerto 53` para usarlo para las peticiones DNS


### nginx
Aquí tendremos configurado

# Dependencias 
necesitamos tener instalado `sshpass`
> sudo apt install sshpass

Este nos servirá para no tener que poner la constraseña siempre que queramos acceder a la raspberry

# scripts
Aquí vamos a definir los scripts para acceder y mantener la raspberry pi
- [sftp.sh](#sftpsh)
- [ssh.sh](#sshsh)
- [variables.sh](#variablessh)

## sftp.sh
Aqui tendremos configurado un script para acceder de manera rapida a la raspberry y enviar los datos.

### Opciones de ejecución
Para ejecutar el script tiene dos maneras:
> ./sftp.sh IP
> ./sftp.sh
>
Si no le pones la IP se intentara conectar a la ip por defecto configurada en [variables.sh]

## ssh.sh
Con este script nos conectaremos de manera rapida a la raspberry por medio de ssh
### Opciones de ejecución
Para ejecutar el script tiene dos maneras:
> ./ssh.sh IP
> ./ssh.sh
>
Si no le pones la IP se intentara conectar a la ip por defecto configurada en [variables.sh]

## variables.sh
Aquí definiremos las variables glovales que vamos a usar en nuestros scripts.

Tenemos definidas las siguientes:
- `path`: Donde esta situado nuestro fichero [home](#home)
- `puerto`: Puerto donde se está eschuchando el ssh la raspberry
- `ip`: Ip de la raspberry
- `pass`: Contraseña que está configurada en la raspbarry
- `ddns`: DDNS que tenemos puesto para acceder a nuestra raspberry