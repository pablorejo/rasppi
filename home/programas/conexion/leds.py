import RPi.GPIO as GPIO
import time

PIN_VERDE = 40
PIN_ROJO = 37
PIN_BUTTON = 38
PIN_BUTTON_LED = 36

ESTADO_LED = False  #Variable que guardará el estado del led


def init():
    GPIO.setwarnings(False)
    GPIO.setmode (GPIO.BOARD)
    GPIO.setup (PIN_VERDE, GPIO.OUT) #led verde
    GPIO.setup (PIN_ROJO, GPIO.OUT) #led rojo
    GPIO.setup (PIN_BUTTON_LED, GPIO.OUT) #led boton
    GPIO.setup (PIN_BUTTON, GPIO.IN) #led boton

def encender(encender):
    if encender:
        GPIO.output(PIN_VERDE, True)  
        GPIO.output(PIN_ROJO, False)  
        #print("Verde encendido Rojo apagado")
    else:
        GPIO.output(PIN_VERDE, False)  
        GPIO.output(PIN_ROJO, True)  
        #print("Verde apagado Rojo encendido")

def end():
    GPIO.cleanup() 



def button(presionado,activado):
    
    boton = GPIO.input(PIN_BUTTON)
    if ((activado == False) and (boton == 1)):
        GPIO.cleanup() 
        init()
        presionado = not presionado
        print("Boton presionado")  
    activado = boton
    GPIO.output(PIN_BUTTON_LED, presionado)
    return presionado

   
    