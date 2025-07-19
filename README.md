# IoT Temperature Monitoring System  for a Smart Home project
**3rd Year University IoT Project**  

## Description  
A Raspberry Pi-based system that:  
- Monitors temperature/humidity using DHT11 sensor  
- Controls an LED based on temperature threshold  
- Publishes data to PubNub cloud service  
- Runs continuously with 5-second intervals
- Records Temperature

## Hardware Requirements  
- Raspberry Pi (any model)  
- DHT11 Temperature/Humidity Sensor  
- LED + 220Ω Resistor  
- Breadboard and jumper wires  

**Connections:**  
| Pi GPIO | Component | Pin |  
|---------|-----------|-----|  
| GPIO 4  | DHT11 Out | 7   |  
| GPIO 21 | LED +     | 40  |  
| GND     | LED -     | 39  |  

## Software Setup  
1. Install dependencies:  
```bash
pip install Adafruit_DHT gpiozero pubnub python-dotenv
```

2. Create `.env` file:  
```ini
PUBNUB_PUBLISH=your_pub_key
PUBNUB_SUBSCRIBE=your_sub_key
```

## Running the System  
```bash
python sensor_monitor.py
```

**Sample Output:**  
```
Temp=23.5°C Humidity=45.0%
Published to PubNub
```

## Data Format  
```json
{
  "temperature": 23.5,
  "humidity": 45.0,
  "timestamp": "2023-11-15T14:30:00Z",
  "heater_status": "ON"
}
```

## Configuration  
Modify in `sensor_monitor.py`:  
```python
TARGET_TEMP = 25.0  # Temperature threshold
PUBLISH_INTERVAL = 5  # Seconds
```

## Troubleshooting  
- **Sensor not reading**: Check GPIO 4 connection  
- **LED not working**: Verify GPIO 21 circuit  
- **PubNub errors**: Confirm API keys in `.env`  

## License  
MIT License - Free for academic use  

**Developed by:** [Sean McAvoy]  
**Course:** IoT Systems - [DkIT]  
**Year:** 2023  
