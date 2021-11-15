# imports Adafruit_DHT libary
import Adafruit_DHT
import time
import datetime

# sensor type
DHT_SENSOR = Adafruit_DHT.DHT11
# GPIO pin DHT11 output is going too
GPIO_PIN = 4


# writing to a file to let the pi run for a few hours and get temp of my room to have realistic data for UDP project
def write_to_file(humidity, temperature):
    time_stamp = datetime.datetime.now()
    temp_readings_file = open("readings.txt", "a")
    temp_readings_file.write('\nTemp={0:0.1f}*C  Humidity={1:0.1f}% TimeStamp: '.format(temperature, humidity))
    temp_readings_file.write(time_stamp.strftime("%Y-%m-%d %H:%M:%S"))
    temp_readings_file.close()


# returns both humidity, temperature
def get_data_reading():
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, GPIO_PIN)
    if humidity is not None and temperature is not None:
        return humidity, temperature
    else:
        return 0, 0


def main():
    minute = 0  # not needed for project just for testing to .txt file
    while True:
        # humidity, temperature = get_data_reading()
        humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, GPIO_PIN)
        if humidity is not None and temperature is not None:
            print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
            if minute >= 20:  # Only for collecting data for UDP
                minute = 0
                write_to_file(humidity, temperature)
        else:
            print('Failed Reading - Trying Again')
        time.sleep(60)  # reading every minute
        minute += 1


if __name__ == "__main__":
    main()


# Help Ref:
# https://www.thegeekpub.com/236867/using-the-dht11-temperature-sensor-with-the-raspberry-pi/
