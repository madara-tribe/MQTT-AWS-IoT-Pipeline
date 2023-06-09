# IoT Pipeline with AWS

This is data pipeline with AWS from Jetson Sensor data gathering to local PC analysis.

This sample pipeline is focused on just analyze (on local) Iot sensor data that gather from remote.

# Oveview diagram

![diagram](https://user-images.githubusercontent.com/48679574/232180376-ed365a01-23ee-4579-a02b-5aacc834276a.jpg)

# MQTT: from Jetson to AWS-IoT

Main transportation is MQTT that is used to send data to AWS IoT form Jetson
```sh
$ pythn3 Jetson/testMQTT.py
```


# References
- [aws-iot-device-sdk-python](https://github.com/aws/aws-iot-device-sdk-python)
- [Jetsonでのリアルタイム物体認識結果をWebで可視化](https://qiita.com/algopia/items/2eb4ec8d5bbd983b4656)
- [【AWS IoT】エッジデバイス（ラズパイ、Jetson nano）をAWS IoT Coreでプロビジョニングしてみた](https://qiita.com/hdmn54321/items/2b78b84f9bc852d206d1)
