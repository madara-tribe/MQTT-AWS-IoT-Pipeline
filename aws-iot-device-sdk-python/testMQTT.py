import os
import os.path
import time
import json
import numpy as np

ROOTDIR='../keys'
THING_NAME = 'testMQTT'
TOPIC_NAME = 'device/22/data'

def create_msg():
    message = {"temperature" : int(np.random.randint(1, 10, 1)),
                "humidity": int(np.random.randint(1, 100, 1)),
                "barometer": int(np.random.randint(1, 1000, 1)),
                "wind": {
                    "velocity": int(np.random.randint(1, 30, 1)),
                    "bearing": int(np.random.randint(1, 300, 1))
               }}
    return message

class IotMqttClient:

    ROOT_CA_PATH = os.path.join(ROOTDIR, 'AmazonRootCA1.pem')
    CERTIFICAT_PATH = os.path.join(ROOTDIR, 'certificate.pem.crt')
    PRIVATE_KEY_PATH = os.path.join(ROOTDIR, 'private.pem.key')
    IOT_ENDPOINT = 'a3phz77nfdgsr1-ats.iot.ap-northeast-1.amazonaws.com'
    IOT_PORT = 8883
    __my_iot_mqtt_client = None
    __is_connected = False

    def __init__(self):
        from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

        # setup client
        self.__my_iot_mqtt_client = AWSIoTMQTTClient(THING_NAME)
        self.__my_iot_mqtt_client.configureEndpoint(self.IOT_ENDPOINT, self.IOT_PORT)
        self.__my_iot_mqtt_client.configureCredentials(self.ROOT_CA_PATH, self.PRIVATE_KEY_PATH, self.CERTIFICAT_PATH)

        # setup access infomation
        self.__my_iot_mqtt_client.configureAutoReconnectBackoffTime(1, 32, 20)
        self.__my_iot_mqtt_client.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
        self.__my_iot_mqtt_client.configureDrainingFrequency(2)  # Draining: 2 Hz
        self.__my_iot_mqtt_client.configureConnectDisconnectTimeout(10)  # 10 sec
        self.__my_iot_mqtt_client.configureMQTTOperationTimeout(5)  # 5 sec

        def on_offline(): self.__is_connected = False
        def on_online(): self.__is_connected = True

        self.__my_iot_mqtt_client.onOffline = on_offline
        self.__my_iot_mqtt_client.onOnline = on_online

        # start access
        self.__my_iot_mqtt_client.connect()

    def publish(self, IOT_TOPIC, unpacked_data):
        if not self.__is_connected:
            self.__my_iot_mqtt_client.connect()
        self.__my_iot_mqtt_client.publishAsync(IOT_TOPIC, str(unpacked_data), 1, ackCallback=None)


def main():
    iot_mqtt_client = IotMqttClient()

    count = 1
    while True:
       print(count)
       count += 1
       time.sleep(1)
       mes = create_msg()
       send_data = mes
       json_data = json.dumps(send_data)
       iot_mqtt_client.publish(TOPIC_NAME, json_data)

if __name__ == '__main__':
    main()
