#!/usr/bin/env python
import cayenne.client
import time

# Cayenne authentication info. This should be obtained from the Cayenne Dashboard.
MQTT_USERNAME  = 908f5540-b1e1-11e7-a9b2-a5d7f5484bce
MQTT_PASSWORD  = 0d76f201738b68b941acfbcb3639ed6f195bf679
MQTT_CLIENT_ID = b7e2f880-b1e2-11e7-b177-579293954599


cayenne.mqtt.mydevices.com

client.begin(908f5540-b1e1-11e7-a9b2-a5d7f5484bce, 0d76f201738b68b941acfbcb3639ed6f195bf679, b7e2f880-b1e2-11e7-b177-579293954599)

i=0
timestamp = 0

while True:
client.loop()
    
if (time.time() > timestamp + 10):
client.celsiusWrite(1, i)
client.luxWrite(2, i*10)
client.hectoPascalWrite(3, i+800)
timestamp = time.time()
        i = i+1
