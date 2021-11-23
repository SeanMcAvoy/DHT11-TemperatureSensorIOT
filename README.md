# DHT11-TemperatureSensor

## Install the DHT python library - To be Able to use the library
sudo pip3 install Adafruit_DHT

### Wire Connections

| DHT11 Pin | Signal        | Pi Pin   |
| ----------|:-------------:| --------:|
| 1         | 5v            |   2      |      
| 2         | data/output   |7 (GPIO4) |
| 3         | n/a           |    n/a   |
| 4         | ground        |    6     |

## Pubnub Connection - On the file
`pip install 'pubnub>=5.4.0'`