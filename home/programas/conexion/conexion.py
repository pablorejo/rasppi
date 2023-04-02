import ping3
import time
import leds
import argparse
#####     DEFAULT     #####
PIN_VERDE = 40
PIN_ROJO = 37
PIN_BUTTON = 38
PIN_BUTTON_LED = 36
IP = "192.168.0.1"
TIME = 1


#####     FUNTIONS     #####
def chek_ip():
    response_time = ping3.ping(ip,timeout=1.0)
    if response_time is not None:
        
        print(f'{ip} is reachable')
        leds.encender(True)
    else:
        print(f'{ip} is unreachable')
        leds.encender(False)



####    PROGRAM    #####
parser = argparse.ArgumentParser()

parser.add_argument("-l","--loop", help="The program run in loop (default)", action="store_true")
parser.add_argument("-n","--normal", help="The program run only one time", action="store_true")
parser.add_argument("-c","--count", help="The program run c times")
parser.add_argument("-i","--ip", help="IP that you want to check")
parser.add_argument("-g", "--green", help="Green ping (default 40)")
parser.add_argument("-r", "--red", help="Red ping (Default 37)")
parser.add_argument("--blue" ,"--booton-led", help="Blue boton ping (Default 36)")
parser.add_argument("-b", "--booton", help="Ping of booton (Default 38)")
parser.add_argument("-t", "--time", help="Time between one packet and other (default 1)")
#parser.add_argument("-f", "--file", help="To read the file config")

args = parser.parse_args()

#### Iniciamos las variables #####

#time
if not args.time:
    timee = TIME
else:
    timee = float(args.time)

#green pin
if not args.green:
    leds.PIN_VERDE = PIN_VERDE
else:
    leds.PIN_VERDE = int(args.green)

#red pin
if not args.red:
    leds.PIN_ROJO = PIN_ROJO
else:
    leds.PIN_ROJO = int(args.red)

leds.ESTADO_LED = False

#ip target
if not args.ip:
    ip = IP
else:
    ip = args.ip

# ping of led booton, blue led
if not args.blue:
    leds.PIN_BUTTON_LED = PIN_BUTTON_LED
else:
    leds.PIN_BUTTON_LED = args.blue

#ping boton
if not args.blue:
    leds.PIN_BUTTON_LED = PIN_BUTTON_LED
else:
    leds.PIN_BUTTON_LED = args.blue

try:
    print("Green ping: " + str(leds.PIN_VERDE) + "\nRed ping: " + str(leds.PIN_ROJO) + "\nIP: " + ip)
    leds.init()

    if args.normal:
        chek_ip()
        print("Normal mode")


    elif args.count:
        print("Count mode")
        while args.count >= 0:
            chek_ip()
            time.sleep(timee)
            args.normal -=1
            
    else:
        print("Loop mode")
        
        # activado = False
        # presionado = False
        # while True:
        #     while leds.button(activado,presionado):
        #         chek_ip()
        #         time.sleep(timee)
            
        while True:
            chek_ip()
            time.sleep(timee)
            
    leds.end()


except KeyboardInterrupt:
    leds.end()
    print("End program")

# except:
#     leds.end()
#     print("Interrupt")