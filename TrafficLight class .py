from time import sleep

class TrafficLight:
    __color = ['Red', 'Yellow', 'Green']

    def running(self):
        i = 0
        while i <=2:
            if i == 0:
                print(f'{TrafficLight.__color[i]} light')
                sleep(7)
                i +=1

            elif i == 1:
                print(f'{TrafficLight.__color[i]} light')
                sleep(2)
                i += 1

            elif i == 2:
                print(f'{TrafficLight.__color[i]} light')
                sleep(3)
                i = 0


TrafficLight = TrafficLight()
TrafficLight.running()




