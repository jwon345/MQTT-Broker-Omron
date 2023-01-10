import paho.mqtt.client as mqtt 
import time

def on_connect(client, userdata, flags,rc):
    print("connected mqtt client")
    print(userdata)
    print(client)
    client.subscribe("testing")

def on_message(client, userdata, msg):
    print(msg.topic + str(msg.payload))



client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("52.63.111.219", 1883, 60)
for i in range(0,10):
    client.publish("testing", "testdata" + str(i))
    time.sleep(1) 
client.loop_forever()

