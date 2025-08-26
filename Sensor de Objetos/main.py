from machine import Pin, time_pulse_us
import time

# --- Configuração dos Pinos ---
PINO_TRIG = 25
PINO_ECHO = 27
PINO_LED_VERMELHO = 35
PINO_LED_VERDE = 26  

# Criação dos objetos
trig = Pin(PINO_TRIG, Pin.OUT)
echo = Pin(PINO_ECHO, Pin.IN)
led_vermelho = Pin(PINO_LED_VERMELHO, Pin.OUT)
led_verde = Pin(PINO_LED_VERDE, Pin.OUT)

# --- Função para medir distância ---
def obter_distancia():
    trig.value(0)
    time.sleep_us(2)

    trig.value(1)
    time.sleep_us(10)
    trig.value(0)

    duracao = time_pulse_us(echo, 1, 30000)  # timeout de 30ms
    distancia = (duracao / 2) * 0.0343
    return distancia

# --- Variável para contar os objetos ---
contador = 0

# --- Loop Principal ---
while True:
    dist = obter_distancia()
    print("Distância:", dist, "cm")

    if dist <= 5:  
        # Pisca o LED vermelho
        led_vermelho.value(1)
        time.sleep(0.2)
        led_vermelho.value(0)
        time.sleep(0.2)

        contador += 1
        print("Objeto detectado! Contagem:", contador)

        # Verifica se atingiu 10 objetos
        if contador >= 10:
            print("10 objetos detectados! Acendendo LED verde...")
            led_verde.value(1)
            time.sleep(10)  # LED verde aceso por 10s
            led_verde.value(0)
            contador = 0  # Reinicia a contagem
    else:
        # Não detectou objeto
        led_vermelho.value(0)

    time.sleep(0.3)  # pequeno delay para estabilizar
