#getter and Setter Method
class car:
        def __init__(self, a=100):
            self.speed=a
        def get_speed(self):
            return self._speed
        def set_speed(self, a):
            if a<=0 or a>=160:
                print("Speed needs to be betwwen 0 to 160")
            else:
                self._speed=a
        speed=property(get_speed, set_speed)
