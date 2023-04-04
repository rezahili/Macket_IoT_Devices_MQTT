# IoT Devices Macket 
Simulating IoT devices using a Macket app and sending its data to Mosquitto Broker. If you want Test you applications and You just need IoT deviecs macket that can produce data for you this repo will help you.
we have these devices for now:
* Fan
* Gas detector
* Current Sensor
* Temperture 
* Lux(light)
* Humidity
* Door(open or close)


If you need more devices contributing is very welcome and you can change it through [This File ](https://github.com/rezahili/Macket_IoT_Devices_MQTT/blob/main/macket/main.py)

## Installation:
clone this repository and run:

```
./setup.sh
```
you will have MQTT on port 1884(default) and macket app on host network. 

## Configuration:
### envfile.env config:
* changing mqtt port
* changing address of mqtt topic by defaul you can subscribe on "test/fan01" and get data from fan01 but you can use anaything instead of "test"
* changing Delay between sending data


[change envfile.env ](https://github.com/rezahili/Macket_IoT_Devices_MQTT/blob/main/envfile.env)

## Usage:
You can use any mqtt client to get data, for instance you can using mosquitto_client:
Installation:
```
sudo apt-get install mosquitto-clients
```
Usage:
* Fan:
```
mosquitto_sub -h '127.0.0.1' -p '1884' -t 'test/fan01'
```
you will get 0 (off) or 1(on)
* Gas:

```
mosquitto_sub -h '127.0.0.1' -p '1884' -t 'test/gas01'
```

you will get 0(not detected) or 1 (detected)
* Current Sensor:

```
mosquitto_sub -h '127.0.0.1' -p '1884' -t 'test/current01'
```
you will a get a number in A
* Temperture:

```
mosquitto_sub -h '127.0.0.1' -p '1884' -t 'test/temp01'
```
you will get a number in C
* Lux(light):
```
mosquitto_sub -h '127.0.0.1' -p '1884' -t 'test/lux01'
```
you will get a number in lux
* Humidity:

```
mosquitto_sub -h '127.0.0.1' -p '1884' -t 'test/humidity01'
```
you will get a number in %
* Door(open or close):

```
mosquitto_sub -h '127.0.0.1' -p '1884' -t 'test/door01'
```
you will get 0 (close) or 1 (open)


data for all of them is in JSON:

```
{"Value": 0}
```
## Contributing:
If you find this repo useful, please consider starring the repository. If you have any feedback or suggestions for improvement, feel free to contribute.
