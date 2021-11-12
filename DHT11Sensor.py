#imports Adafruit_DHT libary
# import Adafruit_DHT
import time

# sensor type
# DHT_SENSOR = Adafruit_DHT.DHT11
# GPIO pin DHT11 output is going too
GPIO_PIN = 4

# writing to a file to let the pi run for a few hours and get temp of my room to have realistic data for UDP project
def write_to_file():
    return 0


def main():
    while True:
        # humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, GPIO_PIN)
        # if humidity is not None and temperature is not None:
        #     print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
        # else:
        #     print('Failed - Recheck wiring')
        time.sleep(3)


if __name__ == "__main__":
    # main()
    temp_readings_file = open("readings.txt","r")
    print(temp_readings_file.read())
    temp_readings_file.close()


# Help Ref:
# https://www.thegeekpub.com/236867/using-the-dht11-temperature-sensor-with-the-raspberry-pi/
