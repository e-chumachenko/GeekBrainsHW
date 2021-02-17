import time


class TrafficLight:
    __color = ['Красный', 'Жёлтый', 'Зелёный']

    def running(self):
        while True:
            print(TrafficLight.__color[0])
            time.sleep(7)
            print(TrafficLight.__color[1])
            time.sleep(2)
            print(TrafficLight.__color[2])
            time.sleep(5)


t_light = TrafficLight()
t_light.running()
